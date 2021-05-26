"""/
UcdReader. Read data from ICU's ppucd.txt file.

Created on May 26, 2021

@author Eric Mader
"""

import csv

def test():
    ppucdFile = open("/Users/emader/Downloads/icu69/icu4c/source/data/unidata/ppucd.txt", newline="")
    ppucdReader = csv.reader(ppucdFile, delimiter=";")

    prefix = {
        "bc": ("U", "bidiClass"),
        "blk": ("UBLOCK", "block"),
        "dt": ("U_DT", "decompositionType"),
        "ea": ("U_EA", "eastAsianWidth"),
        "gc": ("U", "generalCategory"),
        "GCB": ("U_GCB", "graphemeClusterBreak"),
        "hst": ("U_HST", "hangulSyllableType"),
        "InPC": ("U_INPC", "indicPositionalCategory"),
        "InSC": ("U_INSC", "indicSyllabicCategory"),
        "jg": ("U_JG", "joiningGroup"),
        "jt": ("U_JT", "joiningType"),
        "lb": ("U_LB", "lineBreak"),
        "nt": ("U_NT", "numberType"),
        "SB": ("U_SB", "sentenceBreak"),
        "sc": ("USCRIPT", "script"),
        "vo": ("U_VO", "verticalOrientation"),
        "WB": ("U_WB", "wordBreak")
    }

    lines = {}
    for row in ppucdReader:
        if row and row[0] == "value":
            key = row[1]
            if key in prefix:
                if key not in lines:
                    lines[key] = []

                lines[key].append(f"    {prefix[key][0]}_{row[3].upper()}: \"{row[2].replace('_', ' ')}\"")

    for type, values in lines.items():
        print(f"{prefix[type][1]}Names = " + "{")
        print(",\n".join(values))
        print("}\n")

if __name__ == "__main__":
    test()
