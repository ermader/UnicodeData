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

def isLead(code):
    return (code & 0xfffffc00) == 0xd800

def charFromSurrogates(high, low):
    return ((high - 0xD800) << 10) + (low - 0xDC00) + 0x10000

def surrogatesFromChar(ch):
    base = ch - 0x10000
    high = (base >> 10) + 0xD800
    low = (base & 0x03FF) + 0xDC00
    return high, low

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