"""\
Uitility routines, etc.

Created on May 28, 2020

@author Eric Mader
"""

# import struct
import typing

class _object(object):
    """Useful for passing object instances to sstruct.unpack()"""
    pass

def isUnicodeNoncharacter(code: int) -> bool:
    return code >= 0xfdd0 and \
     (code <= 0xfdef or (code & 0xfffe) == 0xfffe) and code <= 0x10ffff

_firstLead = 0xD800
_firstTrail = 0xDC00
_firstNonBMP = 0x10000
_leadShift = 10
_surrogateMask = 0xFFFFF800
_leadTrailMask = 0xFFFFFC00
_trailMask = 0xFFFFFFFF - _leadTrailMask
_surrogateOffset = (_firstLead << _leadShift) + _firstTrail - _firstNonBMP
_leadOffset = _firstLead - (_firstNonBMP >> _leadShift)

def isSurrogate(code: int) -> bool:
    return (code & _surrogateMask) == _firstLead

def isSurrogateLead(code: int) -> bool:
    return (code & 0x400) == 0

def isSurrogateTrail(code: int) -> bool:
    return (code & 0x400) != 0

def isLead(code: int) -> bool:
    return (code & _leadTrailMask) == _firstLead

def isTrail(code: int) -> bool:
    return (code & _leadTrailMask) == _firstTrail

def charFromSurrogates(lead: int, trail: int) -> int:
    return (lead << _leadShift) + trail - _surrogateOffset

def surrogatesFromChar(ch: int) -> tuple[int, int]:
    lead = (ch >> _leadShift) + _leadOffset
    trail = (ch & _trailMask) + _firstTrail
    return lead, trail

def arithmeticShift(value: int, bitsInWord: int, bitsInField: int) -> int:
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

def highBit(value: int) -> typing.Optional[int]:
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

def listOfCodes(codes: list[int]) -> str:
    codeList = [f"{code:04X}" for code in codes]
    return ", ".join(codeList)
