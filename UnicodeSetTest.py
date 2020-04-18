'''
Created on Apr 18, 2020

A subset of usettest.cpp from ICU.

@author: emader
'''

from UnicodeSet import UnicodeSet

def _setFromBits(bits):
    s = UnicodeSet()

    for i in range(32):
        if bits & (1 << i) != 0:
            s.add(i)

    return s

def _bitsFromSet(s):
    bits = 0

    for i in range(32):
        if i in s:
            bits |= (1 << i)

    return bits

def _getPairs(set):
    pairs = ""

    for i in range(set.getRangeCount()):
        start = set.getRangeStart(i)
        end = set.getRangeEnd(i)
        pairs += f"{start:c}{end:c}"

    return pairs

def _testCompliment(bits, s):
    s = _setFromBits(bits)
    s.compliment()
    c = _bitsFromSet(s)
    e = ~bits & 0xFFFFFFFF

    if c != e:
        print(f"  FAIL - {c:08X} != ~{bits:08X}")

def _testAdd(bits1, bits2):
    s1 = _setFromBits(bits1)
    s2 = _setFromBits(bits2)

    s1.addAll(s2)
    totalBits = _bitsFromSet(s1)

    if totalBits != (bits1 | bits2):
        print(f"  FAIL - {totalBits:08X} != {bits1|bits2:08X}")

def _testRetain(bits1, bits2):
    s1 = _setFromBits(bits1)
    s2 = _setFromBits(bits2)

    s1.retainAll(s2)
    retainBits = _bitsFromSet(s1)

    if retainBits != (bits1 & bits2):
        print(f"  FAIL - {retainBits:08X} != {bits1:08X} & {bits2:08X}")
    pass

def _testRemove(bits1, bits2):
    s1 = _setFromBits(bits1)
    s2 = _setFromBits(bits2)

    s1.removeAll(s2)
    removeBits = _bitsFromSet(s1)

    if removeBits != (bits1 & (~bits2 & 0xFFFFFFFF)):
        print(f"  FAIL = {removeBits:08X} != {bits1:08X} & ~{bits2:08X}")

def _testXor(bits1, bits2):
    s1 = _setFromBits(bits1)
    s2 = _setFromBits(bits2)

    s1.complimentAll(s2)
    complimentBits = _bitsFromSet(s1)

    if complimentBits != (bits1 ^ bits2):
        print(f"  FAIL - {complimentBits:08X} != {bits1 ^ bits2:08X}")

def _expectPairs(set, expectedPairs, expectedSize):
    pairs = _getPairs(set)
    count = set.size()
    msg = f'  expect pairs "{expectedPairs}", size {expectedSize}: '
    if pairs != expectedPairs:
        msg += f'FAIL - got "{pairs}", size {count}.'
    else:
        msg += "PASS."

    print(msg)

def testAddRemove():
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

def testExhaustive():
    LIMIT = 128

    for i in range(LIMIT):
        tt = _setFromBits(i)
        _testCompliment(i, tt)

        for j in range(LIMIT):
            _testAdd(i, j)
            _testCompliment(i, j)
            _testRetain(i, j)
            _testRemove(i, j)

        if i % 5 == 0:
            print(".", end="")

    print()

if __name__ == "__main__":
    us = UnicodeSet(0x0915)
    us.dump()
    us.add(0x0916)
    us.dump()
    us.add(0x0918)
    us.dump()
    us.add(0x0917)
    us.dump()
    us.add(0x0914)
    us.dump()
    us.addRange(0x0920, 0x0925)
    us.dump()
    us.addRange(0x0916, 0x0926)
    us.dump()
    print (0x915 in us)
    print (range(0x0915, 0x0817) in us)

    # These tests from ICU's usettest::testAddRemove()
    print("\nTestAddRemove:")
    testAddRemove()

    print("\nTestExhaustive:")
    testExhaustive()
