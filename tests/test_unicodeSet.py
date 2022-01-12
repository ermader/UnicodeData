'''
Created on Apr 18, 2020
Converted to pytest on August 20, 2021

A subset of usettest.cpp from ICU.

@author: emader
'''

from UnicodeData.UnicodeSet import UnicodeSet

def _setFromBits(bits: int):
    s = UnicodeSet()

    for i in range(32):
        if bits & (1 << i) != 0:
            s.add(i)

    return s

def _bitsFromSet(s: UnicodeSet):
    bits = 0

    for i in range(32):
        if i in s:
            bits |= (1 << i)

    return bits

def _getPairs(set: UnicodeSet) -> str:
    pairs = ""

    for i in range(set.getRangeCount()):
        start = set.getRangeStart(i)
        end = set.getRangeEnd(i)
        pairs += f"{start:c}{end:c}"

    return pairs

def _testCompliment(bits: int, s: UnicodeSet):
    s = _setFromBits(bits)
    s.complement()
    c = _bitsFromSet(s)
    e = ~bits & 0xFFFFFFFF

    if c != e:
        print(f"  FAIL - {c:08X} != ~{bits:08X}")

def _testAdd(bits1: int, bits2: int):
    s1 = _setFromBits(bits1)
    s2 = _setFromBits(bits2)

    s1.addAll(s2)
    totalBits = _bitsFromSet(s1)

    assert totalBits == (bits1 | bits2), f"{totalBits:08X} != {bits1|bits2:08X}"

def _testRetain(bits1: int, bits2: int):
    s1 = _setFromBits(bits1)
    s2 = _setFromBits(bits2)

    s1.retainAll(s2)
    retainBits = _bitsFromSet(s1)

    assert retainBits == (bits1 & bits2), f"{retainBits:08X} != {bits1:08X} & {bits2:08X}"

def _testRemove(bits1: int, bits2: int):
    s1 = _setFromBits(bits1)
    s2 = _setFromBits(bits2)

    s1.removeAll(s2)
    removeBits = _bitsFromSet(s1)

    assert removeBits == (bits1 & (~bits2 & 0xFFFFFFFF)), f"{removeBits:08X} != {bits1:08X} & ~{bits2:08X}"

def _testXor(bits1: int, bits2: int):
    s1 = _setFromBits(bits1)
    s2 = _setFromBits(bits2)

    s1.complementAll(s2)
    complimentBits = _bitsFromSet(s1)

    assert complimentBits == (bits1 ^ bits2), f"{complimentBits:08X} != {bits1 ^ bits2:08X}"

def _expectPairs(set: UnicodeSet, expectedPairs: str, expectedSize: int):
    pairs = _getPairs(set)
    count = set.size()
    assert pairs == expectedPairs, f"expected {expectedPairs}, {expectedSize} = got {pairs}, {count}"

def test_addRemove():
    tt = UnicodeSet(range(ord('a'), ord('z') + 1))
    _expectPairs(tt, "az", 26)

    tt.removeRange(ord('m'), ord('p'))
    _expectPairs(tt, "alqz", 22)

    tt.removeRange(ord('e'), ord('g'))
    _expectPairs(tt, "adhlqz", 19)

    tt.removeRange(ord('d'), ord('i'))
    _expectPairs(tt, "acjlqz", 16)

    tt.removeRange(ord('c'), ord('r'))
    _expectPairs(tt, "absz", 10)

    tt.addRange(ord('f'), ord('q'))
    _expectPairs(tt, "abfqsz", 22)

    tt.removeRange(ord('a'), ord('g'))
    _expectPairs(tt, "hqsz", 18)

    tt.removeRange(ord('a'), ord('z'))
    _expectPairs(tt, "", 0)

    tt.add(ord('a'))
    tt.add(ord('b'))
    tt.add(ord('c'))
    _expectPairs(tt, "ac", 3)

    tt.add(ord('p'))
    tt.add(ord('q'))
    _expectPairs(tt, "acpq", 5)

def test_indexOf():
    # [a-cx-y3578]
    set = UnicodeSet(range(ord('a'), ord('c') + 1))
    set.addRange(ord('x'), ord('y'))
    set.add(ord('3'))
    set.add(ord('5'))
    set.addRange(ord('7'), ord('8'))

    for i in range(set.size()):
        c = set.charAt(i)
        if type(c) is int:
            assert set.indexOf(c) == i, f"charAt({i} = {c:c} => indexOf() = {set.indexOf(c)}"
        else:
            assert False, f"index {i} is not in the set"

def test_exhaustive():
    LIMIT = 128

    for i in range(LIMIT):
        tt = _setFromBits(i)
        _testCompliment(i, tt)

        for j in range(LIMIT):
            _testAdd(i, j)
            _testXor(i, j)
            _testRetain(i, j)
            _testRemove(i, j)

def test_operators():
    s1 = UnicodeSet(range(0x0915, 0x0941))
    s2 = UnicodeSet(range(0x0920, 0x0951))

    assert (s1 | s2) == UnicodeSet(range(0x0915, 0x0951)), f"s1 | s2 = {s1|s2}"
    assert (s1 & s2) == UnicodeSet(range(0x0920, 0x0941)), f"s1 & s2 = {s1&s2}"
    assert (s1 - s2) == UnicodeSet(range(0x0915, 0x0920)), f"s1 - s2 = {s1-s2}"
    assert (s1 ^ s2) == UnicodeSet(range(0x0915, 0x0920)) | UnicodeSet(range(0x0941, 0x0951)), f"s1 ^ s2 = {s1^s2}"
