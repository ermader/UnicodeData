"""\
Access to ICU data file. Based on ICU

Created on May 12, 2020

@author Eric Mader
"""

import typing

import struct
import pkg_resources
from fontTools.misc import sstruct  # type: ignore

# from .Utilities import _object

_dataFilePath = pkg_resources.resource_filename("UnicodeData", f"Data/icudata.dat")

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

class DataHeader:
    def __init__(self):
        self.headerLength = 0
        self.magic1 = 0
        self.magic2 = 0
        self.infoSize = 0
        self.reservedWord = 0
        self.isBigEndian = 0
        self.charsetFamily = 0
        self.sizeofUChar = 0
        self.reservedByte = 0
        self.dataFormat = 0
        self.fvMajor = 0
        self.fvMinor = 0
        self.fvMilli = 0
        self.fvMicro = 0
        self.dvMajor = 0
        self.dvMinor = 0
        self.dvMilli = 0
        self.dvMicro = 0
        
_tocEntryFormat = "nameOffset: I; dataOffset: I"
_tocEntryLength = sstruct.calcsize(_tocEntryFormat)

class TOCEntry:
    def __init__(self) -> None:
        self.nameOffset = 0
        self.dataOffset = 0

class ICUData(object):
    _dataOffsets: dict[str, int] = {}
    _fileData: bytes = b""

    @classmethod
    def getString(cls, offset: int):
        s = ""

        while cls._fileData[offset] != 0:
            s += chr(cls._fileData[offset])
            offset += 1

        return s

    @classmethod
    def getName(cls, offset: int):
        name = cls.getString(offset)  # Maybe check the prefix?
        prefixOffset = name.index("/")
        return name[prefixOffset+1:]

    @classmethod
    def getDataOffset(cls, name: str):
        return cls._dataOffsets[name]

    @classmethod
    def getData(cls, startOffset: int, limitOffset: int) -> bytes:
        return cls._fileData[startOffset:limitOffset]

    @classmethod
    def getDataOffsetAndHeader(cls, name: str) -> tuple[int, DataHeader]:
        dataOffset = cls._dataOffsets[name]
        dh = sstruct.unpack(dataHeaderFormat, cls._fileData[dataOffset:dataOffset + dataHeaderLength], DataHeader())
        header = typing.cast(DataHeader, dh)
        return (dataOffset, header)

    @classmethod
    def _populateData(cls):
        if cls._fileData:
            return

        dataFile = open(_dataFilePath, "rb")
        cls._fileData = dataFile.read()

        dh = sstruct.unpack(dataHeaderFormat, cls._fileData[:dataHeaderLength], DataHeader())
        header = typing.cast(DataHeader, dh)

        # this would be a good place to verify (some of) the magic bytes, the data format,
        # the isBigEndian, charsetFamily and sizeofUChar...

        tocOffset = header.headerLength
        (tocCount, ) = struct.unpack("I", cls._fileData[tocOffset:tocOffset + 4])

        tocEntryStart = tocOffset + 4
        tocEntryLimit = tocEntryStart + _tocEntryLength

        for _ in range(tocCount):
            te = sstruct.unpack(_tocEntryFormat, cls._fileData[tocEntryStart:tocEntryLimit], TOCEntry())
            tocEntry = typing.cast(TOCEntry, te)
            name = ICUData.getName(tocEntry.nameOffset + header.headerLength)
            cls._dataOffsets[name] = tocEntry.dataOffset + header.headerLength
            tocEntryStart = tocEntryLimit
            tocEntryLimit += _tocEntryLength

    def __init__(self):
        ICUData._populateData()

# def test():
#     id = ICUData()
#
#     for name in id._dataOffsets.keys():
#         if name.endswith(".icu") or name.endswith(".nrm"):
#             print(f'Found "{name}"')
#
#     print(f'Last name: "{name}"')
#
#     (layoutOffset, layoutHeaderData) = id.getDataOffsetAndHeader("unames.icu")
#     pass
#
# if __name__ == "__main__":
#     test()







