"""\
Access to ICU data file. Based on ICU

Created on May 12, 2020

@author Eric Mader
"""

import struct

_dataFileName = "icudt67l"  # Needs to change if we change the data file...
_dataFilePath = f"Data/{_dataFileName}.dat"
_namePrefix = f"{_dataFileName}/"
_namePrefixLen = len(_namePrefix)

dataHeaderFormat = "HBBHHBBBB4s4B4B"  # MappedData + UDataInfo
dataHeaderLength = struct.calcsize(dataHeaderFormat)

_tocEntryFormat = "II"
_tocEntryLength = struct.calcsize(_tocEntryFormat)

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
    def _populateData(cls):
        if cls._fileData is not None:
            return

        dataFile = open(_dataFilePath, "rb")
        cls._fileData = dataFile.read()

        (headerLength, magic1, magic2, infoSize, _, isBigEndian, charsetFamily, sizeofUChar, _, \
         dataFormat, fvMajor, fvMinor, fvMilli, fvMicro, dvMajor, dvMinor, dvMilli, dvMicro) =\
            struct.unpack(dataHeaderFormat, cls._fileData[:dataHeaderLength])

        # this would be a good place to verify (some of) the magic bytes, the data format,
        # the isBigEndian, charsetFamily and sizeofUChar...

        tocOffset = headerLength
        (tocCount, ) = struct.unpack("I", cls._fileData[tocOffset:tocOffset + 4])

        tocEntryStart = tocOffset + 4
        tocEntryLimit = tocEntryStart + _tocEntryLength

        for _ in range(tocCount):
            (nameOffset, dataOffset) = struct.unpack(_tocEntryFormat, cls._fileData[tocEntryStart:tocEntryLimit])
            name = ICUData.getName(nameOffset + headerLength)
            cls._dataOffsets[name] = dataOffset + headerLength
            tocEntryStart = tocEntryLimit
            tocEntryLimit += _tocEntryLength

    def __init__(self):
        ICUData._populateData()

# dataFilePath = "/usr/share/icu/icudt64l.dat"  # Eventually, keep a copy in our Data directory...
#
# dataHeaderFormat = "HBBHHBBBB4s4B4B"  # MappedData + UDataInfo
# dataHeaderLength = struct.calcsize(dataHeaderFormat)
#
# tocEntryFormat = "II"
# tocEntryLength = struct.calcsize(tocEntryFormat)
#
# dataFile = open(dataFilePath, "rb")
#
# dataHeader = dataFile.read(dataHeaderLength)
#
# (headerLength, magic1, magic2, infoSize, infoReserved, isBigEndian, charsetFamily, sizeofUChar, reservedByte, \
#  dataFormat, fvMajor, fvMinor, fvMilli, fvMicro, dvMajor, dvMinor, dvMilli, dvMicro) =\
#     struct.unpack(dataHeaderFormat, dataHeader)
#
# tocOffset = headerLength
#
# dataFile.seek(tocOffset)
# tocHeader = dataFile.read(4)
# (tocCount, ) = struct.unpack("I", tocHeader)
# tocLength = tocCount * tocEntryLength
# tocEntriesData = dataFile.read(tocLength)
#
# tocEntries = []
#
# tocEntryStart = 0
# tocEntryLimit = tocEntryLength
# minNameOffset = 0xFFFFFFFF
# maxDataOffset = 0
# for _ in range(tocCount):
#     (nameOffset, dataOffset) = struct.unpack(tocEntryFormat, tocEntriesData[tocEntryStart:tocEntryLimit])
#     tocEntries.append((nameOffset, dataOffset))
#     if nameOffset < minNameOffset:
#         minNameOffset = nameOffset
#     if dataOffset > maxDataOffset:
#         maxDataOffset = dataOffset
#     tocEntryStart = tocEntryLimit
#     tocEntryLimit += tocEntryLength
#
# (nameOffset0, dataOffset0) = tocEntries[0]
# (nameOffset1, dataOffset1) = tocEntries[1]
# (nameOffsetH, dataOffsetH) = tocEntries[tocCount // 2]
# (nameOffsetH1, dataOffsetH1) = tocEntries[tocCount // 2 + 1]
# (nameOffsetX, dataOffsetX) = tocEntries[tocCount - 2]
# (nameOffsetL, dataOffsetL) = tocEntries[tocCount - 1]
#
# namesDataLength = dataOffset0 - nameOffset0  # this is a bit too long...
# dataFile.seek(nameOffset0 + headerLength)
# namesData = dataFile.read(namesDataLength)
#
# names = []
#
# # This assumes that all names start with the prefix...
# for (nameOffset, _) in tocEntries:
#     name = ""
#     while namesData[nameOffset - nameOffset0] != 0:
#         name += chr(namesData[nameOffset - nameOffset0])
#         nameOffset += 1
#     names.append(name[_namePrefixLen:])
#
# for name in names:
#     if name.endswith(".icu"):
#         print(f'Found "{name}"')
#
# print(f'Last name: "{names[-1]}"')

def test():
    id = ICUData()

    for name in id._dataOffsets.keys():
        if name.endswith(".icu"):
            print(f'Found "{name}"')

    print(f'Last name: "{name}"')

    layoutOffset = id.getDataOffset("unames.icu")
    layoutHeader = id.getData(layoutOffset, layoutOffset + dataHeaderLength)
    (headerLength, magic1, magic2, infoSize, _, isBigEndian, charsetFamily, sizeofUChar, _, \
     dataFormat, fvMajor, fvMinor, fvMilli, fvMicro, dvMajor, dvMinor, dvMilli, dvMicro) = \
        struct.unpack(dataHeaderFormat, layoutHeader[:dataHeaderLength])
    pass

if __name__ == "__main__":
    test()







