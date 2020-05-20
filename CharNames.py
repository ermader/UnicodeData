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

_rangeFormat = "IIBBH"
_rangeLength = struct.calcsize(_rangeFormat)

id = ICUData()

class Tokens(object):
    _tokens = []
    _strings = []

    @classmethod
    def populateData(cls, tokensStart, tokenStringsStart, tokenStringsLimit):
        if len(cls._tokens) == 0:
            (tokenCount, ) = struct.unpack("H", id.getData(tokensStart, tokensStart + 2))
            tokensData = id.getData(tokensStart + 2, tokenStringsStart)
            cls._tokens = struct.unpack(f"{tokenCount}H", tokensData)

            cls._strings = id.getData(tokenStringsStart, tokenStringsLimit)

    @classmethod
    def expandString(cls, string, nameChoice):
        expandedName = ""

        nameLength = len(string)

        s = 0
        while nameLength > 0:
            c = string[s]
            s += 1
            nameLength -= 1

            if c >= len(cls._tokens):
                if c != CP_SEMICOLON:
                    expandedName += chr(c)
                else:
                    break
            else:
                token = cls._tokens[c]
                if token == 0xFFFE:
                    # this is a lead byte for a double-byte token
                    token = cls._tokens[c << 8 | string[s]]
                    s += 1
                    nameLength -= 1

                if token == 0xFFFF:
                    if c != CP_SEMICOLON:
                        expandedName += chr(c)
                    else:
                        if len(expandedName) == 0 and nameChoice == U_EXTENDED_CHAR_NAME:
                            if CP_SEMICOLON >= len(cls._tokens) or cls._tokens[CP_SEMICOLON] == 0xFFFF:
                                continue
                        break
                else:
                    while cls._strings[token] != 0:
                        expandedName += chr(cls._strings[token])
                        token += 1

        return expandedName

    def __init__(self, tokensStart, tokenStringsStart, tokenStringsLimit):
        Tokens.populateData(tokensStart, tokenStringsStart, tokenStringsLimit)



class Group(object):
    _groupFormat = "HHH"
    _groupLength = struct.calcsize(_groupFormat)

    # expandGroupLengths() reads a block of compressed lengths of 32 strings and
    # expands them into offsets and lengths for each string.
    # Lengths are stored with a variable-width encoding in consecutive nibbles:
    # If a nibble < 0xc, then it is the length itself (0=empty string).
    # If a nibble >= 0xc, then it forms a length value with the following nibble.
    # Calculation see below.
    # The offsets and lengths arrays must be at least 33 (one more) long because
    # there is no check here at the end if the last nibble is still used.
    def expandGroupLengths(self,  groupStringsOffset):
        i = 0
        s = groupStringsOffset
        offset = 0
        length = 0
        offsets = []
        lengths = []

        while i < LINES_PER_GROUP:
            (lengthByte, ) = id.getData(s, s + 1)
            s += 1

            # read even nibble - MSBs of lengthByte
            if length >= 12:
                length = ((length & 0x3) << 4 | lengthByte >> 4) + 12
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

    def __init__(self, groupStart, groupStringsStart):
        groupLimit = groupStart + self._groupLength
        (self.msb, offsetHigh, offsetLow) = struct.unpack(self._groupFormat, id.getData(groupStart, groupLimit))
        offset = (offsetHigh << 16) | offsetLow

        self.strings = []
        (dataOffset, offsets, lengths) = self.expandGroupLengths(groupStringsStart + offset)
        for i in range(len(offsets)):
            stringStart = dataOffset + offsets[i]
            stringLimit = stringStart + lengths[i]

            self.strings.append(id.getData(stringStart, stringLimit))

    def expandName(self, lineNumber, nameChoice):
        if nameChoice != U_UNICODE_CHAR_NAME and nameChoice != U_EXTENDED_CHAR_NAME:
            pass  # Not sure semicolons actually appear in the data...

        return Tokens.expandString(self.strings[lineNumber], nameChoice)

class AlgorithmicRange(object):
    def __init__(self, offset):
        rangeStart = offset
        rangeLimit = rangeStart + _rangeLength
        (start, end, self.type, self.variant, self.size) = struct.unpack(_rangeFormat, id.getData(rangeStart, rangeLimit))

        self.charRange = range(start, end + 1)
        if self.type == 0:
            self.string = id.getString(rangeLimit)
            self.factors = None
            self.elements = None
        elif self.type == 1:
            factorCount = self.variant
            factorsFormat = f"{factorCount}H"
            factorsLength = struct.calcsize(factorsFormat)
            factorsStart = rangeLimit
            factorsLimit = factorsStart + factorsLength
            factorsData = id.getData(factorsStart, factorsLimit)
            self.factors = struct.unpack(factorsFormat, factorsData)
            self.string = id.getString(factorsLimit)
            elementsData = id.getData(factorsLimit + len(self.string) + 1, offset + self.size)

            self.elements = []
            elementStart = factorsLimit + len(self.string) + 1  # + 1 for null byte

            while elementStart < offset + self.size:
                element = id.getString(elementStart)
                self.elements.append(element)
                elementStart += len(element) + 1

        else:
            self.string = None
            self.factors = None
            self.elements = None

    def factorSuffix(self, char):
        indexes = []
        code = char - self.charRange.start
        suffix = self.string

        count = len(self.factors) - 1

        for i in range(count, 0, -1):
            factor = self.factors[i]
            indexes.insert(0, code % factor)
            code //= factor

        indexes.insert(0, code)

        elementIndex = 0
        for i in range(count + 1):
            elementIndex += indexes[i]
            suffix += self.elements[elementIndex]
            elementIndex += self.factors[i] - indexes[i]

        return suffix

    def getName(self, code, nameChoice):
        name = ""

        if nameChoice != U_UNICODE_CHAR_NAME and nameChoice != U_EXTENDED_CHAR_NAME:
            # Only the normative character name can be algorithmic.
            return ""

        if self.type == 0:
            name += self.string

            digits = self.variant
            if digits == 4:
                hex = f"{code:04X}"
            elif digits == 5:
                hex = f"{code:05X}"
            else:
                hex = f"{code:06X}"

            name += hex
        elif self.type == 1:
            name += self.factorSuffix(code)

        return name

    def charInRange(self, char):
        return char in self.charRange

    def charOffsetInRange(self, char):
        return char - self.charRange.start

class CharNames(object):
    _groups = {}
    _algorithmicRanges = []

    @classmethod
    def populateData(cls):
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
        (tokenStringOffset, groupsOffset, groupStringOffset, algNamesOffset) = \
            struct.unpack(_nameDataHeaderFormat,  namesDataHeaderData[:_nameDataHeaderLength])

        tokensStart = namesDataHeaderLimit
        tokenStringsStart = tokenStringOffset + baseOffset
        tokenStringsLimit = groupsOffset + baseOffset

        Tokens.populateData(tokensStart, tokenStringsStart, tokenStringsLimit)

        groupsStart = groupsOffset + baseOffset
        (groupsLimit,) = struct.unpack("H", id.getData(groupsStart, groupsStart + 2))

        groupStringsStart = groupStringOffset + baseOffset

        groupStart = groupsStart + 2

        for _ in range(groupsLimit):
            group = Group(groupStart, groupStringsStart)
            cls._groups[group.msb] = group
            groupStart += Group._groupLength

        rangeStart = algNamesOffset + baseOffset
        (algorithmicRangeCount,) = struct.unpack("I", id.getData(rangeStart, rangeStart + 4))

        rangeStart += 4
        rangeLimit = rangeStart + _rangeLength
        for _ in range(algorithmicRangeCount):
            algRange = AlgorithmicRange(rangeStart)
            cls._algorithmicRanges.append(algRange)
            rangeStart += algRange.size

    @classmethod
    def _getName(cls, code, nameChoice):
        groupMSB = code >> GROUP_SHIFT

        if groupMSB in cls._groups:
            return cls._groups[groupMSB].expandName(code & GROUP_MASK, nameChoice)

        return ""

    @classmethod
    def getCharName(cls, code, nameChoice=U_UNICODE_CHAR_NAME):
        for algorithmicRange in cls._algorithmicRanges:
            if algorithmicRange.charInRange(code):
                return algorithmicRange.getName(code, nameChoice)

        if nameChoice == U_EXTENDED_CHAR_NAME:
            return f"<algorithmic name-{code:04X}>"

        return CharNames._getName(code, nameChoice)

CharNames.populateData()

def test():
    print(f"getCharName('{chr(0x00AF)}') = {CharNames.getCharName(0x00AF)}")

    print(f"getCharName('K') = {CharNames.getCharName(ord('K'))}")
    print(f"getCharName('k') = {CharNames.getCharName(ord('k'))}")

    print(f"getCharName('{chr(0x0901)}') = {CharNames.getCharName(0x0901)}")
    print(f"getCharName('क') = {CharNames.getCharName(ord('क'))}")

    print(f"getCharName('{chr(0x33E0)}') = {CharNames.getCharName(0x33E0)}")
    print(f"getCharName('{chr(0x33F0)}') = {CharNames.getCharName(0x33F0)}")

    print(f"getCharName('漢') = {CharNames.getCharName(ord('漢'))}")
    print(f"getCharName('{chr(0xD55C)}') = {CharNames.getCharName(0xD55C)}")
    print(f"getCharName('{chr(0xAD84)}') = {CharNames.getCharName(0xAD84)}")
    print(f"getCharName('{chr(0xC5B4)}') = {CharNames.getCharName(0xC5B4)}")
    print(f"getCharName('{chr(0xCA8D)}') = {CharNames.getCharName(0xCA8D)}")

    print(f"getCharName(0x17020) = {CharNames.getCharName(0x17020)}")

if __name__ == "__main__":
    test()
