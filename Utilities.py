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
_surrogateOffset = (_firstLead << 10) + _firstTrail - 0x10000
_leadOffset = _firstLead - (0x10000 >> 10)

def isLead(code):
    return (code & 0xfffffc00) == _firstLead

def charFromSurrogates(lead, trail):
    return (lead << 10) + trail - _surrogateOffset

def surrogatesFromChar(ch):
    lead = (ch >> 10) + _leadOffset
    trail = (ch & 0x03FF) + 0xDC00
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

# There doesn't seem to be any use for this...
# def unpackArray(data, dataOffset, dataFormat):
#     itemLength = struct.calcsize(dataFormat)
#     arrayOffset = dataOffset + itemLength
#     itemCount, = struct.unpack(dataFormat, data[dataOffset:arrayOffset])
#     arrayLimit = arrayOffset + (itemCount * itemLength)
#     return struct.unpack(f"{itemCount}{dataFormat}", data[arrayOffset:arrayLimit])

def test():
    ch = charFromSurrogates(0xD850, 0xDEEE)
    high, low = surrogatesFromChar(ch)
    print(f"ch = {ch:04X}, high = {high:04X}, low = {low:04X}")

if __name__ == "__main__":
    test()