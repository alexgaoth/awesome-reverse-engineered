"""Shared primitives. Every instance derives from one seed, so a run can be reproduced exactly."""
import random, zlib

VERSION = "0.3"
LEVELS = (1, 2, 3, 4, 5)


def rng(seed, *salt):
    """Independent random stream for one purpose of one instance."""
    return random.Random(":".join(map(str, (seed, *salt))))


def rbytes(r, n):
    return bytes(r.randrange(256) for _ in range(n))


def sum8(b):
    return sum(b) & 0xFF


def xor8(b):
    x = 0
    for c in b:
        x ^= c
    return x


def crc16_ccitt(b):
    c = 0xFFFF
    for x in b:
        c ^= x << 8
        for _ in range(8):
            c = ((c << 1) ^ 0x1021) & 0xFFFF if c & 0x8000 else (c << 1) & 0xFFFF
    return c


def crc16_modbus(b):
    c = 0xFFFF
    for x in b:
        c ^= x
        for _ in range(8):
            c = (c >> 1) ^ 0xA001 if c & 1 else c >> 1
    return c


def crc16_custom(b, poly, init, xorout, reflect):
    """Vendors often pick their own CRC parameters, so standard tables do not match."""
    c = init
    for x in b:
        if reflect:
            x = int(f"{x:08b}"[::-1], 2)
        c ^= x << 8
        for _ in range(8):
            c = ((c << 1) ^ poly) & 0xFFFF if c & 0x8000 else (c << 1) & 0xFFFF
    if reflect:
        c = int(f"{c:016b}"[::-1], 2)
    return c ^ xorout


def crc32(b):
    return zlib.crc32(b) & 0xFFFFFFFF


def autokey(data, key, decrypt=False):
    """Each ciphertext byte keys the next one, as in the TP-Link Kasa local protocol."""
    out = bytearray()
    for b in data:
        c = b ^ key
        out.append(c)
        key = b if decrypt else c
    return bytes(out)


def varint(n):
    out = bytearray()
    while True:
        b = n & 0x7F
        n >>= 7
        if n:
            out.append(b | 0x80)
        else:
            out.append(b)
            return bytes(out)


def read_varint(b, i):
    n = shift = 0
    while True:
        c = b[i]
        i += 1
        n |= (c & 0x7F) << shift
        shift += 7
        if not c & 0x80:
            return n, i


def zigzag(n):
    return (n << 1) ^ (n >> 63)


def unzigzag(n):
    return (n >> 1) ^ -(n & 1)
