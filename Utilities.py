"""\
Uitility routines, etc.

Created on May 28, 2020

@author Eric Mader
"""

# import struct

class _object(object):
    """Useful for passing object instances to sstruct.unpack()"""
    pass

def isUnicodeNoncharacter(code):
    return code >= 0xfdd0 and \
     (code <= 0xfdef or (code & 0xfffe) == 0xfffe) and code <= 0x10ffff

_firstLead = 0xD800
_firstTrail = 0xDC00
_firstNonBMP = 0x10000
_leadShift = 10
_surrogateMask = 0xFFFFFC00
_trailMask = 0xFFFFFFFF - _surrogateMask
_surrogateOffset = (_firstLead << _leadShift) + _firstTrail - _firstNonBMP
_leadOffset = _firstLead - (_firstNonBMP >> _leadShift)

def isLead(code):
    return (code & _surrogateMask) == _firstLead

def isTrail(code):
    return (code & _surrogateMask) == _firstTrail

def charFromSurrogates(lead, trail):
    return (lead << _leadShift) + trail - _surrogateOffset

def surrogatesFromChar(ch):
    lead = (ch >> _leadShift) + _leadOffset
    trail = (ch & _trailMask) + _firstTrail
    return lead, trail

def arithmeticShift(value, bitsInWord, bitsInField):
    """\
    Arithmetic right shifts the top bits in a word.

    :param value: the value to be shifted
    :param bitsInWord: the number of bits in a word
    :param bitsInField: the number of top bits
    :returns: the signed value of the top bits
    """
    signBit = 1 << (bitsInWord - 1)
    shift = bitsInWord - bitsInField
    result = value >> shift

    return result - (1 << bitsInField) if (value & signBit) != 0 else result

def highBit(value):
    """\
    Return the bit number of the highest bit set in a value.

    :param value: the value. Can be up to 64 bits long
    :returns: the bit number, counting from the low order bit
    """
    bit = 0

    if value == 0: return None  # return None if no bits are set

    # binary search through the bits, looking for the highest one
    if value >= 1 << 32:
        value >>= 32
        bit += 32

    if value >= 1 << 16:
        value >>= 16
        bit += 16

    if value >= 1 << 8:
        value >>= 8
        bit += 8

    if value >= 1 << 4:
        value >>= 4
        bit += 4

    if value >= 1 << 2:
        value >>= 2
        bit += 2

    if value >= 1 << 1:
        value >>= 1
        bit += 1

    return bit

# There doesn't seem to be any use for this...
# def unpackArray(data, dataOffset, dataFormat):
#     itemLength = struct.calcsize(dataFormat)
#     arrayOffset = dataOffset + itemLength
#     itemCount, = struct.unpack(dataFormat, data[dataOffset:arrayOffset])
#     arrayLimit = arrayOffset + (itemCount * itemLength)
#     return struct.unpack(f"{itemCount}{dataFormat}", data[arrayOffset:arrayLimit])

def listOFCodes(codes):
    codeList = [f"{code:04X}" for code in codes]
    return ", ".join(codeList)

def test():
    print("isLead test:")
    failures = []
    for code in range(_firstLead, _firstTrail):
        if not isLead(code):
            failures.append(code)
    if len(failures) == 0:
        print("    Passed!")
    else:
        print(f"    Failed: [{listOFCodes(failures)}]")

    print("isTrail test:")
    failures = []
    for code in range(_firstTrail, 0xE000):
        if not isTrail(code):
            failures.append(code)
    if len(failures) == 0:
        print("    Passed!")
    else:
        print(f"    Failed: [{listOFCodes(failures)}]")
    print()

    ch = charFromSurrogates(0xD850, 0xDEEE)
    high, low = surrogatesFromChar(ch)
    print(f"ch = {ch:04X}, high = {high:04X}, low = {low:04X}")
    print()

    for n in range(0, 0x10, 2):
        print(f"highBit(0x{n:04X}) = {highBit(n)}")

    print(f"highBit(0x3FF) = {highBit(0x3FF)}")
    print(f"highBit(0xFFFFFC00) = {highBit(0xFFFFFC00)}")
    print(f"highBit(0x200000000) = {highBit(0x200000000)}")
    print(f"highBit(0x123456789ABCDEF) = {highBit(0x123456789ABCDEF)}")

if __name__ == "__main__":
    test()