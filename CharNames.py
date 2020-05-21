"""\
Based on uchar.cpp from ICU

Created on May 15, 2020

@author Eric Mader
"""

import struct
from ICUDataFile import ICUData, dataHeaderFormat, dataHeaderLength
from CharProps import getGeneralCategory
from GeneralCategories import GC_SURROGATE, GC_CATEFORY_COUNT

# "extra" general categories
GC_NONCHARACTER_CODEPOINT = GC_CATEFORY_COUNT
GC_LEAD_SURROGATE = GC_CATEFORY_COUNT + 1
GC_TRAIL_SURROGATE = GC_CATEFORY_COUNT + 2

charCatNames = [
    "unassigned",
    "uppercase letter",
    "lowercase letter",
    "titlecase letter",
    "modifier letter",
    "other letter",
    "non spacing mark",
    "enclosing mark",
    "combining spacing mark",
    "decimal digit number",
    "letter number",
    "other number",
    "space separator",
    "line separator",
    "paragraph separator",
    "control",
    "format",
    "private use area",
    "surrogate",
    "dash punctuation",
    "start punctuation",
    "end punctuation",
    "connector punctuation",
    "other punctuation",
    "math symbol",
    "currency symbol",
    "modifier symbol",
    "other symbol",
    "initial punctuation",
    "final punctuation",
    "noncharacter",
    "lead surrogate",
    "trail surrogate"
]

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

class Tokens(object):
    _tokens = []
    _strings = []

    @classmethod
    def populateData(cls, icuData, tokensStart, tokenStringsStart, tokenStringsLimit):
        if len(cls._tokens) == 0:
            (tokenCount, ) = struct.unpack("H", icuData.getData(tokensStart, tokensStart + 2))
            tokensData = icuData.getData(tokensStart + 2, tokenStringsStart)
            cls._tokens = struct.unpack(f"{tokenCount}H", tokensData)

            cls._strings = icuData.getData(tokenStringsStart, tokenStringsLimit)

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
    def expandGroupLengths(self, icuData,  groupStringsOffset):
        i = 0
        s = groupStringsOffset
        offset = 0
        length = 0
        offsets = []
        lengths = []

        while i < LINES_PER_GROUP:
            (lengthByte, ) = icuData.getData(s, s + 1)
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

    def __init__(self, icuData, groupStart, groupStringsStart):
        groupLimit = groupStart + self._groupLength
        (self.msb, offsetHigh, offsetLow) = struct.unpack(self._groupFormat, icuData.getData(groupStart, groupLimit))
        offset = (offsetHigh << 16) | offsetLow
        startChar = self.msb << GROUP_SHIFT
        limitChar = startChar + LINES_PER_GROUP
        self.charRange = range(startChar, limitChar)
        self.nameChoice = U_UNICODE_CHAR_NAME

        self.strings = []
        (dataOffset, offsets, lengths) = self.expandGroupLengths(icuData, groupStringsStart + offset)
        for i in range(len(offsets)):
            stringStart = dataOffset + offsets[i]
            stringLimit = stringStart + lengths[i]

            self.strings.append(icuData.getData(stringStart, stringLimit))

    def expandName(self, lineNumber, nameChoice):
        string = self.strings[lineNumber]

        if nameChoice != U_UNICODE_CHAR_NAME and nameChoice != U_EXTENDED_CHAR_NAME:
            fieldIndex = 2 if nameChoice == U_ISO_COMMENT else nameChoice
            fields = string.split(b';')
            string = fields[fieldIndex] if fieldIndex < len(fields) else b''

        return Tokens.expandString(string, nameChoice)

    def __iter__(self):
        for code in self.charRange:
            yield (code, self.expandName(code & GROUP_MASK, self.nameChoice))

class AlgorithmicRange(object):
    def __init__(self, icuData, offset):
        self.nameChoice = U_UNICODE_CHAR_NAME
        rangeStart = offset
        rangeLimit = rangeStart + _rangeLength
        (start, end, self.type, self.variant, self.size) = struct.unpack(_rangeFormat, icuData.getData(rangeStart, rangeLimit))

        self.charRange = range(start, end + 1)
        if self.type == 0:
            self.string = icuData.getString(rangeLimit)
            self.factors = None
            self.elements = None
        elif self.type == 1:
            factorCount = self.variant
            factorsFormat = f"{factorCount}H"
            factorsLength = struct.calcsize(factorsFormat)
            factorsStart = rangeLimit
            factorsLimit = factorsStart + factorsLength
            factorsData = icuData.getData(factorsStart, factorsLimit)
            self.factors = struct.unpack(factorsFormat, factorsData)
            self.string = icuData.getString(factorsLimit)
            elementsData = icuData.getData(factorsLimit + len(self.string) + 1, offset + self.size)

            self.elements = []
            elementStart = factorsLimit + len(self.string) + 1  # + 1 for null byte

            while elementStart < offset + self.size:
                element = icuData.getString(elementStart)
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

    def __iter__(self):
        for code in self.charRange:
            yield (code, self.getName(code, self.nameChoice))

class CharNames(object):
    _icuData = ICUData()
    _groups = []
    _algorithmicRanges = []

    @classmethod
    def populateData(cls):

        dataOffset = cls._icuData.getDataOffset("unames.icu")
        dataHeaderData = cls._icuData.getData(dataOffset, dataOffset + dataHeaderLength)

        (headerLength, magic1, magic2, infoSize, _, isBigEndian, charsetFamily, sizeofUChar, _, \
         dataFormat, fvMajor, fvMinor, fvMilli, fvMicro, dvMajor, dvMinor, dvMilli, dvMicro) = \
            struct.unpack(dataHeaderFormat, dataHeaderData[:dataHeaderLength])

        baseOffset = dataOffset + headerLength
        namesDataHeaderStart = baseOffset
        namesDataHeaderLimit = namesDataHeaderStart + _nameDataHeaderLength
        namesDataHeaderData = cls._icuData.getData(namesDataHeaderStart, namesDataHeaderLimit)
        (tokenStringOffset, groupsOffset, groupStringOffset, algNamesOffset) = \
            struct.unpack(_nameDataHeaderFormat,  namesDataHeaderData[:_nameDataHeaderLength])

        tokensStart = namesDataHeaderLimit
        tokenStringsStart = tokenStringOffset + baseOffset
        tokenStringsLimit = groupsOffset + baseOffset

        Tokens.populateData(cls._icuData, tokensStart, tokenStringsStart, tokenStringsLimit)

        groupsStart = groupsOffset + baseOffset
        (groupsLimit,) = struct.unpack("H", cls._icuData.getData(groupsStart, groupsStart + 2))

        groupStringsStart = groupStringOffset + baseOffset

        groupStart = groupsStart + 2

        for _ in range(groupsLimit):
            group = Group(cls._icuData, groupStart, groupStringsStart)
            cls._groups.append(group)
            groupStart += Group._groupLength

        rangeStart = algNamesOffset + baseOffset
        (algorithmicRangeCount,) = struct.unpack("I", cls._icuData.getData(rangeStart, rangeStart + 4))

        rangeStart += 4
        rangeLimit = rangeStart + _rangeLength
        for _ in range(algorithmicRangeCount):
            algRange = AlgorithmicRange(cls._icuData, rangeStart)
            cls._algorithmicRanges.append(algRange)
            rangeStart += algRange.size

    @classmethod
    def getGroup(cls, code):
        groupMSB = code >> GROUP_SHIFT
        start = 0
        limit = len(cls._groups)

        while start < limit - 1:
            midpoint = (start + limit) // 2
            if groupMSB < cls._groups[midpoint].msb:
                limit = midpoint
            else:
                start = midpoint

        return cls._groups[start] if cls._groups[start].msb == groupMSB else None

    @classmethod
    def isUnicodeNoncharacter(cls, code):
        return code >= 0xfdd0 and \
         (code <= 0xfdef or (code & 0xfffe) == 0xfffe) and code <= 0x10ffff

    @classmethod
    def isLead(cls, code):
        return (code & 0xfffffc00) == 0xd800

    @classmethod
    def getCharCat(cls, code):
        if cls.isUnicodeNoncharacter(code):
            return GC_NONCHARACTER_CODEPOINT

        cat = getGeneralCategory(code)
        if cat == GC_SURROGATE:
            return GC_LEAD_SURROGATE if cls.isLead(code) else GC_TRAIL_SURROGATE

        return cat

    @classmethod
    def getCharCatName(cls, code):
        cat = cls.getCharCat(code)

        return "unknown" if cat >= len(charCatNames) else charCatNames[cat]

    @classmethod
    def _getName(cls, code, nameChoice):
        group = cls.getGroup(code)

        if group is not None:
            return group.expandName(code & GROUP_MASK, nameChoice)

        return ""

    @classmethod
    def getCharName(cls, code, nameChoice=U_UNICODE_CHAR_NAME):
        for algorithmicRange in cls._algorithmicRanges:
            if algorithmicRange.charInRange(code):
                return algorithmicRange.getName(code, nameChoice)

        if nameChoice == U_EXTENDED_CHAR_NAME:
            return f"<{cls.getCharCatName(code)}-{code:04X}>"

        return CharNames._getName(code, nameChoice)

    def __init__(self, nameChoice=U_UNICODE_CHAR_NAME):
        self.nameChoice = nameChoice

    def __iter__(self):
        charLimit = max(self._groups[-1].charRange.stop, self._algorithmicRanges[-1].charRange.stop)
        char = 0
        algRange = 0
        while char < charLimit:
            group = self.getGroup(char)
            if group is not None and char in group.charRange:
                group.nameChoice = self.nameChoice
                for (code, name) in group:
                    if name: yield (code, name)
                char = group.charRange.stop
            elif algRange < len(self._algorithmicRanges) and self._algorithmicRanges[algRange].charInRange(char):
                algorithmicRange = self._algorithmicRanges[algRange]
                algorithmicRange.nameChoice = self.nameChoice
                for (code, name) in algorithmicRange:
                    if name: yield (code, name)
                char = algorithmicRange.charRange.stop
                algRange += 1
            else:
                char += LINES_PER_GROUP

    def charFromName(self, theName):
        for (code, name) in self:
            if name == theName:
                return code

        return 0xFFFFFFFF

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
    print()

    print(f"getCharName('{chr(0x01A2)}') = {CharNames.getCharName(0x01A2)}")
    print(f"getCharName('{chr(0x01A2)}', U_CHAR_NAME_ALIAS) = {CharNames.getCharName(0x01A2, U_CHAR_NAME_ALIAS)}")
    print(f"getCharName('{chr(0x01A3)}') = {CharNames.getCharName(0x01A3)}")
    print(f"getCharName('{chr(0x01A3)}', U_CHAR_NAME_ALIAS) = {CharNames.getCharName(0x01A3, U_CHAR_NAME_ALIAS)}")
    print(f"getCharName('[', U_EXTENDED_CHAR_NAME) = {CharNames.getCharName(ord('['), U_EXTENDED_CHAR_NAME)}")
    print(f"getCharName(']', U_EXTENDED_CHAR_NAME) = {CharNames.getCharName(ord(']'), U_EXTENDED_CHAR_NAME)}")

    print(f"getCharName('{chr(0x00AF)}', U_EXTENDED_CHAR_NAME) = {CharNames.getCharName(0x00AF, U_EXTENDED_CHAR_NAME)}")

    print(f"getCharName('K', U_EXTENDED_CHAR_NAME) = {CharNames.getCharName(ord('K'), U_EXTENDED_CHAR_NAME)}")
    print(f"getCharName('k', U_EXTENDED_CHAR_NAME) = {CharNames.getCharName(ord('k'), U_EXTENDED_CHAR_NAME)}")
    print()

    print(f'charFromName("DEVANAGARA LETTER KA") is {chr(CharNames().charFromName("DEVANAGARI LETTER KA"))}')
    print(f'charFromName("HANGUL SYLLABLE GIM") is {chr(CharNames().charFromName("HANGUL SYLLABLE GIM"))}')
    print(f'charFromName("HANGUL SYLLABLE CI") is {chr(CharNames().charFromName("HANGUL SYLLABLE CI"))}')
    print(f'charFromName("CJK UNIFIED IDEOGRAPH-6F22") is {chr(CharNames().charFromName("CJK UNIFIED IDEOGRAPH-6F22"))}')
    print()

    allNames = []
    for (code, name) in CharNames(U_CHAR_NAME_ALIAS):
        allNames.append(name)
        print(f'U+{code:04X}: "{name}"')
    print()

if __name__ == "__main__":
    test()
