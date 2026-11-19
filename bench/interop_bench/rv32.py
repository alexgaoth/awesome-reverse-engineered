"""A tiny RV32IM assembler and firmware generator for protocol level 5.

Each instance gets machine code nobody has seen: a proprietary 32-bit frame check in real RISC-V, with
no symbols or strings. Frames are in the clear and nothing is secret, but the check cannot be derived
from traffic, so a client must read the routine in the vendor's public firmware. Decoys share its shape.
"""
import struct
from .core import rbytes, rng

M32 = 0xFFFFFFFF
X = dict(zero=0, ra=1, sp=2, t0=5, t1=6, t2=7, s0=8, s1=9, a0=10, a1=11, a2=12, a3=13, a4=14, s2=18, s3=19, s4=20, s5=21)


def _r(f7, rs2, rs1, f3, rd):
    return f7 << 25 | X[rs2] << 20 | X[rs1] << 15 | f3 << 12 | X[rd] << 7 | 0x33


def _i(imm, rs1, f3, rd, op=0x13):
    return (imm & 0xFFF) << 20 | X[rs1] << 15 | f3 << 12 | X[rd] << 7 | op


def _s(imm, rs2, rs1):
    return ((imm >> 5) & 0x7F) << 25 | X[rs2] << 20 | X[rs1] << 15 | 2 << 12 | (imm & 0x1F) << 7 | 0x23


def _b(imm, rs2, rs1, f3):
    return (((imm >> 12) & 1) << 31 | ((imm >> 5) & 0x3F) << 25 | X[rs2] << 20 | X[rs1] << 15 | f3 << 12
            | ((imm >> 1) & 0xF) << 8 | ((imm >> 11) & 1) << 7 | 0x63)


def _jal(imm, rd):
    return (((imm >> 20) & 1) << 31 | ((imm >> 1) & 0x3FF) << 21 | ((imm >> 11) & 1) << 20
            | ((imm >> 12) & 0xFF) << 12 | X[rd] << 7 | 0x6F)


RET = _i(0, "ra", 0, "zero", 0x67)


def li(rd, v):
    lo = ((v & 0xFFF) ^ 0x800) - 0x800
    hi = ((v - lo) >> 12) & 0xFFFFF
    return [hi << 12 | X[rd] << 7 | 0x37, _i(lo, rd, 0, rd)]


def make_mix(r):
    """A random mixing function of two 32-bit words: rounds of arithmetic that do not invert from data."""
    ops = [("mul", r.getrandbits(32) | 1), ("rot", r.randrange(3, 29)), ("addy",), ("mixy", r.randrange(3, 29))]
    ops += [r.choice([("add", r.getrandbits(32)), ("xor", r.getrandbits(32)), ("rot", r.randrange(3, 29)), ("xory",)]) for _ in range(r.randrange(2, 5))]
    r.shuffle(ops)
    return {"rounds": r.randrange(2, 5), "ops": ops}


def mix(fn, x, y):
    for _ in range(fn["rounds"]):
        for o in fn["ops"]:
            k = o[0]
            if k == "add":
                x = (x + o[1]) & M32
            elif k == "xor":
                x ^= o[1]
            elif k == "mul":
                x = (x * o[1]) & M32
            elif k == "rot":
                x = ((x << o[1]) | (x >> (32 - o[1]))) & M32
            elif k == "addy":
                x = (x + y) & M32
            elif k == "xory":
                x ^= y
            else:
                y ^= (x << o[1]) & M32
    return x


def check(fn, iv, y, data):
    """The firmware's frame check: one mix per 32-bit little-endian word, zero padded."""
    h = iv
    for i in range(0, len(data), 4):
        h = mix(fn, h ^ int.from_bytes(data[i:i + 4].ljust(4, b"\0"), "little"), y)
    return h


def asm_mix(fn):
    code = li("t2", fn["rounds"])
    loop = len(code)
    for o in fn["ops"]:
        k = o[0]
        if k in ("add", "xor", "mul"):
            code += li("t0", o[1])
            code.append({"add": _r(0, "t0", "a0", 0, "a0"), "xor": _r(0, "t0", "a0", 4, "a0"), "mul": _r(1, "t0", "a0", 0, "a0")}[k])
        elif k == "rot":
            code += [_i(o[1], "a0", 1, "t0"), _i(32 - o[1], "a0", 5, "t1"), _r(0, "t1", "t0", 6, "a0")]
        elif k == "addy":
            code.append(_r(0, "a1", "a0", 0, "a0"))
        elif k == "xory":
            code.append(_r(0, "a1", "a0", 4, "a0"))
        else:
            code += [_i(o[1], "a0", 1, "t0"), _r(0, "t0", "a1", 4, "a1")]
    code.append(_i(-1, "t2", 0, "t2"))
    code.append(_b((loop - len(code)) * 4, "zero", "t2", 1))
    return code + [RET]


def asm_check(here, target, iv, y):
    """check(buf, len), calling the mix routine at byte offset target."""
    regs = ["ra", "s0", "s1", "s2", "s5"]
    code = [_i(-32, "sp", 0, "sp")] + [_s(28 - 4 * i, x, "sp") for i, x in enumerate(regs)]
    code += [_i(0, "a0", 0, "s0"), _i(0, "a1", 0, "s1")] + li("s2", iv) + [_i(0, "zero", 0, "s5")]
    loop = len(code)
    branch = len(code)
    code.append(0)  # bgeu, patched once the end is known
    code += [_r(0, "s5", "s0", 0, "t1"), _i(0, "t1", 2, "t2", 0x03), _r(0, "t2", "s2", 4, "a0")] + li("a1", y)
    code.append(_jal(target - (here + len(code) * 4), "ra"))
    code += [_i(0, "a0", 0, "s2"), _i(4, "s5", 0, "s5")]
    code.append(_jal((loop - len(code)) * 4, "zero"))
    code[branch] = _b((len(code) - branch) * 4, "s1", "s5", 7)
    code.append(_i(0, "s2", 0, "a0"))
    code += [_i(28 - 4 * i, "sp", 2, x, 0x03) for i, x in enumerate(regs)]
    return code + [_i(32, "sp", 0, "sp"), RET]


def firmware(seed):
    """Returns (image, check parameters, offsets). The image is position independent raw flash."""
    r = rng(seed, "rv32")
    fns = [make_mix(r) for _ in range(4)]
    real = r.randrange(len(fns))
    iv, y = r.getrandbits(32), r.getrandbits(32)
    img = bytearray(rbytes(r, 0x400))
    off = {}

    def align():
        img.extend(b"\0" * (-len(img) % 16))
    for i, fn in enumerate(fns):
        align()
        off[i] = len(img)
        img += struct.pack(f"<{len(asm_mix(fn))}I", *asm_mix(fn))
        img += rbytes(r, r.randrange(8, 64))
    align()
    at = len(img)
    code = asm_check(at, off[real], iv, y)
    img += struct.pack(f"<{len(code)}I", *code)
    img += rbytes(r, 0x800)
    return bytes(img), (fns[real], iv, y), {"mix": off[real], "check": at}
