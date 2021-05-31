"""/
UCDReader. Read data from ICU's ppucd.txt file.

Created on May 26, 2021

@author Eric Mader
"""

import csv
from datetime import datetime
from pathlib import Path

class UCDReader(object):
    def __init__(self, icuDirectory, outDirectory):
        self.ucdVersion = None

        #
        # The default mapping from long name to ICU enum name
        # doesn't always work, usually because Unicode has renamed
        # them since the ICU enum name was made @stable. These mappings
        # capture those cases.
        #
        # (The "right" way to fix this is to capture the short names from the
        # comments when processing the enums and keep a mapping from short names
        # to ICU enum names.)
        #
        self.bcMapings = {
            "Arabic_Letter": "RIGHT_TO_LEFT_ARABIC",
            "Common_Separator": "COMMON_NUMBER_SEPARATOR",
            "European_Separator": "EUROPEAN_NUMBER_SEPARATOR",
            "European_Terminator": "EUROPEAN_NUMBER_TERMINATOR",
            "Nonspacing_Mark": "NON_SPACING_MARK",
            "White_Space": "WHITE_SPACE_NEUTRAL"
        }

        self.blkMappings = {
            "Combining_Diacritical_Marks_For_Symbols": "COMBINING_MARKS_FOR_SYMBOLS",
            "Greek_And_Coptic": "GREEK"
        }

        #
        # The long names that map to "" do not appear in the ICU enum.
        #
        self.gcMappings = {
            "Other": "",
            "Control": "CONTROL_CHAR",
            "Format": "FORMAT_CHAR",
            "Private_Use": "PRIVATE_USE_CHAR",
            "Letter": "",
            "Cased_Letter": "",
            "Mark": "",
            "Spacing_Mark": "COMBINING_SPACING_MARK",
            "Nonspacing_Mark": "NON_SPACING_MARK",
            "Number": "",
            "Decimal_Number": "DECIMAL_DIGIT_NUMBER",
            "Punctuation": "",
            "Close_Punctuation": "END_PUNCTUATION",
            "Open_Punctuation": "START_PUNCTUATION",
            "Symbol": "",
            "Separator": ""
        }

        self.gcbMappings = {
            "SpacingMark": "SPACING_MARK"
        }

        self.scriptMappings = {
            "Afak": "AFAKA",
            "Blis": "BLISSYMBOLS",
            "Cirt": "CIRTH",
            "Cyrs":  "OLD_CHURCH_SLAVONIC_CYRILLIC",
            "Egyd": "DEMOTIC_EGYPTIAN",
            "Egyh": "HIERATIC_EGYPTIAN",
            "Geok": "KHUTSURI",
            "Hanb": "HAN_WITH_BOPOMOFO",
            "Hans": "SIMPLIFIED_HAN",
            "Hant": "TRADITIONAL_HAN",
            "Inds": "HARAPPAN_INDUS",
            "Jpan": "JAPANESE",
            "Jurc": "JURCHEN",
            "Kore": "KOREAN",
            "Kpel": "KPELLE",
            "Tai_Tham": "LANNA",
            "Latf": "LATIN_FRAKTUR",
            "Latg": "LATIN_GAELIC",
            "Maya": "MAYAN_HIEROGLYPHS",
            "Mende_Kikakui": "MENDE",
            "Meetei_Mayek": "MEITEI_MAYEK",
            "Nkgb": "NAKHI_GEBA",
            "Old_Turkic": "ORKHON",
            "Phlv": "BOOK_PAHLAVI",
            "Roro": "RONGORONGO",
            "Sara": "SARATI",
            "SignWriting": "SIGN_WRITING",
            "Syre": "ESTRANGELO_SYRIAC",
            "Syrj": "WESTERN_SYRIAC",
            "Syrn": "EASTERN_SYRIAC",
            "Teng": "TENGWAR",
            "Visp": "VISIBLE_SPEECH",
            "Wole": "WOLEAI",
            "Zmth": "MATHEMATICAL_NOTATION",
            "Zsye": "SYMBOLS_EMOJI",
            "Zsym": "SYMBOLS",
            "Zxxx": "UNWRITTEN_LANGUAGES",
        }


        self.prefix = {
            "bc": ("U", "bidiClass", self.bcMapings),
            "blk": ("UBLOCK", "block", self.blkMappings),
            "dt": ("U_DT", "decompositionType", {}),
            "ea": ("U_EA", "eastAsianWidth", {}),
            "gc": ("U", "generalCategory", self.gcMappings),
            "GCB": ("U_GCB", "graphemeClusterBreak", self.gcbMappings),
            "hst": ("U_HST", "hangulSyllableType", {}),
            "InPC": ("U_INPC", "indicPositionalCategory", {}),
            "InSC": ("U_INSC", "indicSyllabicCategory", {}),
            "jg": ("U_JG", "joiningGroup", {}),
            "jt": ("U_JT", "joiningType", {}),
            "lb": ("U_LB", "lineBreak", {}),
            "nt": ("U_NT", "numberType", {}),
            "SB": ("U_SB", "sentenceBreak", {}),
            "sc": ("USCRIPT", "script", self.scriptMappings),
            "vo": ("U_VO", "verticalOrientation", {}),
            "WB": ("U_WB", "wordBreak", {})
        }

        self.lines = {}

        self.prefixLines = ['"""/']

        todayString = datetime.now().astimezone().strftime("%B %_d, %Y at %I:%M:%S %p %Z")
        toolName = Path(__file__).name


        self.outPath = outDirectory / "UCDTypeDictionaries.py"
        ppucdPath = icuDirectory / "data/unidata/ppucd.txt"

        self.prefixLines.append(f"{self.outPath.name}, based on {ppucdPath.name} from ICU\n")
        self.prefixLines.append(f"Generated by {toolName} on {todayString}")
        self.prefixLines.append('"""\n')

        self.prefixLines.append("from uchar_h import *")
        self.prefixLines.append("from uscript_h import *\n")


        self.file = open(ppucdPath, newline="")
        self.reader = csv.reader(self.file, delimiter=";")

    def generateDictionaries(self):
        for row in self.reader:
            if row:
                kind = row[0]

                if kind == "ucd":
                    self.ucdVersion = row[1]
                elif kind == "value":
                    type = row[1]
                    shortName = row[2]
                    longName = row[3]
                    if (typePrefix := self.prefix.get(type)):
                        if type not in self.lines:
                            self.lines[type] = []

                        key = typePrefix[2].get(longName)
                        if key == "": continue
                        if not key:
                            key = longName.upper()

                        self.lines[type].append(f"    {typePrefix[0]}_{key}: \"{shortName.replace('_', ' ')}\"")

    def writeFile(self):
        self.file.close()
        outFile = open(self.outPath, "w")

        for headerLine in self.prefixLines:
            outFile.write(f"{headerLine}\n")

        for type, values in self.lines.items():
            outFile.write(f"{self.prefix[type][1]}Names = " + "{\n")
            outFile.write(",\n".join(values))
            outFile.write("\n}\n\n")

        outFile.close()


def test():
    icuSource = Path("/Users/emader/Downloads/icu69/icu4c/source")
    testDir = Path("test")

    ucdReader = UCDReader(icuSource, testDir)
    ucdReader.generateDictionaries()
    ucdReader.writeFile()

    print(f"UCD version = {ucdReader.ucdVersion}")

if __name__ == "__main__":
    test()
