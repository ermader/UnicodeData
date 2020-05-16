"""\
Based on uchar.cpp from ICU

Created on May 15, 2020

@author Eric Mader
"""

import struct
from ICUDataFile import ICUData, dataHeaderFormat, dataHeaderLength

# Character name choices
U_UNICODE_CHAR_NAME = 0  # Unicode character name (Name property).

# The Unicode_1_Name property value which is of little practical value.
# Beginning with ICU 49, ICU APIs return an empty string for this name choice.
U_UNICODE_10_CHAR_NAME = 1

U_EXTENDED_CHAR_NAME = 2  # Standard or synthetic character name.
U_CHAR_NAME_ALIAS = 3  # Corrected name from NameAliases.txt.
U_CHAR_NAME_CHOICE_COUNT = 4

U_ISO_COMMENT = U_CHAR_NAME_CHOICE_COUNT

GROUP_SHIFT = 5
LINES_PER_GROUP = 1 << GROUP_SHIFT
GROUP_MASK = LINES_PER_GROUP - 1

GROUP_MSB = 0
GROUP_OFFSET_HIGH = 1
GROUP_OFFSET_LOW = 2
GROUP_LENGTH = 3

CP_SEMICOLON = ord(';')

_nameDataHeaderFormat = "IIII"
_nameDataHeaderLength = struct.calcsize(_nameDataHeaderFormat)


id = ICUData()

dataOffset = id.getDataOffset("unames.icu")
dataHeaderData = id.getData(dataOffset, dataOffset + dataHeaderLength)

(headerLength, magic1, magic2, infoSize, _, isBigEndian, charsetFamily, sizeofUChar, _, \
 dataFormat, fvMajor, fvMinor, fvMilli, fvMicro, dvMajor, dvMinor, dvMilli, dvMicro) = \
    struct.unpack(dataHeaderFormat, dataHeaderData[:dataHeaderLength])

baseOffset = dataOffset + headerLength
namesDataHeaderStart = baseOffset
namesDataHeaderLimit = namesDataHeaderStart + _nameDataHeaderLength
namesDataHeaderData = id.getData(namesDataHeaderStart, namesDataHeaderLimit)
(tokenStringOffset, groupsOffset, groupStringOffset, algNamesOffset) = struct.unpack(_nameDataHeaderFormat, namesDataHeaderData[:_nameDataHeaderLength])

tokensStart = namesDataHeaderLimit
tokensLimit = tokenStringOffset + baseOffset
tokensFormat = f"{(tokensLimit - tokensStart) // 2}H"
tokensData = id.getData(tokensStart, tokensLimit)
tokens = struct.unpack(tokensFormat, tokensData)
tokenCount = tokens[0]
tokens = tokens[1:]

tokenStringsStart = tokenStringOffset + baseOffset
tokenStringsLimit = groupsOffset + baseOffset
tokenStringsData = id.getData(tokenStringsStart, tokenStringsLimit)

groupsStart = groupsOffset + baseOffset
groupsLimit = groupStringOffset + baseOffset
groupsFormat = f"{(groupsLimit - groupsStart) // 2}H"
groupsData = id.getData(groupsStart, groupsLimit)
groups = struct.unpack(groupsFormat, groupsData[:struct.calcsize(groupsFormat)])
groupsLimit = groups[0]
groups = groups[1:]

groupStringsStart = groupStringOffset + baseOffset
groupStringsLimit = algNamesOffset + baseOffset
groupStringsData = id.getData(groupStringsStart, groupStringsLimit)

pass

def getGroup(code):
    groupMSB = code >> GROUP_SHIFT
    start = 0
    limit = groupsLimit

    while start < limit - 1:
        midPoint = (start + limit) // 2
        if groupMSB < groups[midPoint * GROUP_LENGTH + GROUP_MSB]:
            limit = midPoint
        else:
            start = midPoint

    return groups[start * GROUP_LENGTH:(start+1) * GROUP_LENGTH]

def getGroupOffset(group):
    return (group[GROUP_OFFSET_HIGH] << 16) | group[GROUP_OFFSET_LOW]

# expandGroupLengths() reads a block of compressed lengths of 32 strings and
# expands them into offsets and lengths for each string.
# Lengths are stored with a variable-width encoding in consecutive nibbles:
# If a nibble < 0xc, then it is the length itself (0=empty string).
# If a nibble >= 0xc, then it forms a length value with the following nibble.
# Calculation see below.
# The offsets and lengths arrays must be at least 33 (one more) long because
# there is no check here at the end if the last nibble is still used.
def expandGroupLengths(s):
    i = 0
    offset = 0
    length = 0
    offsets = []
    lengths = []

    while i < LINES_PER_GROUP:
        lengthByte = groupStringsData[s]
        s += 1

        # read even nibble - MSBs of lengthByte
        if length >= 12:
            length = ((length & 0x3) << 4) | ((lengthByte >> 4) + 12)
            lengthByte &= 0xF
        elif lengthByte >= 0xC0:
            length = (lengthByte & 0x3F) + 12
        else:
            length = lengthByte >> 4
            lengthByte &= 0xF

        offsets.append(offset)
        lengths.append(length)
        offset += length
        i += 1

        # read odd nibble - LSBs of lengthByte
        if (lengthByte & 0xF0) == 0:
            # this nibble was not consumed for a double-nibble length above
            length = lengthByte

            if length < 12:
                # single-nibble length in LSBs
                offsets.append(offset)
                lengths.append(length)
                offset += length
                i += 1
            else:
                length = 0  # prevent double-nibble detection in the next iteration

    return (s, offsets, lengths)

def expandName(s, nameLength, nameChoice):
    expandedName = ""

    if nameChoice != U_UNICODE_CHAR_NAME and nameChoice != U_EXTENDED_CHAR_NAME:
        if CP_SEMICOLON >= tokenCount or tokens[CP_SEMICOLON] == 0xFFFF:
            fieldIndex = 2 if nameChoice == U_ISO_COMMENT else nameChoice

            while True:
                while nameLength > 0:
                    nameLength -= 1
                    c = groupStringsData[s]
                    s += 1
                    if c == CP_SEMICOLON:
                        break

                fieldIndex -= 1
                if fieldIndex <= 0:
                    break
            else:
                nameLength = 0

    while nameLength > 0:
        c = groupStringsData[s]
        s += 1
        nameLength -= 1

        if c >= tokenCount:
            if c != CP_SEMICOLON:
                expandedName += chr(c)
            else:
                break

        else:
            token = tokens[c]
            if token == 0xFFFE:
                # this is a lead byte for a double-byte token
                token = tokens[c << 8 | groupStringsData[s]]
                s += 1
                nameLength -= 1

            if token == 0xFFFF:
                if c != CP_SEMICOLON:
                    expandedName += chr(c)
                else:
                    if len(expandedName) == 0 and nameChoice == U_EXTENDED_CHAR_NAME:
                        if CP_SEMICOLON >= tokenCount or tokens[CP_SEMICOLON] == 0xFFFF:
                            continue
                    break

            else:
                while tokenStringsData[token] != 0:
                    expandedName += chr(tokenStringsData[token])
                    token += 1

    return expandedName

def expandGroupName(group, lineNumber, nameChoice):
    s = getGroupOffset(group)
    (s, offsets, lengths) = expandGroupLengths(s)
    return expandName(s + offsets[lineNumber], lengths[lineNumber], nameChoice)

def getName(code, nameChoice):
    group = getGroup(code)

    if (code >> GROUP_SHIFT) == group[GROUP_MSB]:
        return expandGroupName(group, code & GROUP_MASK, nameChoice)

    return ""

print(f"getName('K') = {getName(ord('K'), U_UNICODE_CHAR_NAME)}")
print(f"getName('k') = {getName(ord('k'), U_UNICODE_CHAR_NAME)}")

print(f"getName(0x0901) = {getName(0x0901, U_UNICODE_CHAR_NAME)}")
print(f"getName(0x0915) = {getName(0x0915, U_UNICODE_CHAR_NAME)}")

# print(getName(ord('漢'), U_UNICODE_CHAR_NAME))