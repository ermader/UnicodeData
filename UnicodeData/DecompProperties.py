'''\
Created on Apr 23, 2020

Character Decomposition properties

@author: emader
'''

from xml.etree.ElementTree import Element
from .UCDProperties import UCDProperties

class DecompProperties(UCDProperties):
    def dmToString(self, dm: str, doPoundSign: bool =False):
        # We don't care about characters that decompose to a single character -
        # they either decompose to themselves or are for compatibility.
        # We also don't care about decompositions that start w/ a space
        # if " " not in dm or dm.startswith("0020 "):
        #     return None

        if doPoundSign and dm == "#":
            return chr(self.codePoint)

        if not dm or dm == "#": return None

        codePoints = dm.split(" ")
        chars: list[str] = []
        for codePoint in codePoints:
            chars.append(chr(int(codePoint, 16)))

        return "".join(chars)

    def __init__(self, char: Element, group: Element):
        UCDProperties.__init__(self, char, group)

        self.decompositionType = self.getCharProperty("dt")

        dm = self.getCharProperty("dm")
        self.decomposition = self.dmToString(dm)

        self.compositionExclusion = self.getBooleanProperty("CE")
        self.fullCompositionExclusion = self.getBooleanProperty("Comp_Ex")

        # these are "Y", "N" or "M"
        self.nfcQuickCheck = self.getCharProperty("NFC_QC")
        self.nfdQuickCheck = self.getCharProperty("NFD_QC")
        self.nfkcQuickCheck = self.getCharProperty("NFKC_QC")
        self.nfkdQuickCheck = self.getCharProperty("NFKD_QC")

        self.expandOnNFC = self.getBooleanProperty("XO_NFC")
        self.expandOnNFD = self.getBooleanProperty("XO_NFD")
        self.expandOnNFKC = self.getBooleanProperty("XO_NFKC")
        self.expandOnNFKD = self.getBooleanProperty("XO_NFKD")

        self.nfkcFullClosure = self.dmToString(self.getCharProperty("FC_NFKC"))
        self.nfkcCaseFolded = self.dmToString(self.getCharProperty("NFKC_CF"), doPoundSign=True)

        # Don't need these any more
        del self._char
        del self._group
