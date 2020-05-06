"""\
Based on types from uprops.h in ICU

Created on May 6, 2020

@author Eric Mader
"""

# Grapheme cluster break
U_GCB_OTHER = 0            # [XX]
U_GCB_CONTROL = 1          # [CN]
U_GCB_CR = 2               # [CR]
U_GCB_EXTEND = 3           # [EX]
U_GCB_L = 4                # [L]
U_GCB_LF = 5               # [LF]
U_GCB_LV = 6               # [LV]
U_GCB_LVT = 7              # [LVT]
U_GCB_T = 8                # [T]
U_GCB_V = 9                # [V]
# @stable ICU 4.0
U_GCB_SPACING_MARK = 10    # [SM] from here on: new in Unicode 5.1/ICU 4.0
# @stable ICU 4.0
U_GCB_PREPEND = 11         # [PP]
# @stable ICU 50
U_GCB_REGIONAL_INDICATOR = 12  # [RI] new in Unicode 6.2/ICU 50
# @stable ICU 58
U_GCB_E_BASE = 13          # [EB] from here on: new in Unicode 9.0/ICU 58
# @stable ICU 58
U_GCB_E_BASE_GAZ = 14      # [EBG]
# @stable ICU 58
U_GCB_E_MODIFIER = 15      # [EM]
# @stable ICU 58
U_GCB_GLUE_AFTER_ZWJ = 16  # [GAZ]
# @stable ICU 58
U_GCB_ZWJ = 17             # [ZWJ]

# Word break
U_WB_OTHER = 0             # [XX]
U_WB_ALETTER = 1           # [LE]
U_WB_FORMAT = 2            # [FO]
U_WB_KATAKANA = 3          # [KA]
U_WB_MIDLETTER = 4         # [ML]
U_WB_MIDNUM = 5            # [MN]
U_WB_NUMERIC = 6           # [NU]
U_WB_EXTENDNUMLET = 7      # [EX]
# @stable ICU 4.0
U_WB_CR = 8                # [CR] from here on: new in Unicode 5.1/ICU 4.0
# @stable ICU 4.0
U_WB_EXTEND = 9            # [Extend]
# @stable ICU 4.0
U_WB_LF = 10               # [LF]
# @stable ICU 4.0
U_WB_MIDNUMLET =11         # [MB]
# @stable ICU 4.0
U_WB_NEWLINE =12           # [NL]
# @stable ICU 50
U_WB_REGIONAL_INDICATOR = 13   # [RI] new in Unicode 6.2/ICU 50
# @stable ICU 52
U_WB_HEBREW_LETTER = 14    # [HL] from here on: new in Unicode 6.3/ICU 52
# @stable ICU 52
U_WB_SINGLE_QUOTE = 15     # [SQ]
# @stable ICU 52
U_WB_DOUBLE_QUOTE = 16     # [DQ]
# @stable ICU 58
U_WB_E_BASE = 17           # [EB] from here on: new in Unicode 9.0/ICU 58
# @stable ICU 58
U_WB_E_BASE_GAZ = 18       # [EBG]
# @stable ICU 58
U_WB_E_MODIFIER = 19       # [EM]
# @stable ICU 58
U_WB_GLUE_AFTER_ZWJ = 20   # [GAZ]
# @stable ICU 58
U_WB_ZWJ = 21              # [ZWJ]
# @stable ICU 62
U_WB_WSEGSPACE = 22        # [WSEGSPACE]

# Sentence break
U_SB_OTHER = 0             # [XX]
U_SB_ATERM = 1             # [AT]
U_SB_CLOSE = 2             # [CL]
U_SB_FORMAT = 3            # [FO]
U_SB_LOWER = 4             # [LO]
U_SB_NUMERIC = 5           # [NU]
U_SB_OLETTER = 6           # [LE]
U_SB_SEP = 7               # [SE]
U_SB_SP = 8                # [SP]
U_SB_STERM = 9             # [ST]
U_SB_UPPER = 10            # [UP]
U_SB_CR = 11               # [CR] from here on: new in Unicode 5.1/ICU 4.0
U_SB_EXTEND = 12           # [EX]
U_SB_LF = 13               # [LF]
U_SB_SCONTINUE = 14        # [SC]

# Line break
U_LB_UNKNOWN = 0           # [XX]
U_LB_AMBIGUOUS = 1         # [AI]
U_LB_ALPHABETIC = 2        # [AL]
U_LB_BREAK_BOTH = 3        # [B2]
U_LB_BREAK_AFTER = 4       # [BA]
U_LB_BREAK_BEFORE = 5      # [BB]
U_LB_MANDATORY_BREAK = 6   # [BK]
U_LB_CONTINGENT_BREAK = 7  # [CB]
U_LB_CLOSE_PUNCTUATION = 8 # [CL]
U_LB_COMBINING_MARK = 9    # [CM]
U_LB_CARRIAGE_RETURN = 10   # [CR]
U_LB_EXCLAMATION = 11       # [EX]
U_LB_GLUE = 12              # [GL]
U_LB_HYPHEN = 13            # [HY]
U_LB_IDEOGRAPHIC = 14       # [ID]
U_LB_INSEPARABLE = 15       # [IN]
U_LB_INFIX_NUMERIC = 16     # [IS]
U_LB_LINE_FEED = 17         # [LF]
U_LB_NONSTARTER = 18        # [NS]
U_LB_NUMERIC = 19           # [NU]
U_LB_OPEN_PUNCTUATION = 20  # [OP]
U_LB_POSTFIX_NUMERIC = 21   # [PO]
U_LB_PREFIX_NUMERIC = 22    # [PR]
U_LB_QUOTATION = 23         # [QU]
U_LB_COMPLEX_CONTEXT = 24   # [SA]
U_LB_SURROGATE = 25         # [SG]
U_LB_SPACE = 26             # [SP]
U_LB_BREAK_SYMBOLS = 27     # [SY]
U_LB_ZWSPACE = 28           # [ZW]
# @stable ICU 2.6
U_LB_NEXT_LINE = 29         # [NL] #  from here on: new in Unicode 4/ICU 2.6
# @stable ICU 2.6
U_LB_WORD_JOINER = 30       # [WJ]
# @stable ICU 3.4
U_LB_H2 = 31                # [H2] #  from here on: new in Unicode 4.1/ICU 3.4
# @stable ICU 3.4
U_LB_H3 = 32                # [H3]
# @stable ICU 3.4
U_LB_JL = 33                # [JL]
# @stable ICU 3.4
U_LB_JT = 34                # [JT]
# @stable ICU 3.4
U_LB_JV = 35                # [JV]
# @stable ICU 4.4
U_LB_CLOSE_PARENTHESIS = 36 # [CP] new in Unicode 5.2/ICU 4.4
# @stable ICU 49
U_LB_CONDITIONAL_JAPANESE_STARTER = 37 # [CJ]  new in Unicode 6.1/ICU 49
# @stable ICU 49
U_LB_HEBREW_LETTER = 38     # [HL] new in Unicode 6.1/ICU 49
# @stable ICU 50
U_LB_REGIONAL_INDICATOR = 39# [RI] new in Unicode 6.2/ICU 50
# @stable ICU 58
U_LB_E_BASE = 40            # [EB] from here on: new in Unicode 9.0/ICU 58
# @stable ICU 58
U_LB_E_MODIFIER = 41        # [EM]
# @stable ICU 58
U_LB_ZWJ = 42               # [ZWJ]

graphemeClusterBreakNames = {
    U_GCB_OTHER: "XX",
    U_GCB_CONTROL: "CN",
    U_GCB_CR: "CR",
    U_GCB_EXTEND: "EX",
    U_GCB_L: "L",
    U_GCB_LF: "LF",
    U_GCB_LV: "LV",
    U_GCB_LVT: "LVT",
    U_GCB_T: "T",
    U_GCB_V: "V",
    U_GCB_SPACING_MARK: "SM",
    U_GCB_PREPEND: "PP",
    U_GCB_REGIONAL_INDICATOR: "RI",
    U_GCB_E_BASE: "EB",
    U_GCB_E_BASE_GAZ: "EBG",
    U_GCB_E_MODIFIER: "EM",
    U_GCB_GLUE_AFTER_ZWJ: "GAZ",
    U_GCB_ZWJ: "ZWJ"
}

wordBreakNames = {
    U_WB_OTHER: "XX",
    U_WB_ALETTER: "LE",
    U_WB_FORMAT: "FO",
    U_WB_KATAKANA: "KA",
    U_WB_MIDLETTER: "ML",
    U_WB_MIDNUM: "MN",
    U_WB_NUMERIC: "NU",
    U_WB_EXTENDNUMLET: "EX",
    U_WB_CR: "CR",
    U_WB_EXTEND: "Extend",
    U_WB_LF: "LF",
    U_WB_MIDNUMLET: "MB",
    U_WB_NEWLINE: "NL",
    U_WB_REGIONAL_INDICATOR: "RI",
    U_WB_HEBREW_LETTER: "HL",
    U_WB_SINGLE_QUOTE: "SQ",
    U_WB_DOUBLE_QUOTE: "DQ",
    U_WB_E_BASE: "EB",
    U_WB_E_BASE_GAZ: "EBG",
    U_WB_E_MODIFIER: "EM",
    U_WB_GLUE_AFTER_ZWJ: "GAZ",
    U_WB_ZWJ: "ZWJ",
    U_WB_WSEGSPACE: "WSEGSPACE"
}

sentenceBreakNames = {
    U_SB_OTHER: "XX",
    U_SB_ATERM: "AT",
    U_SB_CLOSE: "CL",
    U_SB_FORMAT: "FO",
    U_SB_LOWER: "LO",
    U_SB_NUMERIC: "NU",
    U_SB_OLETTER: "LE",
    U_SB_SEP: "SE",
    U_SB_SP: "SP",
    U_SB_STERM: "ST",
    U_SB_UPPER: "UP",
    U_SB_CR: "CR",
    U_SB_EXTEND: "EX",
    U_SB_LF: "LF",
    U_SB_SCONTINUE: "SC"
}

lineBreakNames = {
    U_LB_UNKNOWN: "XX",
    U_LB_AMBIGUOUS: "AI",
    U_LB_ALPHABETIC: "AL",
    U_LB_BREAK_BOTH: "B2",
    U_LB_BREAK_AFTER: "BA",
    U_LB_BREAK_BEFORE: "BB",
    U_LB_MANDATORY_BREAK: "BK",
    U_LB_CONTINGENT_BREAK: "CB",
    U_LB_CLOSE_PUNCTUATION: "CL",
    U_LB_COMBINING_MARK: "CM",
    U_LB_CARRIAGE_RETURN: "CR",
    U_LB_EXCLAMATION: "EX",
    U_LB_GLUE: "GL",
    U_LB_HYPHEN: "HY",
    U_LB_IDEOGRAPHIC: "ID",
    U_LB_INSEPARABLE: "IN",
    U_LB_INFIX_NUMERIC: "IS",
    U_LB_LINE_FEED: "LF",
    U_LB_NONSTARTER: "NS",
    U_LB_NUMERIC: "NU",
    U_LB_OPEN_PUNCTUATION: "OP",
    U_LB_POSTFIX_NUMERIC: "PO",
    U_LB_PREFIX_NUMERIC: "PR",
    U_LB_QUOTATION: "QU",
    U_LB_COMPLEX_CONTEXT: "SA",
    U_LB_SURROGATE: "SG",
    U_LB_SPACE: "SP",
    U_LB_BREAK_SYMBOLS: "SY",
    U_LB_ZWSPACE: "ZW",
    U_LB_NEXT_LINE: "NL",
    U_LB_WORD_JOINER: "WJ",
    U_LB_H2: "H2",
    U_LB_H3: "H3",
    U_LB_JL: "JL",
    U_LB_JT: "JT",
    U_LB_JV: "JV",
    U_LB_CLOSE_PARENTHESIS: "CP",
    U_LB_CONDITIONAL_JAPANESE_STARTER: "CJ",
    U_LB_HEBREW_LETTER: "HL",
    U_LB_REGIONAL_INDICATOR: "RI",
    U_LB_E_BASE: "EB",
    U_LB_E_MODIFIER: "EM",
    U_LB_ZWJ: "ZWJ"
}
