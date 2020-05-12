"""\
Access to ICU data file. Based on ICU

Created on May 12, 2020

@author Eric Mader
"""

import struct

dataFilePath = "/usr/share/icu/icudt64l.dat"  # Eventually, keep a copy in our Data directory...

dataHeaderFormat = "HBBHHBBBB4s4B4B"
dataHeaderLength = struct.calcsize(dataHeaderFormat)

tocEntryFormat = "II"
tocEntryLength = struct.calcsize(tocEntryFormat)

dataFile = open(dataFilePath, "rb")

dataHeader = dataFile.read(dataHeaderLength)

(headerLength, magic1, magic2, infoSize, infoReserved, isBigEndian, charsetFamily, sizeofUChar, reservedByte, \
 dataFormat, fvMajor, fvMinor, fvMilli, fvMicro, dvMajor, dvMinor, dvMilli, dvMicro) =\
    struct.unpack(dataHeaderFormat, dataHeader)

tocOffset = headerLength

dataFile.seek(tocOffset)
tocHeader = dataFile.read(4)
(tocCount, ) = struct.unpack("I", tocHeader)
tocLength = tocCount * tocEntryLength
tocEntriesData = dataFile.read(tocLength)

tocEntries = []

tocEntryStart = 0
tocEntryLimit = tocEntryLength
for _ in range(tocCount):
    tocEntries.append(struct.unpack(tocEntryFormat, tocEntriesData[tocEntryStart:tocEntryLimit]))
    tocEntryStart = tocEntryLimit
    tocEntryLimit += tocEntryLength

(nameOffset0, dataOffset0) = tocEntries[0]
(nameOffset1, dataOffset1) = tocEntries[1]
(nameOffsetH, dataOffsetH) = tocEntries[tocCount // 2]
(nameOffsetH1, dataOffsetH1) = tocEntries[tocCount // 2 + 1]
(nameOffsetX, dataOffsetX) = tocEntries[tocCount - 2]
(nameOffsetL, dataOffsetL) = tocEntries[tocCount - 1]

namesDataLength = dataOffset0 - nameOffset0  # this is a bit too long...
dataFile.seek(nameOffset0 + headerLength)
namesData = dataFile.read(namesDataLength)

names = []
for (nameOffset, _) in tocEntries:
    name = ""
    while namesData[nameOffset - nameOffset0] != 0:
        name += chr(namesData[nameOffset - nameOffset0])
        nameOffset += 1
    names.append(name)

for name in names:
    if name.find("ulayout") >= 0:
        print(f'Found "{name}"')







