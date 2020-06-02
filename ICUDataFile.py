"""\
Access to ICU data file. Based on ICU

Created on May 12, 2020

@author Eric Mader
"""

import struct
from fontTools.misc import sstruct

_dataFileName = "icudt67l"  # Needs to change if we change the data file...
_dataFilePath = f"Data/{_dataFileName}.dat"
_namePrefix = f"{_dataFileName}/"
_namePrefixLen = len(_namePrefix)


dataHeaderFormat = """
# MappedData header
headerLength: H
magic1: B; magic2: B

# UDataInfo info
infoSize: H
reservedWord: H
isBigEndian: B
charsetFamily: B
sizeofUChar: B
reservedByte: B
dataFormat: 4s
fvMajor: B; fvMinor: B; fvMilli: B; fvMicro: B
dvMajor: B; dvMinor: B; dvMilli: B; dvMicro: B
"""
dataHeaderLength = sstruct.calcsize(dataHeaderFormat)

class _object(object):
    pass

_tocEntryFormat = "nameOffset: I; dataOffset: I"
_tocEntryLength = sstruct.calcsize(_tocEntryFormat)

class ICUData(object):
    _dataOffsets = {}
    _fileData = None

    @classmethod
    def getString(cls, offset):
        s = ""

        while cls._fileData[offset] != 0:
            s += chr(cls._fileData[offset])
            offset += 1

        return s

    @classmethod
    def getName(cls, offset):
        name = cls.getString(offset)  # Maybe check to be sure name starts with prefix?
        return name[_namePrefixLen:]

    @classmethod
    def getDataOffset(cls, name):
        return cls._dataOffsets[name]

    @classmethod
    def getData(cls, startOffset, limitOffset):
        return cls._fileData[startOffset:limitOffset]

    @classmethod
    def getDataOffsetAndHeader(cls, name):
        dataOffset = cls._dataOffsets[name]
        header = sstruct.unpack(dataHeaderFormat, cls._fileData[dataOffset:dataOffset + dataHeaderLength], _object())
        return (dataOffset, header)

    @classmethod
    def _populateData(cls):
        if cls._fileData is not None:
            return

        dataFile = open(_dataFilePath, "rb")
        cls._fileData = dataFile.read()

        header = sstruct.unpack(dataHeaderFormat, cls._fileData[:dataHeaderLength], _object())

        # this would be a good place to verify (some of) the magic bytes, the data format,
        # the isBigEndian, charsetFamily and sizeofUChar...

        tocOffset = header.headerLength
        (tocCount, ) = struct.unpack("I", cls._fileData[tocOffset:tocOffset + 4])

        tocEntryStart = tocOffset + 4
        tocEntryLimit = tocEntryStart + _tocEntryLength

        for _ in range(tocCount):
            tocEntry = sstruct.unpack(_tocEntryFormat, cls._fileData[tocEntryStart:tocEntryLimit], _object())
            name = ICUData.getName(tocEntry.nameOffset + header.headerLength)
            cls._dataOffsets[name] = tocEntry.dataOffset + header.headerLength
            tocEntryStart = tocEntryLimit
            tocEntryLimit += _tocEntryLength

    def __init__(self):
        ICUData._populateData()

def test():
    id = ICUData()

    for name in id._dataOffsets.keys():
        if name.endswith(".icu") or name.find("norm") >= 0 or name.find("nrm") >= 0:
            print(f'Found "{name}"')

    print(f'Last name: "{name}"')

    (layoutOffset, layoutHeaderData) = id.getDataOffsetAndHeader("unames.icu")
    pass

if __name__ == "__main__":
    test()







