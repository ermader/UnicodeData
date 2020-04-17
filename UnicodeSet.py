'''
Created on Apr 14, 2020

A simplified version of the UnicodeSet class from ICU.

@author: emader
'''

UNICODE_SET_HIGH = 0x0110000
UNICODE_SET_LOW = 0x0000000

def _pinCodePoint(cp):
    if (cp < UNICODE_SET_LOW):
        cp = UNICODE_SET_LOW
    elif (cp > (UNICODE_SET_HIGH - 1)):
        cp = UNICODE_SET_HIGH - 1

    return cp

class UnicodeSet:
    def _findCodePoint(self, cp):
        if cp < self.list[0]:
            return 0

        length = len(self.list)
        lo = 0
        hi = length - 1

        # High runner test. cp is often after the last range
        # so this test pays off
        if lo >= hi or cp >= self.list[hi - 1]:
            return hi

        # invariant: cp >= list[lo]
        # invariant: cp < list[hi]

        while True:
            i = (lo + hi) >> 1

            if i == lo:
                break

            if cp < self.list[i]:
                hi = i
            else:
                lo = i

        return hi

    # polarity = 0 is normal: x intersect y
    # polarity = 2: x intersect ~y == set - minus
    # polarity = 1: ~x intersect y
    # polarity = 3: ~x intersect ~y
    def _retainList(self, other, polarity = 0):
        if other is None or len(other) == 0:
            return

        buffer = []

        # C++ code has:
        # int32_t i = 0, j = 0, k = 0
        # UChar32 a = list[i++]
        # UChar32 b = other[j++]
        i = 1
        j = 1
        a = self.list[0]
        b = other[0]

        # polarity bit 1 means a is second, bit 2 means b is.
        while True:
            if polarity == 0: # both first; drop the smaller
                if a < b: # drop a
                    a = self.list[i]
                    i += 1
                    polarity ^= 1
                elif b < a: # drop b
                    b = other[j]
                    j += 1
                    polarity ^= 2
                else: # a == b, take one, drop other
                    if a == UNICODE_SET_HIGH:
                        break
                    buffer.append(a)
                    a = self.list[i]
                    i += 1
                    polarity ^= 1
                    b = other[j]
                    j += 1
                    polarity ^= 2
            elif polarity == 3: # both second; take lower if unequal
                if a < b: # take a
                    buffer.append(a)
                    a = self.list[i]
                    i += 1
                    polarity ^= 1
                elif b < a: # take b
                    buffer.append(b)
                    b = other[j]
                    j += 1
                    polarity ^= 2
                else: # a == b, drop both!
                    if a == UNICODE_SET_HIGH:
                        break
                    a = self.list[i]
                    i += 1
                    polarity ^= 1
                    b = other[j]
                    j += 1
                    polarity ^= 2

            elif polarity == 1: # a second, b first; if b < a, overlap
                if a < b: # no overlap, drop a
                    a = self.list[i]
                    i += 1
                    polarity ^= 1
                elif b < a: # overlap, take b
                    buffer.append(b)
                    b = other[j]
                    j += 1
                    polarity ^= 2
                else: # a == b, drop both!
                    if a == UNICODE_SET_HIGH:
                        break
                    a = self.list[i]
                    i += 1
                    polarity ^= 1
                    b = other[j]
                    j += 1
                    polarity ^= 2

            elif polarity == 2: # a first, b second; if a < b, overlap
                if b < a: # no overlap, drop b
                    b = other[j]
                    j += 1
                    polarity ^= 2
                elif a < b: # overlap, take a
                    buffer.append(a)
                    a = self.list[i]
                    i += 1
                    polarity ^= 1
                else: # a == b, drop both!
                    if a == UNICODE_SET_HIGH:
                        break
                    a = self.list[i]
                    i += 1
                    polarity ^= 1
                    b = other[j]
                    j += 1
                    polarity ^= 2

        buffer.append(UNICODE_SET_HIGH)
        self.list = buffer

    # polarity = 0 is normal: x union y
    # polarity = 2: x union ~y
    # polarity = 1: ~x union y
    # polarity = 3: ~x union ~y
    def _addList(self, other, polarity = 0):
        if other is None or len(other) == 0:
            return

        buffer = []

        # C++ code has:
        # int32_t i = 0, j = 0, k = 0
        # UChar32 a = list[i++]
        # UChar32 b = other[j++]
        i = 1
        j = 1
        a = self.list[0]
        b = other[0]

        # polarity bit 1 means a is second, bit 2 means b is.
        while True:
            if polarity == 0: # both first, take lower if unequal
                if a < b: # take a
                    # Back up over overlapping ranges in buffer[]
                    if len(buffer) > 0 and a <= buffer[-1]:
                        a = max(self.list[i], buffer.pop())
                    else:
                        buffer.append(a)
                        a = self.list[i]

                    i += 1
                    polarity ^= 1
                elif b < a: # take b
                    if len(buffer) > 0 and b < buffer[-1]:
                        b = max(other[j], buffer.pop())
                    else:
                        buffer.append(b)
                        b = other[j]

                    j += 1
                    polarity ^= 2
                else: # a == b: take a, drop b
                    if a == UNICODE_SET_HIGH:
                        break
                    if len(buffer) > 0 and a < buffer[-1]:
                        a = max(self.list[i], buffer.pop())
                    else:
                        buffer.append(a)
                        a = self.list[i]

                    i += 1
                    polarity ^= 1
                    b = other[j]
                    j += 1
                    polarity ^= 2

            elif polarity == 3: # both second; take higher if unequal, and drop other
                if b <= a: # take a
                    if a == UNICODE_SET_HIGH:
                        break
                    buffer.append(a)
                else:
                    if b == UNICODE_SET_HIGH:
                        break
                    buffer.append(b)
                a = self.list[i]
                i += 1
                polarity ^= 1
                b = other[j]
                j += 1
                polarity ^= 2

            elif polarity == 1: # a second, b first; if b < a, overlap
                if a < b: # no overlap, take a
                    buffer.append(a)
                    a = self.list[i]
                    i += 1
                    polarity ^= 1
                elif b < a: # overlap, drop b
                    b = other[j]
                    j += 1
                    polarity ^= 2
                else: # a == b, drop both!
                    if a == UNICODE_SET_HIGH:
                        break
                    a = self.list[i]
                    i += 1
                    polarity ^= 1
                    b = other[j]
                    j += 1
                    polarity ^= 2

            elif polarity == 2: # a first, b second; if a < b, overlap
                if b < a: # no overlap, take b
                    buffer.append(b)
                    b = other[j]
                    j += 1
                    polarity ^= 2
                elif a < b: # overlap, drop a
                    a = self.list[i]
                    i += 1
                    polarity ^= 1
                else: # a == b, drop both!
                    if a == UNICODE_SET_HIGH:
                        break

                    a = self.list[i]
                    i += 1
                    polarity ^= 1
                    b = other[j]
                    j += 1
                    polarity ^= 2

        buffer.append(UNICODE_SET_HIGH)
        self.list = buffer

    # polarity = 0, 3 is normal: x xor y
    # polarity = 1, 2: x xor ~y == x === y

    def _exclusiveOrList(self, other, polarity = 0):
        if other is None or len(other) == 0:
            return

        buffer = []

        # C++ code has:
        # int32_t i = 0, j = 0, k = 0
        # UChar32 a = list[i++]
        # UChar32 b
        i = 1
        j = 1
        a = self.list[0]
        b = other[0]

        if polarity == 1 or polarity == 2:
            b = UNICODE_SET_LOW
            if other[0] == UNICODE_SET_LOW: # skip base if already LOW
                b = other[1]
        else:
            b = other[0]

        # simple: sort values, discarding identicals!
        while True:
            if a < b:
                buffer.append(a)
                a = self.list[i]
                i += 1
            elif b < a:
                buffer.append(b)
                b = other[j]
                j += 1
            elif a != UNICODE_SET_HIGH: # a == b, discard both
                a = self.list[i]
                i += 1
                b = other[j]
                j += 1
            else: # done!
                buffer.append(UNICODE_SET_HIGH)
                break

        self.list = buffer

    def add(self, cp):
        i = self._findCodePoint(_pinCodePoint(cp))

        if (i & 1) != 0:
            return

        if cp == self.list[i] - 1:
            self.list[i] = cp

            if cp == UNICODE_SET_HIGH - 1:
                self.list.append(UNICODE_SET_HIGH)

            if i > 0 and cp == self.list[i-1]:
                del self.list[i-1:i+1]

        elif i > 0 and cp == self.list[i-1]:
            self.list[i-1] += 1
        else:
            self.list[i:i] = [cp, cp+1]

    def addRange(self, start, end):
        if _pinCodePoint(start) < _pinCodePoint(end):
            length = len(self.list)
            limit = end + 1

            # Fast path for adding range after the last one
            if (length & 1) != 0:
                lastLimit = -2 if length == 1 else self.list[-2]
                if lastLimit <= start:
                    if lastLimit == start:
                        self.list[-2] = limit
                        if limit == UNICODE_SET_HIGH:
                            self.list.pop()
                    else:
                        self.list[-1] = start
                        if limit < UNICODE_SET_HIGH:
                            self.list.extend([limit, UNICODE_SET_HIGH])
                        else:
                            self.list.append(UNICODE_SET_HIGH)
                    return

            self._addList([start, limit, UNICODE_SET_HIGH])
        else:
            if start == end:
                self.add(start)

    def addAll(self, other):
        self._addList(other.list)

    def removeRange(self, start, end):
        if _pinCodePoint(start) < _pinCodePoint(end):
            other = [start, end + 1, UNICODE_SET_HIGH]
            self._retainList(other, 2) # polarity == 2 means set minus

    def remove(self, cp):
        self.removeRange(cp, cp)

    def removeAll(self, other):
        self._retainList(other.list, 2) # polarity == 2 means set minus

    def retainRange(self, start, end):
        if _pinCodePoint(start) < _pinCodePoint(end):
            other = [start, end + 1, UNICODE_SET_HIGH]
            self._retainList(other, 0) # polarity == 0 means intersect

    def retain(self, cp):
        self.retainRange(cp, cp)

    def retainAll(self, other):
        self._retainList(other.list, 0) # polarity == 0 means intersect

    def complimentRange(self, start, end):
        if _pinCodePoint(start) < _pinCodePoint(end):
            other = [start, end + 1, UNICODE_SET_HIGH]
            self._exclusiveOrList(other)

    def compliment(self, arg = None):
        if arg is None:
            if self.list[0] == UNICODE_SET_LOW:
                self.list = self.list[1:]
            else:
                self.list[0:0] = [UNICODE_SET_LOW]
        elif type(arg) == type(0):
            self.complimentRange(arg, arg)
        elif type(arg) == type(range(0)):
            self.complimentRange(arg.start, arg.stop - 1)
        else:
            raise(TypeError("Argument type must be int or range."))

    def complimentAll(self, other):
        self._exclusiveOrList(other.list)

    def clear(self):
        self.list = [UNICODE_SET_HIGH]

    def contains(self, arg):
        if type(arg) == type(0): # i.e. int
            i = self._findCodePoint(arg)
            return (i & 1) != 0
        elif type(arg) == type(range(0)):
            start = arg.start
            end = arg.stop - 1
            i = self._findCodePoint(start)
            return (i & 1) != 0 and end < self.list[i]
        else:
            raise(TypeError("Argument type must be int or range."))

    def __contains__(self, arg):
        return self.contains(arg)

    def __init__(self, arg = None):
        if arg is None:
            self.list = [UNICODE_SET_HIGH]
        elif type(arg) == type(0):
            self.list = [arg, arg + 1, UNICODE_SET_HIGH]
        elif type(arg) == type(range(0)):
            self.list = [arg.start, arg.stop, UNICODE_SET_HIGH]
        else:
            raise(TypeError("Argument type must be int or range."))

    def size(self):
        s = 0

        for index in range(self.getRangeCount()):
            start = self.getRangeStart(index)
            end = self.getRangeEnd(index)
            s += end - start + 1

        return s

    def getRangeCount(self):
        return len(self.list) // 2

    def getRangeStart(self, index):
        return self.list[index * 2]

    def getRangeEnd(self, index):
        return self.list[index * 2 + 1] - 1

    def dump(self):
        s = "["
        for cp in self.list:
            s += f"0x{cp:04X}, "


        print(f"{s[:-2]}]")

    def getRanges(self):
        ranges = []
        for i in range(0, len(self.list) - 1, 2):
            ranges.append(range(self.list[i], self.list[i+1]))

        return ranges

def setFromBits(bits):
    s = UnicodeSet()

    for i in range(32):
        if bits & (1 << i) != 0:
            s.add(i)

    return s

def bitsFromSet(s):
    bits = 0

    for i in range(32):
        if i in s:
            bits |= (1 << i)

    return bits

def getPairs(set):
    pairs = ""

    for i in range(set.getRangeCount()):
        start = set.getRangeStart(i)
        end = set.getRangeEnd(i)
        pairs += f"{start:c}{end:c}"

    return pairs

def testCompliment(bits, s):
    s = setFromBits(bits)
    s.compliment()
    c = bitsFromSet(s)

    if (c & 0xFFFFFFFF) != (~bits & 0xFFFFFFFF):
        print(f"  FAIL - {c:08X} != ~{bits:08X}")

def testAdd(bits1, bits2):
    s1 = setFromBits(bits1)
    s2 = setFromBits(bits2)

    s1.addAll(s2)
    totalBits = bitsFromSet(s1)

    if totalBits != (bits1 | bits2):
        print(f"  FAIL - {totalBits:08X} != {bits1|bbits2:08X}")

def testXor(bits1, bits2):
    s1 = setFromBits(bits1)
    s2 = setFromBits(bits2)

    s1.complimentAll(s2)
    complimentBits = bitsFromSet(s1)

    if complimentBits != (bits1 ^ bits2):
        print(f"  FAIL - {complimentBits:08X} != {bits1 ^ bits2:08X}")

def expectPairs(set, expectedPairs, expectedSize):
    pairs = getPairs(set)
    count = set.size()
    msg = f'  expect pairs "{expectedPairs}", size {expectedSize}: '
    if pairs != expectedPairs:
        msg += f'FAIL - got "{pairs}", size {count}.'
    else:
        msg += "PASS."

    print(msg)

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
    print("TestAddRemove:")
    tt = UnicodeSet(range(ord('a'), ord('z') + 1))
    expectPairs(tt, "az", 26)

    tt.removeRange(ord('m'), ord('p'))
    expectPairs(tt, "alqz", 22)

    tt.removeRange(ord('e'), ord('g'))
    expectPairs(tt, "adhlqz", 19)

    tt.removeRange(ord('d'), ord('i'))
    expectPairs(tt, "acjlqz", 16)

    tt.removeRange(ord('c'), ord('r'))
    expectPairs(tt, "absz", 10)

    tt.addRange(ord('f'), ord('q'))
    expectPairs(tt, "abfqsz", 22)

    tt.removeRange(ord('a'), ord('g'))
    expectPairs(tt, "hqsz", 18)

    tt.removeRange(ord('a'), ord('z'))
    expectPairs(tt, "", 0)

    tt.add(ord('a'))
    tt.add(ord('b'))
    tt.add(ord('c'))
    expectPairs(tt, "ac", 3)

    tt.add(ord('p'))
    tt.add(ord('q'))
    expectPairs(tt, "acpq", 5)

    print("\nTestExhaustive:")
    LIMIT = 128

    for i in range(LIMIT):
        tt = setFromBits(i)
        testCompliment(i, tt)

        for j in range(LIMIT):
            testAdd(i, j)
            testCompliment(i, j)
