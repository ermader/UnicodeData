'''\
Created on Apr 14, 2020

A simplified version of the UnicodeSet class from ICU.

@author: emader
'''

from __future__ import annotations


import typing

# from .Utilities import listOfCodes

UNICODE_SET_HIGH = 0x0110000
"""A value greater than all Unicode code points."""

UNICODE_SET_LOW = 0x0000000
"""The lowest valid Unicode code point."""


def _pinCodePoint(cp: int) -> int:
    """\
    Modify the given code point so that it is in the range [UNICODE_SET_LOW - UNICODE_SET_HIGH].
    Values less that UNICODE_SET_LOW will be set to UNICODE_SET_LOW and values greater than
    to UNICODE_SET_HIGH - 1 will be set to UNICODE_SET_HIGH - 1

    :param cp: the code point
    :return: the pinned value
    """
    if (cp < UNICODE_SET_LOW):
        cp = UNICODE_SET_LOW
    elif (cp > (UNICODE_SET_HIGH - 1)):
        cp = UNICODE_SET_HIGH - 1

    return cp


class UnicodeSet(object):
    """\
    A mutable set of Unicode characters.

    Legal code points are U+0000 to U+10FFFF inclusive.

    The iterface is similar to Python's set class. All
    operations of set are supported, except that they take
    a code point range, or a single code point instead of an
    arbitrary object.

    the API may be thought of in terms of boolean logic. An OR
    operation is implemented by add(), an AND operation is implemented
    by retain(), an XOR operation is implemented by complement() taking
    an argument, and a NOT operation is implemented by complement() with
    no argument.

    In terms of traditional set theory function names, add() is union,
    retain() is intersection,d remove() is asymmetric difference and
    compliment() with no arguments is set compliment with respect to the
    range [UNICODE_SET_LOW - UNICODE_SET_HIGH].
    """

    def _findCodePoint(self, cp: int) -> int:
        """\
        Returns the smallest value i such that cp < self.list[i]. Caller
        must insure that cp is a legal value or this function will enter
        an infinite loop.

        :param cp: a character in the range [UNICODE_SET_LOW - UNICODE_SET_HIGH]
        :return: the smallest integer i in the range [0 - len(self.list) - 1, inclusive such that cp less than self.list[i]
        """
        if cp < self.list[0]:
            return 0

        length = len(self.list)
        lo: int = 0
        hi: int = length - 1

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

    def _retainList(self, other:list[int], polarity: int = 0):
        """\
        Intersect with the list other, as controlled by polarity.

        polarity = 0: x intersect y\n
        polarity = 2: x intersect ~y (set-minus)\n
        polarity = 1: ~x intersect y\n
        polarity = 3: ~x intersect ~y\n

        :param other: the list with which to intersect
        :param polarity: the type of intersection, as described above. (default is 0)
        :return: self, to support chaining.
        """
        # if other is None or len(other) == 0:
        #     return

        buffer: list[int] = []

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

            elif polarity == 1: # a second, b first
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
        return self

    def _addList(self, other: list[int], polarity: int = 0):
        """\n
        Union the set with the list other, as controlled by polarity.

        polarity = 0: x union y\n
        polarity = 2: x union ~y\n
        polarity = 1: ~x union y\n
        polarity = 3: ~x union ~y\n

        :param other: the list with which to union.
        :param polarity: the type of union, as described above. (default is 0)
        :return: self, to support chaining.
        """
        # if other is None or len(other) == 0:
        #     return

        buffer: list[int] = []

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
        return self

    def _exclusiveOrList(self, other: list[int], polarity: int = 0):
        """\
        Xor the set with the list other, as controlled by polarity.

        polarity = 0, 3: x xor y\n
        polarity = 1, 2: x xor ~y (x === y)\n

        :param other: the list with which to xor
        :param polarity: the type of xor, as described above. (default is 0)
        :return: self, to support chaining.
        """
        # if other is None or len(other) == 0:
        #     return

        buffer: list[int] = []

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
        return self

    def add(self, cp: int):
        """\n
        Add the given code point to this set.

        :param cp: the code point to add.
        :return: self, to support chaining.
        """
        i = self._findCodePoint(_pinCodePoint(cp))

        if (i & 1) != 0:
            return self

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

        return self

    def addRange(self, start: int, end: int):
        """\
        Add the code points in the range start - end inclusive to this set.

        :param start: the first code point in the range to add.
        :param end: the last code point in the range to add.
        :return: self, to support chaining.
        """
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

            # This is slow. Could be much faster using findCodePoint(start)
            # and modifying the list, dealing with adjacent & overlapping ranges.
            self._addList([start, limit, UNICODE_SET_HIGH])
        else:
            if start == end:
                self.add(start)

        return self

    def addAll(self, other: UnicodeSet):
        """\n
        Add the code points in the set other to this set.

        :param other: the set from which to add.
        :return: self, to support chaining.
        """
        return self._addList(other.list)

    def removeRange(self, start: int, end: int):
        """\n
        Remove the code points in the range start - end inclusive from this set.

        :param start: the first code point in the range to remove.
        :param end: the last code point in the range to remove.
        :return: self, to support chaining.
        """
        if _pinCodePoint(start) < _pinCodePoint(end):
            other = [start, end + 1, UNICODE_SET_HIGH]
            self._retainList(other, 2) # polarity == 2 means set minus

        return self

    def remove(self, cp: int) -> UnicodeSet:
        """\n
        Remove the given code point from this set.

        :param cp: the code point to remove.
        :return: self, to support chaining.
        """
        return self.removeRange(cp, cp)

    def removeAll(self, other: UnicodeSet) -> UnicodeSet:
        """\n
        Remove all the code points in the set other from this set.

        :param other: the set whose code points should be removed.
        :return: self, to support chaining.
        """
        return self._retainList(other.list, 2) # polarity == 2 means set minus

    def retainRange(self, start: int, end: int):
        """\n
        Interset the code points in the range start - end inclusive with this set.

        :param start: the first code point in the range to intersect.
        :param end: the last code point in the range to intersect.
        :return: self, to support chaining.
        """
        if _pinCodePoint(start) < _pinCodePoint(end):
            other = [start, end + 1, UNICODE_SET_HIGH]
            self._retainList(other, 0) # polarity == 0: intersect

        return self

    def retain(self, cp: int):
        """\n
        Intersect the given code point with this set.

        :param cp: the code point to intersect with this set.
        :return: self, to support chaining.
        """
        return self.retainRange(cp, cp)

    def retainAll(self, other: UnicodeSet):
        """\n
        Interset the given set with this set.

        :param other: the set with which to intersect.
        :return: self, to support chaining.
        """
        return self._retainList(other.list, 0) # polarity == 0 means intersect

    def complementRange(self, start: int, end: int):
        """\n
        Complements the specified range of code points in this set. Any
        code point in the range will be removed if it is in the set, or will
        be added if it not in the set. If end < start, then the range is empty
        and the set will not be changed.

        :param start: the first code point in the range.
        :param end: the last code point in the range.
        :return: self, to support chaining.
        """
        if _pinCodePoint(start) < _pinCodePoint(end):
            other = [start, end + 1, UNICODE_SET_HIGH]
            self._exclusiveOrList(other)

        return self

    def complement(self, arg: typing.Union[int, range, None] = None):
        """\n
        Complement this set, based on the type of arg.

        arg is None: complement the whole set.\n
        arg is an int: complement the given code point.\n
        arg is a range: complement the code points in the range.

        :param arg: the arguement, as described above. (default is None)
        :return: self, to support chaining.
        """
        if arg is None:
            if self.list[0] == UNICODE_SET_LOW:
                self.list = self.list[1:]
            else:
                self.list[0:0] = [UNICODE_SET_LOW]
        elif type(arg) is int:
            self.complementRange(arg, arg)
        elif type(arg) is range:
            self.complementRange(arg.start, arg.stop - 1)
        else:
            raise(TypeError("Argument type must be int or range."))

        return self

    def complementAll(self, other: UnicodeSet):
        """\n
        Complement all the code points in the set other in this set.

        :param other: the other set.
        :return: self, to support chaining.
        """
        return self._exclusiveOrList(other.list)

    def clear(self):
        """Remove all code points from this set."""
        self.list = [UNICODE_SET_HIGH]
        return self

    def contains(self, arg: typing.Union[int, range]):
        """\n
        Check if this set contains the code points specified by arg.

        arg is an int: see if this set contains the given code pointn
        arg is a range: see if this set contains all the code points in the given range.\n

        :param arg: the code point, or range of code points, as described above.
        :return: True if the set contans the code point(s), False otherwise.
        """
        if type(arg) is int:
            i = self._findCodePoint(arg)
            return (i & 1) != 0
        elif type(arg) is range:
            start = arg.start
            end = arg.stop - 1
            i = self._findCodePoint(start)
            return (i & 1) != 0 and end < self.list[i]
        else:
            raise(TypeError("Argument type must be int or range."))

    # these match operations for Python's set type.
    def union(self, other: UnicodeSet):
        """\n
        Return the union of this set and other.

        :param other: the set with which to union this set.
        :return: the union of the two sets.
        """
        result = UnicodeSet(self)
        return result.addAll(other)

    def intersection(self, other: UnicodeSet):
        """\n
        Return the intersection of this set and other.

        :param other: the set with which to intersect this set.
        :return: the intersection of the two sets.
        """
        result = UnicodeSet(self)
        return result.retainAll(other)

    def difference(self, other: UnicodeSet):
        """\n
        Return the difference of this set and other.

        :param other: the set to remove from this set.
        :return: the difference of the two sets.
        """
        result = UnicodeSet(self)
        return result.removeAll(other)

    def symmetric_difference(self, other: UnicodeSet):
        """\n
        Return the xor of this set and other.

        :param other: the set with which to xor this set.
        :return: the xor of the two sets.
        """
        result = UnicodeSet(self)
        return result.complementAll(other)

    def __eq__(self, other: object):
        otherSet = typing.cast(UnicodeSet, other)
        return self.list == otherSet.list

    def __ne__(self, other: object):
        return not self == other

    def __or__(self, other: UnicodeSet):
        """Operator overload: | is union."""
        return self.union(other)

    def __and__(self, other: UnicodeSet):
        """Operator overload: & is intersection."""
        return self.intersection(other)

    def __sub__(self, other: UnicodeSet):
        """Operator overload: - is set difference."""
        return self.difference(other)

    def __xor__(self, other: UnicodeSet):
        """Operator overload: ^ is set xor."""
        return self.symmetric_difference(other)

    def __isub__(self, other: UnicodeSet) -> UnicodeSet:
        return self.removeAll(other)

    def __iand__(self, other: UnicodeSet):
        return self.retainAll(other)

    def __ior__(self, other: UnicodeSet):
        return self.addAll(other)

    def __ixor__(self, other: UnicodeSet):
        return self.complementAll(other)

    def __contains__(self, arg: typing.Union[int, range]):
        """Operator overload: in is contains."""
        return self.contains(arg)

    # T = typing.TypeVar("T", 'UnicodeSet', int, range)
    def __init__(self, arg: typing.Union[range, int, UnicodeSet, None] = None):
        """/
        Initialize a set, based on the type of arg:\n
        arg == None: make an empty set\n
        arg is a UnicodeSet: make a set containg the same elements as arg\n
        arg is an int: make a set containing the single code point\n
        arg is a range: make a set containing the code points in arg\n

        :param arg: the argument (default = None)
        """
        if arg is None:
            self.list: list[int] = [UNICODE_SET_HIGH]
        elif type(arg) is UnicodeSet:
            self.list = arg.list.copy()
        elif type(arg) is int:
            self.list = [arg, arg + 1, UNICODE_SET_HIGH]
        elif type(arg) is range:
            self.list = [arg.start, arg.stop, UNICODE_SET_HIGH]
        else:
            raise(TypeError("Argument type must be UnicodeSet, int or range."))

    def size(self):
        """Return the number of code points in this set."""
        s = 0

        for index in range(self.getRangeCount()):
            start = self.getRangeStart(index)
            end = self.getRangeEnd(index)
            s += end - start + 1

        return s

    def getRangeCount(self) -> int:
        """Return the number of code point ranges in this set."""
        return len(self.list) // 2

    def getRangeStart(self, index: int) -> int:
        """\n
        Get the starting code point of the given range.

        :param index: the index of the range. Must be less than getRangeCount().
        :return: the starting code point of the range.
        """
        return self.list[index * 2]

    def getRangeEnd(self, index: int) -> int:
        """\n
        Get the ending code point of the given range.

        :param index: the index of the range. Must be less than getRangeCount().
        :return: the ending code point of the range.
        """
        return self.list[index * 2 + 1] - 1

    def indexOf(self, cp: int) -> typing.Optional[int]:
        """\
        Return the index of the given code point within the set,
        where the set is ordered by ascending code point.

        :param cp: the code point.
        :return: the index or None if the code point is not in the set.
        """

        if cp < UNICODE_SET_LOW or cp > UNICODE_SET_HIGH:
            return None

        # the largest even integer <= the length of the list
        len2 = len(self.list) & ~1
        n = 0

        for i in range(0, len2, 2):
            start = self.list[i]

            if cp < start:
                break

            limit = self.list[i+1]

            if cp < limit:
                return n + cp - start

            n += limit - start

        return None

    def charAt(self, index: int) -> typing.Optional[int]:
        """\
        Return the code point at the given index within the set,
        where the set is ordered by ascending code point.

        :param index: the index.
        :return: the code point at the given index or None.
        """

        if index >= 0:
            # the largest even integer <= the length of the list
            len2 = len(self.list) & ~1
            for i in range(0, len2, 2):
                start = self.list[i]
                count = self.list[i+1] - start
                if index < count:
                    return start + index
                index -= count

        return None

    def __str__(self) -> str:
        """Return the code point list as a string."""

        pieces: list[str] = []

        for cp in self.list:
            pieces.append(f"0x{cp:04X}")

        s = ", ".join(pieces)

        return f"[{s}]"

    def dump(self):
        """Print the code point range list."""
        print(self)

    def getRanges(self):
        """Return the list of code point ranges in the set."""
        ranges: list[range] = []
        for i in range(0, len(self.list) - 1, 2):
            ranges.append(range(self.list[i], self.list[i+1]))

        return ranges

    def __iter__(self):
        for i in range(0, len(self.list) - 1, 2):
            for cp in range(self.list[i], self.list[i+1]):
                yield cp
