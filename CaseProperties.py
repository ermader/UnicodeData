'''\
Created on Apr 14, 2020

Case properties properties.

@author: emader
'''

from UCDProperties import UCDProperties

class CaseProperties(UCDProperties):
    def __init__(self, char, group):
        UCDProperties.__init__(self, char, group)

        self.upper = self.getBooleanProperty("Upper")
        self.lower = self.getBooleanProperty("Lower")
        self.otherUpper = self.getBooleanProperty("OUpper")
        self.otherLower = self.getBooleanProperty("OLower")

        self.simpleUpperCase = self.getCodePointsProperty("suc")
        self.simpleLowerCase = self.getCodePointsProperty("slc")
        self.simpleTitleCase = self.getCharProperty("stc")

        self.upperCase = self.getCodePointsProperty("uc")
        self.lowerCase = self.getCodePointsProperty("lc")
        self.titleCase = self.getCodePointsProperty("tc")

        self.simpleCaseFolding = self.getCodePointsProperty("scf")
        self.caseFolding = self.getCodePointsProperty("cf")

        self.caseIgnorable = self.getBooleanProperty("CI")
        self.cased = self.getBooleanProperty("Cased")
        self.changesWhenCaseFolded = self.getBooleanProperty("CWCF")
        self.changesWhenCasedMapped = self.getBooleanProperty("CWCM")
        self.changesWhenLowercased = self.getBooleanProperty("CWL")
        self.changesWhenNFKCCaseFolded = self.getBooleanProperty("CWKCF")
        self.changesWhenTitlecased = self.getBooleanProperty("CWT")
        self.changesWhenUppercased = self.getBooleanProperty("CWU")
        self.nkfcCasefold = self.getCodePointsProperty("NFKC_CF")

        self._char = None
        self._group = None