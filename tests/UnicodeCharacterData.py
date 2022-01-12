'''
Created on Apr 13, 2020

@author: emader
'''

import tempfile
import zipfile
from urllib.request import urlopen
import xml.etree.ElementTree as ElementTree
from timeit import default_timer as timer
#import shelve

from UnicodeData.UnicodeVersion import unicodeVersion
from UnicodeData.CharacterData import CharacterData
from UnicodeData.UnicodeSet import UnicodeSet

# _characterData = {}

# def stringFromRanges(ranges):
#     pieces = []

#     for range in ranges:
#         pieces.append(f"{range.start:04X}-{range.stop-1:04X}")

#     s = ", ".join(pieces)
#     return f"[{s}]"


def codePointsInSet(unicodeSet: UnicodeSet) -> list[int]:
    chars: list[int] = []
    len2 = len(unicodeSet.list) & ~1
    for i in range(0, len2, 2):
        start = unicodeSet.list[i]
        stop = unicodeSet.list[i+1]

        chars.extend([ch for ch in range(start, stop)])
    return chars


class PropertyList(object):
    def __init__(self):
        self.dict: dict[str, UnicodeSet] = {}

    def __getitem__(self, key: str):
        if key not in self.dict:
            self.dict[key] = UnicodeSet()

        return self.dict[key]

    def addCodePointForKey(self, key: str, codePoint: int):
        self[key].add(codePoint)

    def keys(self):
        return self.dict.keys()

    def values(self):
        return self.dict.values()

    def items(self):
        return self.dict.items()

class UnicodeCharacterData(object):

    characterData: dict[int, CharacterData] = {}

    @classmethod
    def _populateCharacterData(cls):
        if len(cls.characterData) > 0:
            return cls.characterData

        startTime = timer()
        download = urlopen(f"https://www.unicode.org/Public/{unicodeVersion}/ucdxml/ucd.all.grouped.zip")
        tf = tempfile.TemporaryFile()
        tf.write(download.read())
        tf.seek(0)
        zf = zipfile.ZipFile(tf)
        ucdFile = zf.open("ucd.all.grouped.xml")

        tree = ElementTree.parse(ucdFile)

        ucdFile.close()
        zf.close()
        download.close()

        root = tree.getroot()
        ucdNameSpace = root.tag[1:-4]  # remove initial "{" and final "}ucd"
        nameSpaces = {"ucd": ucdNameSpace}

        for group in root.findall("ucd:repertoire/ucd:group", nameSpaces):
            for char in group.findall("ucd:char", nameSpaces):
                if "cp" not in char.attrib:  # some entries are <char first-cp=xxxx last-cp=yyyy.../>
                    continue

                characterData = CharacterData(char, group)
                codePoint = characterData.codePoint
                cls.characterData[codePoint] = characterData

        endTime = timer()
        print(f"  Downloading, unzipping, reading {download.url} took {round(endTime - startTime, 2)} seconds.")

    def __init__(self):
        UnicodeCharacterData._populateCharacterData()


_scriptList = PropertyList()
_generalCategories = PropertyList()
_bidiClasses = PropertyList()
_bidiPairedBracketTypes = PropertyList()
_numericTypes = PropertyList()
_blockList = PropertyList()

_decompositions = {}


# when is it safe to close dataShelf?
def read():
    ucd = UnicodeCharacterData()

    for (_cp, characterData) in ucd.characterData.items():
        codePoint = characterData.codePoint
        generalCategory = characterData.generalCategory
        bidiProps = characterData.bidiProperties
        bidiClass = bidiProps.bidiClass
        bidiPairedBracketType = bidiProps.bidiPairedBracketType
        decompProps = characterData.decompProperties
        decomposition = decompProps.decomposition
        numericType = characterData.numericType
        script = characterData.script
        block = characterData.block


        _generalCategories[generalCategory].add(codePoint)
        _bidiClasses[bidiClass].add(codePoint)
        _bidiPairedBracketTypes[bidiPairedBracketType].add(codePoint)

        if decomposition is not None:
            _decompositions[codePoint] = decomposition

        if numericType != "None":
            _numericTypes[numericType].add(codePoint)

        _scriptList[script].add(codePoint)
        _blockList[block].add(codePoint)

    return ucd


# def main():
#     cd = read()
#
#     for (script, unicodeSet) in _scriptList.items():
#         ranges = unicodeSet.getRanges()
#         print(f"    '{script}': {stringFromRanges(ranges)}")
#     # print(_decompositions)
#
#     devaSet = _scriptList['Deva']
#     print(f"    devaSet.charAt(0x15) = {devaSet.charAt(0x15):04X}")
#     print(f"    devaSet.charAt(106) = {devaSet.charAt(106):04X}")
#     print(f"    devaSet.charAt(1000) = {devaSet.charAt(1000)}")
#     print(f"    devaSet.indexOf(0x0970) = {devaSet.indexOf(0x0970)}")
#     print(f"    devaSet.indexOf(0x0980) = {devaSet.indexOf(0x0980)}")
#
#
# if __name__ == "__main__":
#     main()
