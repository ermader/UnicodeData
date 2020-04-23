'''
Created on Apr 14, 2020

@author: emader
'''

from UCDProperties import UCDProperties
from BidiProperties import BidiProperties
from DecompProperties import DecompProperties

class CharacterData(UCDProperties):
    def __init__(self, char, group):
        UCDProperties.__init__(self, char, group)

        cp = self.getCharProperty("cp")
        self.codePoint = int(cp, 16)

        ccc = self.getCharProperty("ccc")
        self.combiningClass = int(ccc)

        self.name = self.getCharProperty("na")
        self.generalCategory = self.getCharProperty("gc")

        self.bidiProperties = BidiProperties(char, group)

        self.numericType = self.getCharProperty("nt")
        nv = self.getCharProperty("nv")
        self.numericValue = None if nv == "NaN" else eval(nv)

        self.script = self.getCharProperty("sc")
        self.block = self.getCharProperty("blk")

        self.decompProperties = DecompProperties(char, group)

        if self.name is None or len(self.name) == 0:
            self.name = self.getCharProperty("na1")

        self.name = self.name.replace("#", cp)

        # Don't need these any more
        self._char = None
        self._group = None
