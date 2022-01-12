"""\
Based on uchar.cpp from ICU

Created on May 15, 2020

@author Eric Mader
"""

import typing

import struct
from fontTools.misc import sstruct  # type: ignore

from .ICUDataFile import ICUData
from .CharProps import getGeneralCategory
from .GeneralCategories import GC_SURROGATE, GC_CATEFORY_COUNT
from .Utilities import isLead, isUnicodeNoncharacter

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

class NameDataHeader(object):
    # __slots__ = ["tokenStringOffset", "groupsOffset", "groupStringOffset", "algNamesOffset"]

    def __init__(self) -> None:
        self.tokenStringOffset = 0
        self.groupsOffset = 0
        self.groupStringOffset = 0
        self.algNamesOffset = 0

_nameDataHeaderFormat = "tokenStringOffset: I; groupsOffset: I; groupStringOffset: I; algNamesOffset: I"
_nameDataHeaderLength = sstruct.calcsize(_nameDataHeaderFormat)

class AlgRange(object):
    # __slots__ = ["start", "end", "type", "variant", "size"]

    def __init__(self) -> None:
        self.start = 0
        self.end = 0
        self.type = 0
        self.variant = 0
        self.size = 0

_rangeFormat = "start: I; end: I; type: B; variant: B; size: H"
_rangeLength = sstruct.calcsize(_rangeFormat)

class Tokens(object):
    _tokens: typing.Sequence[int] = []
    _strings: typing.Sequence[int] = []

    @classmethod
    def populateData(cls, icuData: ICUData, tokensStart: int, tokenStringsStart: int, tokenStringsLimit: int):
        if len(cls._tokens) == 0:
            (tokenCount, ) = struct.unpack("H", icuData.getData(tokensStart, tokensStart + 2))
            tokensData = icuData.getData(tokensStart + 2, tokenStringsStart)
            cls._tokens = struct.unpack(f"{tokenCount}H", tokensData)

            cls._strings = icuData.getData(tokenStringsStart, tokenStringsLimit)

    @classmethod
    def expandString(cls, string: typing.Sequence[int], nameChoice: int):
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

    # def __init__(self, tokensStart: int, tokenStringsStart: int, tokenStringsLimit: int):
    #     Tokens.populateData(tokensStart, tokenStringsStart, tokenStringsLimit)



class Group(object):
    _groupFormat = "msb: H; offsetHigh: H; offsetLow: H"
    _groupLength = sstruct.calcsize(_groupFormat)

    class _GroupObject(object):
        # __slots__ = ["msb", "offsetHigh", "offsetLow"]

        def __init__(self) -> None:
            self.msb = 0
            self.offsetHigh = 0
            self.offsetLow = 0

    @classmethod
    def groupLength(cls) ->int:
        return cls._groupLength

    # expandGroupLengths() reads a block of compressed lengths of 32 strings and
    # expands them into offsets and lengths for each string.
    # Lengths are stored with a variable-width encoding in consecutive nibbles:
    # If a nibble < 0xc, then it is the length itself (0=empty string).
    # If a nibble >= 0xc, then it forms a length value with the following nibble.
    # Calculation see below.
    # The offsets and lengths arrays must be at least 33 (one more) long because
    # there is no check here at the end if the last nibble is still used.
    def expandGroupLengths(self, icuData: ICUData,  groupStringsOffset: int) -> tuple[int, list[int], list[int]]:
        i = 0
        s = groupStringsOffset
        offset = 0
        length = 0
        offsets: list[int] = []
        lengths: list[int] = []

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

    def __init__(self, icuData: ICUData, groupStart: int, groupStringsStart: int):
        groupLimit = groupStart + self._groupLength
        go = sstruct.unpack(self._groupFormat, icuData.getData(groupStart, groupLimit), self._GroupObject())
        group = typing.cast(type(self._GroupObject), go)
        self.msb = group.msb
        offset = (group.offsetHigh << 16) | group.offsetLow
        startChar = self.msb << GROUP_SHIFT
        limitChar = startChar + LINES_PER_GROUP
        self.charRange = range(startChar, limitChar)

        self.strings: list[bytes] = []
        (dataOffset, offsets, lengths) = self.expandGroupLengths(icuData, groupStringsStart + offset)
        for i in range(len(offsets)):
            stringStart = dataOffset + offsets[i]
            stringLimit = stringStart + lengths[i]

            self.strings.append(icuData.getData(stringStart, stringLimit))

    def expandName(self, lineNumber: int, nameChoice: int) -> str:
        string = self.strings[lineNumber]

        if nameChoice != U_UNICODE_CHAR_NAME and nameChoice != U_EXTENDED_CHAR_NAME:
            fieldIndex = 2 if nameChoice == U_ISO_COMMENT else nameChoice
            fields = string.split(b';')
            string = fields[fieldIndex] if fieldIndex < len(fields) else b''

        return Tokens.expandString(string, nameChoice)

    def nameIterator(self, nameChoice: int):
        for code in self.charRange:
            yield (code, self.expandName(code & GROUP_MASK, nameChoice))

class AlgorithmicRange(object):
    def __init__(self, icuData: ICUData, offset: int):
        rangeStart = offset
        rangeLimit = rangeStart + _rangeLength
        ar = sstruct.unpack(_rangeFormat, icuData.getData(rangeStart, rangeLimit), AlgRange())
        algRange = typing.cast(AlgRange, ar)
        self.type = algRange.type
        self.variant = algRange.variant
        self.size = algRange.size

        self.charRange = range(algRange.start, algRange.end + 1)
        if self.type == 0:
            self.string = icuData.getString(rangeLimit)
            # self.factors = None
            # self.elements = None
            self.factors: tuple[int, ...] = ()
            self.elements: list[str] = []
        elif self.type == 1:
            factorCount = self.variant
            factorsFormat = f"{factorCount}H"
            factorsLength = struct.calcsize(factorsFormat)
            factorsStart = rangeLimit
            factorsLimit = factorsStart + factorsLength
            factorsData = icuData.getData(factorsStart, factorsLimit)
            self.factors = struct.unpack(factorsFormat, factorsData)
            self.string = icuData.getString(factorsLimit)

            self.elements: list[str] = []
            elementStart = factorsLimit + len(self.string) + 1  # + 1 for null byte

            while elementStart < offset + self.size:
                element = icuData.getString(elementStart)
                self.elements.append(element)
                elementStart += len(element) + 1

        else:
            self.string = ""
            self.factors = ()
            self.elements = []

    def factorSuffix(self, char: int) -> str:
        indexes: list[int] = []
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

    def getName(self, code: int, nameChoice: int) -> str:
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

    def charInRange(self, char: int) -> bool:
        return char in self.charRange

    def charOffsetInRange(self, char: int) -> int:
        return char - self.charRange.start

    def nameIterator(self, nameChoice: int):
        for code in self.charRange:
            yield (code, self.getName(code, nameChoice))

class CharNames(object):
    _icuData = ICUData()
    _groups: list[Group] = []
    _algorithmicRanges: list[AlgorithmicRange] = []

    @classmethod
    def populateData(cls):

        (dataOffset, dataHeader) = cls._icuData.getDataOffsetAndHeader("unames.icu")

        baseOffset = dataOffset + dataHeader.headerLength
        namesDataHeaderStart = baseOffset
        namesDataHeaderLimit = namesDataHeaderStart + _nameDataHeaderLength
        namesDataHeaderData = cls._icuData.getData(namesDataHeaderStart, namesDataHeaderLimit)
        ndh = sstruct.unpack(_nameDataHeaderFormat, namesDataHeaderData[:_nameDataHeaderLength], NameDataHeader())
        nameDataHeader = typing.cast(NameDataHeader, ndh)

        tokensStart = namesDataHeaderLimit
        tokenStringsStart = nameDataHeader.tokenStringOffset + baseOffset
        tokenStringsLimit = nameDataHeader.groupsOffset + baseOffset

        Tokens.populateData(cls._icuData, tokensStart, tokenStringsStart, tokenStringsLimit)

        groupsStart = nameDataHeader.groupsOffset + baseOffset
        (groupsLimit,) = struct.unpack("H", cls._icuData.getData(groupsStart, groupsStart + 2))

        groupStringsStart = nameDataHeader.groupStringOffset + baseOffset

        groupStart = groupsStart + 2

        for _ in range(groupsLimit):
            group = Group(cls._icuData, groupStart, groupStringsStart)
            cls._groups.append(group)
            groupStart += Group.groupLength()

        rangeStart = nameDataHeader.algNamesOffset + baseOffset
        (algorithmicRangeCount,) = struct.unpack("I", cls._icuData.getData(rangeStart, rangeStart + 4))

        rangeStart += 4
        for _ in range(algorithmicRangeCount):
            algRange = AlgorithmicRange(cls._icuData, rangeStart)
            cls._algorithmicRanges.append(algRange)
            rangeStart += algRange.size

    @classmethod
    def getGroup(cls, code: int) -> typing.Optional[Group]:
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
    def getCharCat(cls, code: int) -> int:
        if isUnicodeNoncharacter(code):
            return GC_NONCHARACTER_CODEPOINT

        cat = getGeneralCategory(code)
        if cat == GC_SURROGATE:
            return GC_LEAD_SURROGATE if isLead(code) else GC_TRAIL_SURROGATE

        return cat

    @classmethod
    def getCharCatName(cls, code: int) -> str:
        cat = cls.getCharCat(code)

        return "unknown" if cat >= len(charCatNames) else charCatNames[cat]

    @classmethod
    def _getName(cls, code: int, nameChoice: int) -> str:
        group = cls.getGroup(code)

        if group is not None:
            return group.expandName(code & GROUP_MASK, nameChoice)

        return ""

    @classmethod
    def getCharName(cls, code: int, nameChoice:int=U_UNICODE_CHAR_NAME) -> str:
        for algorithmicRange in cls._algorithmicRanges:
            if algorithmicRange.charInRange(code):
                return algorithmicRange.getName(code, nameChoice)

        if nameChoice == U_EXTENDED_CHAR_NAME:
            return f"<{cls.getCharCatName(code)}-{code:04X}>"

        return CharNames._getName(code, nameChoice)

    @classmethod
    def nameIterator(cls, nameChoice: int =U_UNICODE_CHAR_NAME) -> typing.Iterator[tuple[int, str]]:
        charLimit = max(cls._groups[-1].charRange.stop, cls._algorithmicRanges[-1].charRange.stop)
        char = 0
        algRange = 0
        while char < charLimit:
            group = cls.getGroup(char)
            if group and char in group.charRange:
                # group.nameChoice = self.nameChoice
                for (code, name) in group.nameIterator(nameChoice):
                    if name: yield (code, name)
                char = group.charRange.stop
            elif algRange < len(cls._algorithmicRanges) and cls._algorithmicRanges[algRange].charInRange(char):
                algorithmicRange = cls._algorithmicRanges[algRange]
                # algorithmicRange.nameChoice = self.nameChoice
                for (code, name) in algorithmicRange.nameIterator(nameChoice):
                    if name: yield (code, name)
                char = algorithmicRange.charRange.stop
                algRange += 1
            else:
                char += LINES_PER_GROUP

    @classmethod
    def charFromName(cls, theName: str, nameChoice:int=U_UNICODE_CHAR_NAME) -> int:
        for (code, name) in cls.nameIterator(nameChoice):
            if name == theName:
                return code

        return 0xFFFFFFFF

CharNames.populateData()
