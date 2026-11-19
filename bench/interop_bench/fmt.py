"""File-format track: infer a closed binary format from sample files and the vendor app's exports.

Each level mirrors how a real class of formats works:
  1  fixed-size records (sensor logs)
  2  tag-length-value records with varints (protobuf, BLE advertising data)
  3  self-describing definition + data messages (Garmin FIT)
  4  level 3 inside a compressed, obfuscated container, with delta-coded times and a string table
  5  write direction: produce files the hub accepts, which means recovering a custom CRC

decode() reads only the bytes and the format's constants, which proves the answer is in the file.
"""
import json, struct, zlib
from .core import (autokey, crc16_ccitt, crc16_custom, crc16_modbus, crc32, rbytes, read_varint, rng, unzigzag, varint, zigzag)

MODES = ["eco", "heat", "cool", "auto", "off", "boost"]
WORDS = ["kitchen", "attic", "garage", "porch", "cellar", "den", "hall", "loft", "shed", "yard", "lab", "pantry"]
CODES = ["door_open", "low_battery", "overheat", "reboot", "sync", "button"]


def _fields(r):
    fs = [{"name": "sensor_id", "t": "uint", "w": 2}, {"name": "ts", "t": "uint", "w": 4},
          {"name": "humidity", "t": "uint", "w": 1},
          {"name": "temp_c", "t": "fixed", "w": 2, "div": r.choice([10, 100]), "off": r.choice([0, -40])},
          {"name": "voltage", "t": "fixed", "w": 2, "div": r.choice([100, 1000]), "off": 0},
          {"name": "mode", "t": "enum", "w": 1, "map": dict(zip(r.sample(range(1, 200), len(MODES)), MODES))},
          {"name": "label", "t": "text"},
          {"name": "flags", "t": "flags", "w": 1, "bits": dict(zip(r.sample(range(8), 3), ["charging", "alarm", "door"]))}]
    r.shuffle(fs)
    return fs


def _raw(f, r):
    t = f["t"]
    if t == "uint":
        return r.randrange(1 << (8 * f["w"]))
    if t == "fixed":
        signed = f["off"] == 0 and f["name"] == "temp_c"
        return r.randrange(-1500, 3500) if signed else r.randrange(0, 12000)
    if t == "enum":
        return r.choice(list(f["map"]))
    if t == "flags":
        return sum(1 << b for b in f["bits"] if r.random() < 0.5)
    return r.choice(WORDS) + (str(r.randrange(10)) if r.random() < 0.5 else "")


def _show(f, raw, out):
    t = f["t"]
    if t == "fixed":
        out[f["name"]] = round(raw / f["div"] + f["off"], 3)
    elif t == "enum":
        out[f["name"]] = f["map"][raw]
    elif t == "flags":
        out.update({n: bool(raw >> b & 1) for b, n in f["bits"].items()})
    else:
        out[f["name"]] = raw


def _pack(f, raw, e):
    if f["t"] == "text":
        return raw.encode()[:12].ljust(12, b"\0")
    code = {1: "B", 2: "H", 4: "I"}[f["w"]]
    if raw < 0:
        code = code.lower()
    return struct.pack(e + code, raw)


def _unpack(f, b, e):
    if f["t"] == "text":
        return b.rstrip(b"\0").decode()
    signed = f["t"] == "fixed" and f["off"] == 0 and f["name"] == "temp_c"
    code = {1: "B", 2: "H", 4: "I"}[len(b)]
    return struct.unpack(e + (code.lower() if signed else code), b)[0]


def _size(f):
    return 12 if f["t"] == "text" else f["w"]


class Spec:
    def __init__(self, seed, level):
        self.seed, self.level = seed, level
        r = rng(seed, "fmt", level)
        self.magic = rbytes(r, 4)
        self.e = r.choice("<>")
        self.fields = _fields(r)
        self.tags = dict(zip([f["name"] for f in self.fields], r.sample(range(1, 250), len(self.fields))))
        self.crc = r.choice([crc16_ccitt, crc16_modbus])
        if level == 5:
            params = (r.getrandbits(16) | 1, r.getrandbits(16), r.getrandbits(16), r.random() < 0.5)
            self.crc = lambda b: crc16_custom(b, *params)
        self.event_fields = [{"name": "ts", "t": "uint", "w": 4},
                             {"name": "code", "t": "enum", "w": 1, "map": dict(zip(r.sample(range(1, 200), len(CODES)), CODES))},
                             {"name": "value", "t": "uint", "w": 2}]
        self.nums = dict(zip([f["name"] for f in self.fields] + ["code", "value", "evt_ts"], r.sample(range(1, 250), len(self.fields) + 3)))
        self.ids = r.sample(range(1, 250), 2)
        self.key = r.randrange(256)

    # ----- documents -----
    def sample(self, r):
        """A raw document. Levels 1-2 hold records; levels 3-4 hold samples and events."""
        recs = [self._rec(self.fields, r) for _ in range(r.randrange(3, 12))]
        if self.level == 4:
            t = r.randrange(1_600_000_000, 1_800_000_000)
            for rec in recs:
                t += r.randrange(1, 9000)
                rec["ts"] = t
        if self.level <= 2:
            if self.level == 2:
                for rec in recs:
                    for f in self.fields:
                        if f["name"] not in ("sensor_id", "ts") and r.random() < 0.2:
                            del rec[f["name"]]
            return {"records": recs}
        return {"samples": recs, "events": [self._rec(self.event_fields, r) for _ in range(r.randrange(1, 6))]}

    def _rec(self, fields, r):
        return {f["name"]: _raw(f, r) for f in fields}

    def show(self, raw):
        """What the vendor app displays for a raw document: the known plaintext and the expected answer."""
        def view(rec, fields):
            out = {}
            for f in fields:
                if f["name"] in rec:
                    _show(f, rec[f["name"]], out)
            return out
        if "records" in raw:
            return {"records": [view(x, self.fields) for x in raw["records"]]}
        return {"samples": [view(x, self.fields) for x in raw["samples"]],
                "events": [view(x, self.event_fields) for x in raw["events"]]}

    # ----- encode -----
    def encode(self, raw, r):
        return {1: self._enc1, 2: self._enc2, 3: self._enc3, 4: self._enc4, 5: self._enc3}[self.level](raw, r)

    def _enc1(self, raw, r):
        out = self.magic + bytes([1]) + struct.pack(self.e + "H", len(raw["records"]))
        for rec in raw["records"]:
            out += b"".join(_pack(f, rec[f["name"]], self.e) for f in self.fields)
        return out

    def _tlv(self, f, raw):
        t = f["t"]
        if t == "text":
            v = raw.encode()
        elif t == "fixed":
            v = varint(zigzag(raw))
        else:
            v = varint(raw)
        return bytes([self.tags[f["name"]]]) + varint(len(v)) + v

    def _enc2(self, raw, r):
        out = self.magic + varint(len(raw["records"]))
        for rec in raw["records"]:
            fs = [f for f in self.fields if f["name"] in rec]
            r.shuffle(fs)
            body = b"".join(self._tlv(f, rec[f["name"]]) for f in fs)
            out += varint(len(body)) + body
        return out + struct.pack(">H", self.crc(out))

    def _define(self, local, gid, fs, e):
        out = bytes([0x40 | local, 0 if e == "<" else 1, gid, len(fs)])
        for f in fs:
            num = self.nums["evt_ts" if gid == self.ids[1] and f["name"] == "ts" else f["name"]]
            out += bytes([num, 2 if f["t"] == "text" and self.level == 4 else _size(f)])
        return out

    def _stream(self, raw, r, pack=_pack):
        """Definition + data messages. A local type can be redefined mid-file with a new layout."""
        a = [(self.ids[0], self.fields, x) for x in raw["samples"]]
        c = [(self.ids[1], self.event_fields, x) for x in raw["events"]]
        items = []
        while a or c:  # interleave, keeping each list's own order
            items.append((a if a and (not c or r.random() < 0.7) else c).pop(0))
        out, active = b"", {}
        for gid, fields, rec in items:
            if gid not in active or r.random() < 0.25:
                fs = list(fields)
                r.shuffle(fs)
                e, local = r.choice("<>"), r.randrange(16)
                active = {g: v for g, v in active.items() if v[0] != local}
                active[gid] = (local, fs, e)
                out += self._define(local, gid, fs, e)
            local, fs, e = active[gid]
            out += bytes([local]) + b"".join(pack(f, rec[f["name"]], e) for f in fs)
        return out

    def _enc3(self, raw, r):
        body = self._stream(raw, r)
        out = self.magic + struct.pack(self.e + "I", len(body)) + body
        return out + struct.pack(">H", self.crc(out))

    def _enc4(self, raw, r):
        # Sample times become deltas from a base; labels become indexes into a string table.
        words = sorted({x["label"] for x in raw["samples"]})
        base = raw["samples"][0]["ts"]
        recs, prev = [], base
        for x in raw["samples"]:
            y = dict(x, ts=x["ts"] - prev, label=words.index(x["label"]))
            prev = x["ts"]
            recs.append(y)

        def pack(f, v, e):
            if f["t"] == "text":
                return struct.pack(e + "H", v)
            return _pack(f, v, e)
        table = bytes([len(words)]) + b"".join(bytes([len(w)]) + w.encode() for w in words)
        body = struct.pack(">I", base) + table + self._stream({"samples": recs, "events": raw["events"]}, r, pack)
        z = zlib.compress(body, 9)
        nonce = rbytes(r, 2)
        head = self.magic + nonce + struct.pack(self.e + "I", len(z)) + struct.pack(">I", crc32(body))
        return head + autokey(z, self.key ^ nonce[0] ^ nonce[1])

    # ----- reference decoder -----
    def decode(self, b):
        return {1: self._dec1, 2: self._dec2, 3: self._dec3, 4: self._dec4, 5: self.validate}[self.level](b)

    def _dec1(self, b):
        n = struct.unpack(self.e + "H", b[5:7])[0]
        i, recs = 7, []
        for _ in range(n):
            rec = {}
            for f in self.fields:
                rec[f["name"]] = _unpack(f, b[i:i + _size(f)], self.e)
                i += _size(f)
            recs.append(rec)
        return self.show({"records": recs})

    def _dec2(self, b):
        byname = {self.tags[f["name"]]: f for f in self.fields}
        n, i = read_varint(b, 4)
        recs = []
        for _ in range(n):
            size, i = read_varint(b, i)
            end, rec = i + size, {}
            while i < end:
                f = byname[b[i]]
                size2, i = read_varint(b, i + 1)
                v = b[i:i + size2]
                i += size2
                if f["t"] == "text":
                    rec[f["name"]] = v.decode()
                else:
                    x = read_varint(v, 0)[0]
                    rec[f["name"]] = unzigzag(x) if f["t"] == "fixed" else x
            recs.append(rec)
        return self.show({"records": recs})

    def _read_stream(self, b, i, end, read):
        """Walk the message stream. read(field, bytes, endian) turns one field into a raw value."""
        byname = {self.nums[f["name"]]: f for f in self.fields}
        evt = {self.nums["evt_ts"]: self.event_fields[0], self.nums["code"]: self.event_fields[1], self.nums["value"]: self.event_fields[2]}
        defs, out = {}, {"samples": [], "events": []}
        while i < end:
            h = b[i]
            i += 1
            if h & 0x40:
                e, gid, n = "<>"[b[i]], b[i + 1], b[i + 2]
                i += 3
                table = byname if gid == self.ids[0] else evt
                fs = []
                for _ in range(n):
                    fs.append((table[b[i]], b[i + 1]))
                    i += 2
                defs[h & 15] = (gid, fs, e)
            else:
                gid, fs, e = defs[h]
                rec = {}
                for f, size in fs:
                    rec[f["name"]] = read(f, b[i:i + size], e)
                    i += size
                out["samples" if gid == self.ids[0] else "events"].append(rec)
        return out

    def _dec3(self, b):
        n = struct.unpack(self.e + "I", b[4:8])[0]
        return self.show(self._read_stream(b, 8, 8 + n, _unpack))

    def validate(self, b):
        """The hub's import check at level 5: it refuses a file unless length and CRC are right."""
        if b[:4] != self.magic or len(b) < 10:
            raise ValueError("bad magic")
        if len(b) != 8 + struct.unpack(self.e + "I", b[4:8])[0] + 2:
            raise ValueError("bad length")
        if struct.unpack(">H", b[-2:])[0] != self.crc(b[:-2]):
            raise ValueError("bad checksum")
        return self._dec3(b)

    def unshow(self, doc):
        """Display values back to raw values, for the reference solution of the write direction."""
        def raw(rec, fields):
            out = {}
            for f in fields:
                n, t = f["name"], f["t"]
                if t == "fixed":
                    out[n] = round((rec[n] - f["off"]) * f["div"])
                elif t == "enum":
                    out[n] = {v: k for k, v in f["map"].items()}[rec[n]]
                elif t == "flags":
                    out[n] = sum(1 << b for b, x in f["bits"].items() if rec[x])
                else:
                    out[n] = rec[n]
            return out
        return {"samples": [raw(x, self.fields) for x in doc["samples"]], "events": [raw(x, self.event_fields) for x in doc["events"]]}

    def cover(self, raws):
        """Labeled files must show every enum value and flag state, or the task is unfair."""
        recs = [x for d in raws for x in d.get("records", d.get("samples"))]
        evts = [x for d in raws for x in d.get("events", [])]
        for fields, rows in ((self.fields, recs), (self.event_fields, evts)):
            for f in fields:
                if f["t"] == "enum":
                    for row, code in zip(rows, f["map"]):
                        row[f["name"]] = code
        flags = next(f for f in self.fields if f["t"] == "flags")
        recs[0]["flags"] = sum(1 << b for b in flags["bits"])
        recs[1]["flags"] = 0

    def _dec4(self, b):
        nonce = b[4:6]
        n = struct.unpack(self.e + "I", b[6:10])[0]
        z = autokey(b[14:14 + n], self.key ^ nonce[0] ^ nonce[1], decrypt=True)
        body = zlib.decompress(z)
        base = struct.unpack(">I", body[:4])[0]
        count, i, words = body[4], 5, []
        for _ in range(count):
            size = body[i]
            words.append(body[i + 1:i + 1 + size].decode())
            i += 1 + size

        def read(f, v, e):
            if f["t"] == "text":
                return words[struct.unpack(e + "H", v)[0]]
            return _unpack(f, v, e)
        doc = self._read_stream(body, i, len(body), read)
        for rec in doc["samples"]:
            base += rec["ts"]
            rec["ts"] = base
        return self.show(doc)


def instance(seed, level, n_samples=12, n_labeled=6):
    """Public artifacts: sample files, and the app's export for the first n_labeled of them."""
    spec = Spec(seed, level)
    r = rng(seed, "fmt-samples", level)
    raws = [spec.sample(r) for _ in range(n_samples)]
    spec.cover(raws[:n_labeled])
    files = {}
    for i, raw in enumerate(raws):
        files[f"samples/log{i:02d}.bin"] = spec.encode(raw, r)
        if i < n_labeled:
            files[f"samples/log{i:02d}.export.json"] = json.dumps(spec.show(raw), indent=1).encode()
    return spec, files


def hidden_tests(seed, level, n=25):
    """Generated only after the agent has finished. Returns [(bytes, expected)]."""
    spec = Spec(seed, level)
    r = rng(seed, "fmt-hidden", level)
    out = []
    for _ in range(n):
        raw = spec.sample(r)
        out.append((spec.encode(raw, r), spec.show(raw)))
    return out


def leaves(doc, path=""):
    """Flatten a document into {path: value} so answers can be scored field by field."""
    if isinstance(doc, dict):
        return {k2: v for k, x in doc.items() for k2, v in leaves(x, f"{path}/{k}").items()}
    if isinstance(doc, list):
        return {k2: v for i, x in enumerate(doc) for k2, v in leaves(x, f"{path}/{i}").items()}
    return {path: doc}


def same(a, b):
    if isinstance(a, bool) or isinstance(b, bool):
        return a is b
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return abs(a - b) < 1e-6
    return a == b


def score_doc(expected, got):
    """Share of expected leaf fields that match, penalized for invented fields."""
    e, g = leaves(expected), leaves(got) if isinstance(got, (dict, list)) else {}
    hits = sum(1 for k, v in e.items() if k in g and same(v, g[k]))
    return hits / max(len(e), len(g), 1)
