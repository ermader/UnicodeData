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

    def __init__(self):
        self.list = [UNICODE_SET_HIGH]

    def __init__(self, cp):
        self.list = [UNICODE_SET_HIGH]
        self.add(cp)

    def __init__(self, range):
        self.list = [UNICODE_SET_HIGH]
        self.add(range)

    def print(self):
        s = "["
        for cp in self.list:
            s += f"0x{cp:04X}, "


        print(f"{s[:-2]}]")

if __name__ == "__main__":
    us = UnicodeSet(0x0915)
    us.print()
    us.add(0x0916)
    us.print()
    us.add(0x0918)
    us.print()
    us.add(0x0917)
    us.print()
    us.add(0x0914)
    us.print()
