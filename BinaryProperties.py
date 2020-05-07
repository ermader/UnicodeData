'''\
Created on May 5, 2020

Various binary properties.

@author: Eric Mader
'''

from UCDProperties import UCDProperties

propsList = [
    ("whitespace", "WSpace"),
    ("dash", "Dash"),
    ("hyphen", "Hyphen"),
    ("quotationMark", "QMark"),
    ("terminalPunctuation", "Term"),
    ("sentenceTerminalPunctuation", "STerm"),
    ("diacritic", "Dia"),
    ("extender", "Ext"),
    ("prependedConcatenationMark", "PCM"),
    ("softDotted", "SD"),
    ("alphabetic", "Alpha"),
    ("otherAlphabetic", "OAlpha"),
    ("math", "Math"),
    ("otherMath", "OMath"),
    ("hexDigit", "Hex"),
    ("asciiHexDigit", "AHex"),
    ("defaultIgnorable", "DI"),
    ("otherDefaultIgnorable", "ODI"),
    ("logicalOrderException", "LOE"),
    ("regionalIndicator", "RI"),
    ("graphemeBase", "Gr_Base"),
    ("graphemeExtended", "Gr_Ext"),
    ("otherGraphemeExtended", "OGr_Ext"),
    ("graphemeLink", "Gr_Link"),
    ("ideographic", "Ideo"),
    ("unifiedIdeographic", "UIdeo"),
    ("idsBinaryOperator", "IDSB"),
    ("idsTrinaryOperator", "IDST"),
    ("radical", "Radical"),
    ("deprecated", "Dep"),
    ("variationSelector", "VS"),
    ("nonCharacterCodePoint", "NChar"),
    ("idStart", "IDS"),
    ("otherIDStart", "OIDS"),
    ("xIDStart", "XIDS"),
    ("idContinue", "IDC"),
    ("otherIDContinue", "OIDC"),
    ("xIDContinue", "XIDC"),
    ("patternSyntax", "Pat_Syn"),
    ("patternWhitespace", "Pat_WS")
]

class BinaryProperties(UCDProperties):
    def __init__(self, char, group):
        UCDProperties.__init__(self, char, group)

        for (field, tag) in propsList:
            value = self.getBooleanProperty(tag)
            setattr(self, field, value)

        self._char = None
        self._group = None

