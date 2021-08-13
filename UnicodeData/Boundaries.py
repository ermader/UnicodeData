"""\
Based on types from uchar.h in ICU

Created on May 6, 2020

@author Eric Mader
"""

# Grapheme cluster break
GCB_OTHER = 0            # [XX]
GCB_CONTROL = 1          # [CN]
GCB_CR = 2               # [CR]
GCB_EXTEND = 3           # [EX]
GCB_L = 4                # [L]
GCB_LF = 5               # [LF]
GCB_LV = 6               # [LV]
GCB_LVT = 7              # [LVT]
GCB_T = 8                # [T]
GCB_V = 9                # [V]
# @stable ICU 4.0
GCB_SPACING_MARK = 10    # [SM] from here on: new in Unicode 5.1/ICU 4.0
# @stable ICU 4.0
GCB_PREPEND = 11         # [PP]
# @stable ICU 50
GCB_REGIONAL_INDICATOR = 12  # [RI] new in Unicode 6.2/ICU 50
# @stable ICU 58
GCB_E_BASE = 13          # [EB] from here on: new in Unicode 9.0/ICU 58
# @stable ICU 58
GCB_E_BASE_GAZ = 14      # [EBG]
# @stable ICU 58
GCB_E_MODIFIER = 15      # [EM]
# @stable ICU 58
GCB_GLUE_AFTER_ZWJ = 16  # [GAZ]
# @stable ICU 58
GCB_ZWJ = 17             # [ZWJ]

# Word break
WB_OTHER = 0             # [XX]
WB_ALETTER = 1           # [LE]
WB_FORMAT = 2            # [FO]
WB_KATAKANA = 3          # [KA]
WB_MIDLETTER = 4         # [ML]
WB_MIDNUM = 5            # [MN]
WB_NUMERIC = 6           # [NU]
WB_EXTENDNUMLET = 7      # [EX]
# @stable ICU 4.0
WB_CR = 8                # [CR] from here on: new in Unicode 5.1/ICU 4.0
# @stable ICU 4.0
WB_EXTEND = 9            # [Extend]
# @stable ICU 4.0
WB_LF = 10               # [LF]
# @stable ICU 4.0
WB_MIDNUMLET =11         # [MB]
# @stable ICU 4.0
WB_NEWLINE =12           # [NL]
# @stable ICU 50
WB_REGIONAL_INDICATOR = 13   # [RI] new in Unicode 6.2/ICU 50
# @stable ICU 52
WB_HEBREW_LETTER = 14    # [HL] from here on: new in Unicode 6.3/ICU 52
# @stable ICU 52
WB_SINGLE_QUOTE = 15     # [SQ]
# @stable ICU 52
WB_DOUBLE_QUOTE = 16     # [DQ]
# @stable ICU 58
WB_E_BASE = 17           # [EB] from here on: new in Unicode 9.0/ICU 58
# @stable ICU 58
WB_E_BASE_GAZ = 18       # [EBG]
# @stable ICU 58
WB_E_MODIFIER = 19       # [EM]
# @stable ICU 58
WB_GLUE_AFTER_ZWJ = 20   # [GAZ]
# @stable ICU 58
WB_ZWJ = 21              # [ZWJ]
# @stable ICU 62
WB_WSEGSPACE = 22        # [WSEGSPACE]

# Sentence break
SB_OTHER = 0             # [XX]
SB_ATERM = 1             # [AT]
SB_CLOSE = 2             # [CL]
SB_FORMAT = 3            # [FO]
SB_LOWER = 4             # [LO]
SB_NUMERIC = 5           # [NU]
SB_OLETTER = 6           # [LE]
SB_SEP = 7               # [SE]
SB_SP = 8                # [SP]
SB_STERM = 9             # [ST]
SB_UPPER = 10            # [UP]
SB_CR = 11               # [CR] from here on: new in Unicode 5.1/ICU 4.0
SB_EXTEND = 12           # [EX]
SB_LF = 13               # [LF]
SB_SCONTINUE = 14        # [SC]

# Line break
LB_UNKNOWN = 0           # [XX]
LB_AMBIGUOUS = 1         # [AI]
LB_ALPHABETIC = 2        # [AL]
LB_BREAK_BOTH = 3        # [B2]
LB_BREAK_AFTER = 4       # [BA]
LB_BREAK_BEFORE = 5      # [BB]
LB_MANDATORY_BREAK = 6   # [BK]
LB_CONTINGENT_BREAK = 7  # [CB]
LB_CLOSE_PUNCTUATION = 8 # [CL]
LB_COMBINING_MARK = 9    # [CM]
LB_CARRIAGE_RETURN = 10   # [CR]
LB_EXCLAMATION = 11       # [EX]
LB_GLUE = 12              # [GL]
LB_HYPHEN = 13            # [HY]
LB_IDEOGRAPHIC = 14       # [ID]
LB_INSEPARABLE = 15       # [IN]
LB_INFIX_NUMERIC = 16     # [IS]
LB_LINE_FEED = 17         # [LF]
LB_NONSTARTER = 18        # [NS]
LB_NUMERIC = 19           # [NU]
LB_OPEN_PUNCTUATION = 20  # [OP]
LB_POSTFIX_NUMERIC = 21   # [PO]
LB_PREFIX_NUMERIC = 22    # [PR]
LB_QUOTATION = 23         # [QU]
LB_COMPLEX_CONTEXT = 24   # [SA]
LB_SURROGATE = 25         # [SG]
LB_SPACE = 26             # [SP]
LB_BREAK_SYMBOLS = 27     # [SY]
LB_ZWSPACE = 28           # [ZW]
# @stable ICU 2.6
LB_NEXT_LINE = 29         # [NL] #  from here on: new in Unicode 4/ICU 2.6
# @stable ICU 2.6
LB_WORD_JOINER = 30       # [WJ]
# @stable ICU 3.4
LB_H2 = 31                # [H2] #  from here on: new in Unicode 4.1/ICU 3.4
# @stable ICU 3.4
LB_H3 = 32                # [H3]
# @stable ICU 3.4
LB_JL = 33                # [JL]
# @stable ICU 3.4
LB_JT = 34                # [JT]
# @stable ICU 3.4
LB_JV = 35                # [JV]
# @stable ICU 4.4
LB_CLOSE_PARENTHESIS = 36 # [CP] new in Unicode 5.2/ICU 4.4
# @stable ICU 49
LB_CONDITIONAL_JAPANESE_STARTER = 37 # [CJ]  new in Unicode 6.1/ICU 49
# @stable ICU 49
LB_HEBREW_LETTER = 38     # [HL] new in Unicode 6.1/ICU 49
# @stable ICU 50
LB_REGIONAL_INDICATOR = 39# [RI] new in Unicode 6.2/ICU 50
# @stable ICU 58
LB_E_BASE = 40            # [EB] from here on: new in Unicode 9.0/ICU 58
# @stable ICU 58
LB_E_MODIFIER = 41        # [EM]
# @stable ICU 58
LB_ZWJ = 42               # [ZWJ]

graphemeClusterBreakNames = {
    GCB_OTHER: "XX",
    GCB_CONTROL: "CN",
    GCB_CR: "CR",
    GCB_EXTEND: "EX",
    GCB_L: "L",
    GCB_LF: "LF",
    GCB_LV: "LV",
    GCB_LVT: "LVT",
    GCB_T: "T",
    GCB_V: "V",
    GCB_SPACING_MARK: "SM",
    GCB_PREPEND: "PP",
    GCB_REGIONAL_INDICATOR: "RI",
    GCB_E_BASE: "EB",
    GCB_E_BASE_GAZ: "EBG",
    GCB_E_MODIFIER: "EM",
    GCB_GLUE_AFTER_ZWJ: "GAZ",
    GCB_ZWJ: "ZWJ"
}

wordBreakNames = {
    WB_OTHER: "XX",
    WB_ALETTER: "LE",
    WB_FORMAT: "FO",
    WB_KATAKANA: "KA",
    WB_MIDLETTER: "ML",
    WB_MIDNUM: "MN",
    WB_NUMERIC: "NU",
    WB_EXTENDNUMLET: "EX",
    WB_CR: "CR",
    WB_EXTEND: "Extend",
    WB_LF: "LF",
    WB_MIDNUMLET: "MB",
    WB_NEWLINE: "NL",
    WB_REGIONAL_INDICATOR: "RI",
    WB_HEBREW_LETTER: "HL",
    WB_SINGLE_QUOTE: "SQ",
    WB_DOUBLE_QUOTE: "DQ",
    WB_E_BASE: "EB",
    WB_E_BASE_GAZ: "EBG",
    WB_E_MODIFIER: "EM",
    WB_GLUE_AFTER_ZWJ: "GAZ",
    WB_ZWJ: "ZWJ",
    WB_WSEGSPACE: "WSEGSPACE"
}

sentenceBreakNames = {
    SB_OTHER: "XX",
    SB_ATERM: "AT",
    SB_CLOSE: "CL",
    SB_FORMAT: "FO",
    SB_LOWER: "LO",
    SB_NUMERIC: "NU",
    SB_OLETTER: "LE",
    SB_SEP: "SE",
    SB_SP: "SP",
    SB_STERM: "ST",
    SB_UPPER: "UP",
    SB_CR: "CR",
    SB_EXTEND: "EX",
    SB_LF: "LF",
    SB_SCONTINUE: "SC"
}

lineBreakNames = {
    LB_UNKNOWN: "XX",
    LB_AMBIGUOUS: "AI",
    LB_ALPHABETIC: "AL",
    LB_BREAK_BOTH: "B2",
    LB_BREAK_AFTER: "BA",
    LB_BREAK_BEFORE: "BB",
    LB_MANDATORY_BREAK: "BK",
    LB_CONTINGENT_BREAK: "CB",
    LB_CLOSE_PUNCTUATION: "CL",
    LB_COMBINING_MARK: "CM",
    LB_CARRIAGE_RETURN: "CR",
    LB_EXCLAMATION: "EX",
    LB_GLUE: "GL",
    LB_HYPHEN: "HY",
    LB_IDEOGRAPHIC: "ID",
    LB_INSEPARABLE: "IN",
    LB_INFIX_NUMERIC: "IS",
    LB_LINE_FEED: "LF",
    LB_NONSTARTER: "NS",
    LB_NUMERIC: "NU",
    LB_OPEN_PUNCTUATION: "OP",
    LB_POSTFIX_NUMERIC: "PO",
    LB_PREFIX_NUMERIC: "PR",
    LB_QUOTATION: "QU",
    LB_COMPLEX_CONTEXT: "SA",
    LB_SURROGATE: "SG",
    LB_SPACE: "SP",
    LB_BREAK_SYMBOLS: "SY",
    LB_ZWSPACE: "ZW",
    LB_NEXT_LINE: "NL",
    LB_WORD_JOINER: "WJ",
    LB_H2: "H2",
    LB_H3: "H3",
    LB_JL: "JL",
    LB_JT: "JT",
    LB_JV: "JV",
    LB_CLOSE_PARENTHESIS: "CP",
    LB_CONDITIONAL_JAPANESE_STARTER: "CJ",
    LB_HEBREW_LETTER: "HL",
    LB_REGIONAL_INDICATOR: "RI",
    LB_E_BASE: "EB",
    LB_E_MODIFIER: "EM",
    LB_ZWJ: "ZWJ"
}
