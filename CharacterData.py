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

        self.script = self.getCharProperty("sc")
        self.block = self.getCharProperty("blk")

        self.decompProperties = DecompProperties(char, group)

        if self.name is None or len(self.name) == 0:
            self.name = self.getCharProperty("na1")

        self.name = self.name.replace("#", cp)
