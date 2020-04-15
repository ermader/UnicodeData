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
    def findCodePoint(self, cp):
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

    def add(self, cp):
        i = self.findCodePoint(_pinCodePoint(cp))

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

    def _addList(self, list, priority = 0):
        pass

    def addRange(self, start, end):
        if _pinCodePoint(start) < _pinCodePoint(end):
            length = len(self.list)
            limit = end + 1

            # Fast path for adding range after the last one
            if (length & 1) != 0:
                lastLimit = -2 if length == 1 else self.list[length - 2]
                if lastLimit <= start:
                    if lastLimit == start:
                        self.list[length -2] = limit
                        if limit == UNICODE_SET_HIGH:
                            self.list.pop()
                    else:
                        self.list[length - 1] = start
                        if limit < UNICODE_SET_HIGH:
                            self.list.extend([limit, UNICODE_SET_HIGH])
                        else:
                            self.list.append(UNICODE_SET_HIGH)
                return

            self._addList([start, limit, UNICODE_SET_HIGH])
        else:
            if start == end:
                self.add(start)

    def contains(self, arg):
        if type(arg) == type(0): # i.e. int
            i = self.findCodePoint(arg)
            return (i & 1) != 0
        elif type(arg) == type(range(0)):
            start = arg.start
            end = arg.stop - 1
            i = self.findCodePoint(start)
            return (i & 1) != 0 and end < self.list[i]
        else:
            raise(TypeError("Argument type must be int or range."))

    # def containsRange(self, range):
    #     start = range.start
    #     end = range.stop - 1
    #     i = self.findCodePoint(start)
    #     return (i & 1) != 0 and end < self.list[i]

    def __contains__(self, arg):
        return self.contains(arg)

    def __init__(self):
        self.list = [UNICODE_SET_HIGH]

    def __init__(self, cp):
        self.list = [UNICODE_SET_HIGH]
        self.add(cp)

    def __init__(self, range):
        self.list = [UNICODE_SET_HIGH]
        self.add(range)

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
    print (0x915 in us)
    print (range(0x0915, 0x0817) in us)
