'''
Created on Apr 14, 2020

@author: emader
'''

from xml.etree.ElementTree import Element

from .UCDProperties import UCDProperties
from .BidiProperties import BidiProperties
from .DecompProperties import DecompProperties
from .CaseProperties import CaseProperties
from .IndicProperties import IndicProperties
from .BinaryProperties import BinaryProperties

class CharacterData(UCDProperties):
    def __init__(self, char: Element, group: Element):
        UCDProperties.__init__(self, char, group)

        # cp = self.getCharProperty("cp")
        # self.codePoint = int(cp, 16)

        ccc = self.getCharProperty("ccc")
        self.combiningClass = int(ccc)

        self.name = self.getCharProperty("na")
        self.generalCategory = self.getCharProperty("gc")

        self.bidiProperties = BidiProperties(char, group)

        self.numericType = self.getCharProperty("nt")
        nv = self.getCharProperty("nv")
        self.numericValue = None if nv == "NaN" else eval(nv)

        self.script = self.getCharProperty("sc")
        self.scriptExtensions = self.getCharProperty("scx").split(" ")
        self.block = self.getCharProperty("blk").replace("_", " ")

        self.decompProperties = DecompProperties(char, group)

        self.joiningType = self.getCharProperty("jt")
        self.joiningGroup = self.getCharProperty("jg").replace("_", " ")
        self.isJoiningControl = self.getBooleanProperty("Join_C")

        self.lineBreak = self.getCharProperty("lb")
        self.sentenceBreak = self.getCharProperty("SB")
        self.wordBreak = self.getCharProperty("WB")
        self.graphemeClusterBreak = self.getCharProperty("GCB")

        self.eastAsianWidth = self.getCharProperty("ea")

        self.caseProperties = CaseProperties(char, group)

        self.hangulSyllableType = self.getCharProperty("hst")
        self.jamoShortName = self.getCharProperty("JSN")  # maybe empty string => None?

        self.indicProperties = IndicProperties(char, group)
        self.verticalOrientation = self.getCharProperty("vo")

        self.binaryProperties = BinaryProperties(char, group)

        self.emoji = self.getBooleanProperty("Emoji")
        self.emojiPresentation = self.getBooleanProperty("EPres")
        self.emojiModifier = self.getBooleanProperty("EMod")
        self.emojiModifierBase = self.getBooleanProperty("EBase")
        self.emojiComponent = self.getBooleanProperty("EComp")
        self.extendedPictograph = self.getBooleanProperty("ExtPict")

        # if self.name is None or len(self.name) == 0:
        #     self.name = self.getCharProperty("na1")

        self.name = self.name.replace("#", self.cp)

        # Don't need these any more
        del self._char
        del self._group
