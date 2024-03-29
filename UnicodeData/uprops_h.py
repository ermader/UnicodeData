"""/
uprops_h.py, based on uprops.h from ICU

Generated by HeaderToPtyhon.py on August 26, 2021 at 11:27:13 AM HST
"""

UPROPS_PROPS32_INDEX = 0
UPROPS_EXCEPTIONS_INDEX = 1
UPROPS_EXCEPTIONS_TOP_INDEX = 2
UPROPS_ADDITIONAL_TRIE_INDEX = 3
UPROPS_ADDITIONAL_VECTORS_INDEX = 4
UPROPS_ADDITIONAL_VECTORS_COLUMNS_INDEX = 5
UPROPS_SCRIPT_EXTENSIONS_INDEX = 6
UPROPS_RESERVED_INDEX_7 = 7
UPROPS_RESERVED_INDEX_8 = 8
UPROPS_DATA_TOP_INDEX = 9
UPROPS_MAX_VALUES_INDEX = 10
UPROPS_MAX_VALUES_2_INDEX = 11
UPROPS_INDEX_COUNT = 16
UPROPS_NUMERIC_TYPE_VALUE_SHIFT = 6  #   6 (10 bits) 
UPROPS_NTV_NONE = 0
UPROPS_NTV_DECIMAL_START = 1
UPROPS_NTV_DIGIT_START = 11
UPROPS_NTV_NUMERIC_START = 21
UPROPS_NTV_FRACTION_START = 0xb0
UPROPS_NTV_LARGE_START = 0x1e0
UPROPS_NTV_BASE60_START = 0x300
UPROPS_NTV_FRACTION20_START = UPROPS_NTV_BASE60_START+36  # 0x300+9*4=0x324
UPROPS_NTV_FRACTION32_START = UPROPS_NTV_FRACTION20_START+24  # 0x324+6*4=0x34c
UPROPS_NTV_RESERVED_START = UPROPS_NTV_FRACTION32_START+16  # 0x34c+4*4=0x35c
UPROPS_NTV_MAX_SMALL_INT = UPROPS_NTV_FRACTION_START-UPROPS_NTV_NUMERIC_START-1
UPROPS_VECTOR_WORDS = 3
UPROPS_AGE_MASK = 0xff000000
UPROPS_AGE_SHIFT = 24
UPROPS_SCRIPT_X_MASK = 0x00f000ff
UPROPS_SCRIPT_X_SHIFT = 22
UPROPS_SCRIPT_HIGH_MASK = 0x00300000
UPROPS_SCRIPT_HIGH_SHIFT = 12
UPROPS_MAX_SCRIPT = 0x3ff
UPROPS_EA_MASK = 0x000e0000
UPROPS_EA_SHIFT = 17
UPROPS_BLOCK_MASK = 0x0001ff00
UPROPS_BLOCK_SHIFT = 8
UPROPS_SCRIPT_LOW_MASK = 0x000000ff
UPROPS_SCRIPT_X_WITH_COMMON = 0x400000
UPROPS_SCRIPT_X_WITH_INHERITED = 0x800000
UPROPS_SCRIPT_X_WITH_OTHER = 0xc00000
UPROPS_WHITE_SPACE = 0
UPROPS_DASH = 1
UPROPS_HYPHEN = 2
UPROPS_QUOTATION_MARK = 3
UPROPS_TERMINAL_PUNCTUATION = 4
UPROPS_MATH = 5
UPROPS_HEX_DIGIT = 6
UPROPS_ASCII_HEX_DIGIT = 7
UPROPS_ALPHABETIC = 8
UPROPS_IDEOGRAPHIC = 9
UPROPS_DIACRITIC = 10
UPROPS_EXTENDER = 11
UPROPS_NONCHARACTER_CODE_POINT = 12
UPROPS_GRAPHEME_EXTEND = 13
UPROPS_GRAPHEME_LINK = 14
UPROPS_IDS_BINARY_OPERATOR = 15
UPROPS_IDS_TRINARY_OPERATOR = 16
UPROPS_RADICAL = 17
UPROPS_UNIFIED_IDEOGRAPH = 18
UPROPS_DEFAULT_IGNORABLE_CODE_POINT = 19
UPROPS_DEPRECATED = 20
UPROPS_LOGICAL_ORDER_EXCEPTION = 21
UPROPS_XID_START = 22
UPROPS_XID_CONTINUE = 23
UPROPS_ID_START = 24  #  ICU 2.6, uprops format version 3.2 
UPROPS_ID_CONTINUE = 25
UPROPS_GRAPHEME_BASE = 26
UPROPS_S_TERM = 27  #  new in ICU 3.0 and Unicode 4.0.1 
UPROPS_VARIATION_SELECTOR = 28
UPROPS_PATTERN_SYNTAX = 29  #  new in ICU 3.4 and Unicode 4.1 
UPROPS_PATTERN_WHITE_SPACE = 30
UPROPS_PREPENDED_CONCATENATION_MARK = 31  # new in ICU 60 and Unicode 10
UPROPS_BINARY_1_TOP = 32  #  ==32 - full! 
UPROPS_2_EXTENDED_PICTOGRAPHIC = 26
UPROPS_2_EMOJI_COMPONENT = 27
UPROPS_2_EMOJI = 28
UPROPS_2_EMOJI_PRESENTATION = 29
UPROPS_2_EMOJI_MODIFIER = 30
UPROPS_2_EMOJI_MODIFIER_BASE = 31
UPROPS_LB_MASK = 0x03f00000
UPROPS_LB_SHIFT = 20
UPROPS_SB_MASK = 0x000f8000
UPROPS_SB_SHIFT = 15
UPROPS_WB_MASK = 0x00007c00
UPROPS_WB_SHIFT = 10
UPROPS_GCB_MASK = 0x000003e0
UPROPS_GCB_SHIFT = 5
UPROPS_DT_MASK = 0x0000001f
TAB = 0x0009
LF = 0x000a
FF = 0x000c
CR = 0x000d
NBSP = 0x00a0
CGJ = 0x034f
FIGURESP = 0x2007
HAIRSP = 0x200a
ZWNJ = 0x200c
ZWJ = 0x200d
RLM = 0x200f
NNBSP = 0x202f
ZWNBSP = 0xfeff
UPROPS_SRC_NONE = 0
UPROPS_SRC_CHAR = 1
UPROPS_SRC_PROPSVEC = 2
UPROPS_SRC_NAMES = 3
UPROPS_SRC_CASE = 4
UPROPS_SRC_BIDI = 5
UPROPS_SRC_CHAR_AND_PROPSVEC = 6
UPROPS_SRC_CASE_AND_NORM = 7
UPROPS_SRC_NFC = 8
UPROPS_SRC_NFKC = 9
UPROPS_SRC_NFKC_CF = 10
UPROPS_SRC_NFC_CANON_ITER = 11
UPROPS_SRC_INPC = 12
UPROPS_SRC_INSC = 13
UPROPS_SRC_VO = 14
UPROPS_SRC_COUNT = 15