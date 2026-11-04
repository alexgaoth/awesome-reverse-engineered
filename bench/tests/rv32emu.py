"""Minimal RV32IM emulator, used only to prove the generated firmware does what the device does."""
M = 0xFFFFFFFF
STACK = 0x100000
STOP = 0xFFFFFFF0


def s32(v):
    return v - (1 << 32) if v & 0x80000000 else v


def sx(v, bits):
    return v - (1 << bits) if v & (1 << (bits - 1)) else v


def run(mem, pc, regs):
    r = [0] * 32
    r[2] = STACK - 64
    r[1] = STOP
    for i, v in enumerate(regs):
        r[10 + i] = v & M
    for _ in range(2_000_000):
        if pc == STOP:
            return r
        w = int.from_bytes(mem[pc:pc + 4], "little")
        op, rd, f3, rs1, rs2, f7 = w & 0x7F, w >> 7 & 31, w >> 12 & 7, w >> 15 & 31, w >> 20 & 31, w >> 25
        nxt = pc + 4
        if op == 0x37:
            v = w & 0xFFFFF000
        elif op == 0x13:
            imm = sx(w >> 20, 12)
            v = {0: r[rs1] + imm, 1: r[rs1] << (imm & 31), 4: r[rs1] ^ imm, 5: r[rs1] >> (imm & 31)}[f3]
        elif op == 0x33:
            a, b = r[rs1], r[rs2]
            v = a * b if f7 == 1 else {0: a + b, 4: a ^ b, 6: a | b}[f3]
        elif op == 0x03:
            at = (r[rs1] + sx(w >> 20, 12)) & M
            v = int.from_bytes(mem[at:at + 4], "little")
        elif op == 0x23:
            at = (r[rs1] + sx((w >> 25) << 5 | rd, 12)) & M
            mem[at:at + 4] = r[rs2].to_bytes(4, "little")
            pc = nxt
            continue
        elif op == 0x63:
            imm = sx((w >> 31) << 12 | (w >> 7 & 1) << 11 | (w >> 25 & 0x3F) << 5 | (w >> 8 & 15) << 1, 13)
            if {1: r[rs1] != r[rs2], 7: r[rs1] >= r[rs2]}[f3]:
                nxt = pc + imm
            pc = nxt
            continue
        elif op == 0x6F:
            imm = sx((w >> 31) << 20 | (w >> 12 & 0xFF) << 12 | (w >> 20 & 1) << 11 | (w >> 21 & 0x3FF) << 1, 21)
            v, nxt = pc + 4, pc + imm
        elif op == 0x67:
            v, nxt = pc + 4, (r[rs1] + sx(w >> 20, 12)) & M & ~1
        else:
            raise ValueError(f"bad instruction {w:08x} at {pc:#x}")
        if rd:
            r[rd] = v & M
        pc = nxt
    raise TimeoutError


def call(img, at, args):
    mem = bytearray(img) + bytearray(STACK + 4096 - len(img))
    r = run(mem, at, args)
    return r[10], r[11]


def check(img, at, data):
    mem = bytearray(img) + bytearray(STACK + 4096 - len(img))
    buf = 0x80000
    mem[buf:buf + len(data)] = data
    return run(mem, at, [buf, len(data)])[10]
