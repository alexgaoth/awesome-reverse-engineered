"""Protocol track: infer a closed device protocol from captures and a live unit.

Each level mirrors a real family of local device protocols:
  1  plain framing and a checksum (hobby serial and TCP gear)
  2  length prefix, autokey XOR, sequence numbers (TP-Link Kasa)
  3  hello, per-session key from a nonce and a device id, stamps, CRC (Xiaomi miIO)
  4  messy evidence: mostly unlabeled captures, fragmented messages, push telemetry, a custom CRC
  5  level 4, but the frame check exists only as RISC-V machine code in the public firmware

Levels 4 and 5 carry no keys and no encryption, by design: the index excludes decryption and security
bypasses, and this benchmark stays inside the same scope. Their difficulty is ordinary interoperability.

Device is sans-IO, so captures, the live TCP unit and the hidden tests all run the same code.
"""
import json, random, socket, socketserver, struct, threading
from . import rv32
from .core import autokey, crc16_ccitt, crc16_custom, crc16_modbus, rbytes, rng, sum8, xor8

MODES = ["eco", "heat", "auto", "away"]
NAMES = ["kitchen", "attic", "garage", "porch", "cellar", "den", "hall", "loft"]
MAX_NAME = 32  # a long name would overflow the one-byte payload length of a status reply
NACK = 0x7F
TELEMETRY = 0x7E  # levels 4-5: frames the device pushes on its own
FRAGMENT = 6      # levels 4-5: payload bytes per frame


class Bad(Exception):
    pass


class Spec:
    def __init__(self, seed, level):
        self.seed, self.level = seed, level
        r = rng(seed, "proto", level)
        self.magic = rbytes(r, 2)
        self.e = r.choice("<>")
        self.cmds = dict(zip(["status", "power", "temp", "mode", "rename", "open"], r.sample(range(1, 120), 6)))
        self.version = rbytes(r, 2)
        self.div = r.choice([2, 10, 100])
        self.on, self.off = r.sample(range(1, 250), 2)
        self.modes = dict(zip(MODES, r.sample(range(1, 250), len(MODES))))
        self.order = r.sample(["power", "temp", "mode", "name"], 4)
        self.chk = r.choice([sum8, xor8])
        self.crc = r.choice([crc16_ccitt, crc16_modbus])
        self.key0 = r.randrange(256)
        self.K = rbytes(r, 4)
        if level == 4:
            params = (r.getrandbits(16) | 1, r.getrandbits(16), r.getrandbits(16), r.random() < 0.5)
            self.seal = lambda b: struct.pack(">H", crc16_custom(b, *params))
            self.seal_size = 2
        if level == 5:
            self.fw, params, _ = rv32.firmware(seed)
            self.seal = lambda b: struct.pack("<I", rv32.check(*params, b))
            self.seal_size = 4

    def units(self, i):
        return rng(self.seed, "unit", self.level, i).getrandbits(32).to_bytes(4, "big")

    def frame_len(self, b):
        if len(b) < (6 if self.level >= 4 else 5):
            return None
        if self.level >= 4:
            return 6 + b[5] + self.seal_size
        if self.level == 1:
            return 4 + b[3] + 1
        if self.level == 2:
            return 4 + struct.unpack(">I", b[:4])[0]
        return 8 + struct.unpack(self.e + "H", b[2:4])[0] + 2

    def reply_end(self, b):
        """Length of the first complete reply in b, or None. Replies can span frames and follow telemetry."""
        i = 0
        while True:
            n = self.frame_len(b[i:])
            if n is None or len(b) < i + n:
                return None
            i += n
            if self.level < 4 or (b[i - n + 2] & 1 == 0 and b[i - n + 4] != TELEMETRY):
                return i

    # Payloads
    def enc_status(self, st):
        out = b""
        for k in self.order:
            if k == "power":
                out += bytes([self.on if st["power"] else self.off])
            elif k == "temp":
                out += struct.pack(self.e + "h", round(st["temp"] * self.div))
            elif k == "mode":
                out += bytes([self.modes[st["mode"]]])
            else:
                out += bytes([len(st["name"])]) + st["name"].encode()
        return out

    def dec_status(self, b):
        st, i = {}, 0
        modes = {v: k for k, v in self.modes.items()}
        for k in self.order:
            if k == "power":
                st["power"], i = b[i] == self.on, i + 1
            elif k == "temp":
                st["temp"], i = struct.unpack(self.e + "h", b[i:i + 2])[0] / self.div, i + 2
            elif k == "mode":
                st["mode"], i = modes[b[i]], i + 1
            else:
                st["name"], i = b[i + 1:i + 1 + b[i]].decode(), i + 1 + b[i]
        return st


class Channel:
    """One side of a session: frames and unframes messages for the current level."""

    def __init__(self, spec, server):
        self.s, self.server = spec, server
        self.seq = self.stamp = self.tx = 0
        self.key = None

    def _xor3(self, data, stamp):
        return bytes(b ^ self.key[i % 4] ^ (stamp & 0xFF) for i, b in enumerate(data))

    def wrap(self, cmd, payload):
        s, plain = self.s, bytes([cmd]) + payload
        if s.level == 1:
            body = bytes([cmd, len(payload)]) + payload
            return s.magic + body + bytes([s.chk(body)])
        if s.level == 2:
            if not self.server:
                self.seq = (self.seq + 1) & 0xFF
            c = autokey(bytes([self.seq]) + plain, s.key0)
            return struct.pack(">I", len(c)) + c
        if s.level == 3:
            if not self.server:
                self.stamp += 1
            c = self._xor3(plain, self.stamp)
            f = s.magic + struct.pack(s.e + "H", len(c)) + struct.pack(s.e + "I", self.stamp) + c
            return f + struct.pack(">H", s.crc(f))
        out = b""
        chunks = [payload[i:i + FRAGMENT] for i in range(0, len(payload), FRAGMENT)] or [b""]
        for i, part in enumerate(chunks):
            self.tx = (self.tx + 1) & 0xFF
            f = s.magic + bytes([int(i < len(chunks) - 1), self.tx, cmd, len(part)]) + part
            out += f + s.seal(f)
        return out

    def unwrap(self, f):
        s = self.s
        if s.level == 1:
            if f[:2] != s.magic:
                raise Bad(1)
            if s.chk(f[2:-1]) != f[-1]:
                raise Bad(2)
            return f[2], f[4:-1]
        if s.level == 2:
            p = autokey(f[4:], s.key0, decrypt=True)
            if self.server:
                if p[0] != (self.seq + 1) & 0xFF:
                    raise Bad(3)
                self.seq = p[0]
            return p[1], p[2:]
        if s.level == 3:
            if f[:2] != s.magic:
                raise Bad(1)
            if s.crc(f[:-2]) != struct.unpack(">H", f[-2:])[0]:
                raise Bad(2)
            stamp = struct.unpack(s.e + "I", f[4:8])[0]
            if self.server and stamp <= self.stamp:
                raise Bad(3)
            if self.server:
                self.stamp = stamp
            p = self._xor3(f[8:-2], stamp)
            return p[0], p[1:]
        if f[:2] != s.magic:
            raise Bad(1)
        if s.seal(f[:-s.seal_size]) != f[-s.seal_size:]:
            raise Bad(2)
        if self.server:
            if f[3] != (self.seq + 1) & 0xFF:
                raise Bad(3)
            self.seq = f[3]
        return f[4], f[6:-s.seal_size], f[2] & 1

    def read_reply(self, b):
        """One whole reply: at levels 4-5, skip telemetry and join fragments."""
        if self.s.level < 4:
            return self.unwrap(b)
        i, joined = 0, b""
        while i < len(b):
            n = self.s.frame_len(b[i:])
            cmd, p, more = self.unwrap(b[i:i + n])
            i += n
            if cmd != TELEMETRY:
                joined += p
                if not more:
                    return cmd, joined
        raise Bad(9)


class Device:
    def __init__(self, spec, unit, state, seed):
        self.spec, self.unit, self.state = spec, unit, dict(state)
        self.r = random.Random(seed)
        self.lock = threading.Lock()

    def session(self):
        return Session(self, random.Random(self.r.getrandbits(64)))

    def execute(self, cmd, p):
        s, st = self.spec, self.state
        c = s.cmds
        with self.lock:
            if cmd == c["status"]:
                return s.enc_status(st)
            if cmd == c["power"] and len(p) == 1 and p[0] in (s.on, s.off):
                st["power"] = p[0] == s.on
            elif cmd == c["temp"] and len(p) == 2:
                st["temp"] = struct.unpack(s.e + "h", p)[0] / s.div
            elif cmd == c["mode"] and len(p) == 1 and p[0] in s.modes.values():
                st["mode"] = {v: k for k, v in s.modes.items()}[p[0]]
            elif cmd == c["rename"] and p and p[0] == len(p) - 1 and p[0] <= MAX_NAME:
                st["name"] = p[1:].decode(errors="replace")
            else:
                raise Bad(4)
        return b"\x00"


class Session:
    def __init__(self, dev, r):
        self.dev, self.r, self.s = dev, r, dev.spec
        self.ch = Channel(dev.spec, True)
        self.buf, self.part, self.closed = b"", b"", False
        self.ready = self.s.level < 3

    def feed(self, data):
        self.buf += data
        out = b""
        while not self.closed:
            n = self.s.frame_len(self.buf)
            if n is None or len(self.buf) < n:
                break
            if n > 4096:
                self.closed = True
                break
            f, self.buf = self.buf[:n], self.buf[n:]
            out += self.on_frame(f)
        return out

    def on_frame(self, f):
        try:
            if not self.ready:
                return self.hello(f)
            if self.s.level < 4:
                cmd, p = self.ch.unwrap(f)
                return self.ch.wrap(cmd | 0x80, self.dev.execute(cmd, p))
            cmd, p, more = self.ch.unwrap(f)
            self.part += p
            if more:
                return b""
            p, self.part = self.part, b""
            out = self.ch.wrap(cmd | 0x80, self.dev.execute(cmd, p))
            return self.ch.wrap(TELEMETRY, rbytes(self.r, 3)) + out if self.r.random() < 0.4 else out
        except (Bad, IndexError, struct.error) as ex:
            return self.ch.wrap(NACK, bytes([ex.args[0] if isinstance(ex, Bad) else 5]))

    def hello(self, f):
        s, ch = self.s, self.ch
        if s.level >= 4:
            cmd, p, _ = ch.unwrap(f)
            if cmd != s.cmds["open"] or p != s.version:
                raise Bad(6)
            self.ready = True
            return ch.wrap(cmd | 0x80, self.dev.unit)
        if f[:2] != s.magic or len(f) != 10 or s.crc(f[:-2]) != struct.unpack(">H", f[-2:])[0]:
            self.closed = True
            return b""
        nonce = rbytes(self.r, 4)
        ch.stamp = self.r.getrandbits(30)
        ch.key = derive3(s, self.dev.unit, nonce)
        head = s.magic + struct.pack(s.e + "H", 8) + struct.pack(s.e + "I", ch.stamp)
        r = head + self.dev.unit + nonce
        self.ready = True
        return r + struct.pack(">H", s.crc(r))


def derive3(s, unit, nonce):
    return bytes(a ^ b ^ c for a, b, c in zip(nonce, unit, s.K))


class Client:
    """Reference client. xfer(bytes) returns the device's reply bytes."""

    def __init__(self, spec, xfer, r):
        self.s, self.xfer = spec, xfer
        self.ch = Channel(spec, False)
        s, ch = spec, self.ch
        if s.level == 3:
            f = s.magic + struct.pack(s.e + "H", 0) + struct.pack(s.e + "I", 0)
            b = xfer(f + struct.pack(">H", s.crc(f)))
            ch.stamp = struct.unpack(s.e + "I", b[4:8])[0]
            ch.key = derive3(s, b[8:12], b[12:16])
        elif s.level >= 4:
            ch.read_reply(xfer(ch.wrap(s.cmds["open"], s.version)))

    def call(self, name, payload=b""):
        cmd, p = self.ch.read_reply(self.xfer(self.ch.wrap(self.s.cmds[name], payload)))
        if cmd == NACK:
            raise Bad(p[0])
        return p

    def status(self):
        return self.s.dec_status(self.call("status"))

    def set_power(self, v):
        self.call("power", bytes([self.s.on if v == "on" else self.s.off]))

    def set_temp(self, v):
        self.call("temp", struct.pack(self.s.e + "h", round(float(v) * self.s.div)))

    def set_mode(self, v):
        self.call("mode", bytes([self.s.modes[v]]))

    def rename(self, v):
        self.call("rename", bytes([len(v)]) + v.encode())


def _state(r):
    return {"power": r.random() < 0.5, "temp": r.randrange(32, 57) / 2, "mode": r.choice(MODES), "name": r.choice(NAMES)}


def _ops(r, n, cover=False):
    ops = []
    if cover:  # captures always show every mode and both power states, so the task is fair
        ops += [("set_mode", m) for m in MODES] + [("set_power", "on"), ("set_power", "off")]
    while len(ops) < n:
        k = r.choice(["status", "set_power", "set_temp", "set_mode", "rename"])
        v = {"set_power": r.choice(["on", "off"]), "set_temp": str(r.randrange(20, 60) / 2), "set_mode": r.choice(MODES),
             "rename": r.choice(NAMES) + str(r.randrange(100))}.get(k)
        ops.append((k,) if k == "status" else (k, v))
    r.shuffle(ops)
    return ops


def _say(op):
    return {"status": "open the status page", "set_power": "turn power {}", "set_temp": "set the target to {} C",
            "set_mode": "switch mode to {}", "rename": "rename the unit to {}"}[op[0]].format(*op[1:])


def instance(seed, level, n_sessions=4):
    """Public artifacts: annotated captures from several units, and firmware at level 4."""
    spec = Spec(seed, level)
    r = rng(seed, "proto-capture", level)
    lines = ["# Traffic between the vendor app and two units. '>' app to device, '<' device to app. Hex.", ""]
    for i in range(n_sessions):
        dev = Device(spec, spec.units(i % 2), _state(r), r.getrandbits(64))
        sess = dev.session()
        lines.append(f"## Session {i + 1}, unit {'AB'[i % 2]}")

        def xfer(b):
            lines.append("> " + b.hex())
            out = sess.feed(b)
            lines.append("< " + out.hex())
            return out
        c = Client(spec, xfer, r)
        labeled = level < 4 or i == 0  # from level 4 only the first session is annotated
        for op in _ops(r, 9, cover=i == 0):
            if labeled:
                lines.append(f"# user: {_say(op)}")
            shown = getattr(c, op[0])(*op[1:])
            if shown and labeled:
                lines.append("# app shows: " + json.dumps(shown))
        lines.append("")
    files = {"capture.txt": "\n".join(lines).encode()}
    if level == 5:
        files["firmware.bin"] = spec.fw
    return spec, files


class Live:
    """A unit listening on localhost. Its secrets exist only in this process's memory."""

    def __init__(self, dev):
        class Handler(socketserver.BaseRequestHandler):
            def handle(h):
                h.request.settimeout(30)
                sess = dev.session()
                try:
                    while not sess.closed:
                        data = h.request.recv(4096)
                        if not data:
                            break
                        out = sess.feed(data)
                        if out:
                            h.request.sendall(out)
                except OSError:
                    pass

        class Server(socketserver.ThreadingTCPServer):
            allow_reuse_address = True
            daemon_threads = True
        self.srv = Server(("127.0.0.1", 0), Handler)
        self.port = self.srv.server_address[1]
        threading.Thread(target=self.srv.serve_forever, daemon=True).start()

    def close(self):
        self.srv.shutdown()
        self.srv.server_close()


def live_unit(seed, level, which):
    """which: 'public' is the unit the agent can poke; 'hidden' is a new unit used only for scoring."""
    spec = Spec(seed, level)
    r = rng(seed, "proto-unit", level, which)
    return Device(spec, spec.units(7 if which == "public" else 8), _state(r), r.getrandbits(64))


def hidden_ops(seed, level, n=30):
    return _ops(rng(seed, "proto-ops", level), n)


def tcp_client(spec, port, r):
    """Reference client over TCP, used by self-tests."""
    sock = socket.create_connection(("127.0.0.1", port), timeout=5)

    def xfer(b):
        sock.sendall(b)
        buf = b""
        while True:
            if spec.reply_end(buf):
                return buf
            d = sock.recv(4096)
            if not d:
                raise Bad(9)
            buf += d
    return sock, Client(spec, xfer, r)
