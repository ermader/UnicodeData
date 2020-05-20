"""\
Based on UCharCategory from uchar.h in ICU

Created on May 3, 2020

@author Eric Mader
"""

# Non-category for unassigned and non-character code points. @stable ICU 2.0
GC_UNASSIGNED = 0
# Cn "Other, Not Assigned (no characters in [UnicodeData.txt] have this property)" (same as GC_UNASSIGNED!) @stable ICU 2.0
GC_GENERAL_OTHER_TYPES = 0
# Lu @stable ICU 2.0
GC_UPPERCASE_LETTER = 1
# Ll @stable ICU 2.0
GC_LOWERCASE_LETTER = 2
# Lt @stable ICU 2.0
GC_TITLECASE_LETTER = 3
# Lm @stable ICU 2.0
GC_MODIFIER_LETTER = 4
# Lo @stable ICU 2.0
GC_OTHER_LETTER = 5
# Mn @stable ICU 2.0
GC_NON_SPACING_MARK = 6
# Me @stable ICU 2.0
GC_ENCLOSING_MARK = 7
# Mc @stable ICU 2.0
GC_COMBINING_SPACING_MARK = 8
# Nd @stable ICU 2.0
GC_DECIMAL_DIGIT_NUMBER = 9
# Nl @stable ICU 2.0
GC_LETTER_NUMBER = 10
# No @stable ICU 2.0
GC_OTHER_NUMBER = 11
# Zs @stable ICU 2.0
GC_SPACE_SEPARATOR = 12
# Zl @stable ICU 2.0
GC_LINE_SEPARATOR = 13
# Zp @stable ICU 2.0
GC_PARAGRAPH_SEPARATOR = 14
# Cc @stable ICU 2.0
GC_CONTROL_CHAR = 15
# Cf @stable ICU 2.0
GC_FORMAT_CHAR = 16
# Co @stable ICU 2.0
GC_PRIVATE_USE_CHAR = 17
# Cs @stable ICU 2.0
GC_SURROGATE = 18
# Pd @stable ICU 2.0
GC_DASH_PUNCTUATION = 19
# Ps @stable ICU 2.0
GC_START_PUNCTUATION = 20
# Pe @stable ICU 2.0
GC_END_PUNCTUATION = 21
# Pc @stable ICU 2.0
GC_CONNECTOR_PUNCTUATION = 22
# Po @stable ICU 2.0
GC_OTHER_PUNCTUATION = 23
# Sm @stable ICU 2.0
GC_MATH_SYMBOL = 24
# Sc @stable ICU 2.0
GC_CURRENCY_SYMBOL = 25
# Sk @stable ICU 2.0
GC_MODIFIER_SYMBOL = 26
# So @stable ICU 2.0
GC_OTHER_SYMBOL = 27
# Pi @stable ICU 2.0
GC_INITIAL_PUNCTUATION = 28
# Pf @stable ICU 2.0
GC_FINAL_PUNCTUATION = 29

GC_CATEFORY_COUNT = 30

# GC_XX_MASK constants are bit flags corresponding to Unicode
# general category values.
# For each category, the nth bit is set if the numeric value of the
# corresponding UCharCategory constant is n.
#
# There are also some GC_Y_MASK constants for groups of general categories
# like L for all letter categories.

GC_CN_MASK = 1 << GC_GENERAL_OTHER_TYPES

#  Mask constant for a UCharCategory. @stable ICU 2.1
GC_LU_MASK = 1 << GC_UPPERCASE_LETTER
#  Mask constant for a UCharCategory. @stable ICU 2.1
GC_LL_MASK = 1 << GC_LOWERCASE_LETTER
#  Mask constant for a UCharCategory. @stable ICU 2.1
GC_LT_MASK = 1 << GC_TITLECASE_LETTER
#  Mask constant for a UCharCategory. @stable ICU 2.1
GC_LM_MASK = 1 << GC_MODIFIER_LETTER
#  Mask constant for a UCharCategory. @stable ICU 2.1
GC_LO_MASK = 1 << GC_OTHER_LETTER

#  Mask constant for a UCharCategory. @stable ICU 2.1
GC_MN_MASK = 1 << GC_NON_SPACING_MARK
#  Mask constant for a UCharCategory. @stable ICU 2.1
GC_ME_MASK = 1 << GC_ENCLOSING_MARK
#  Mask constant for a UCharCategory. @stable ICU 2.1
GC_MC_MASK = 1 << GC_COMBINING_SPACING_MARK

#  Mask constant for a UCharCategory. @stable ICU 2.1
GC_ND_MASK = 1 << GC_DECIMAL_DIGIT_NUMBER
#  Mask constant for a UCharCategory. @stable ICU 2.1
GC_NL_MASK = 1 << GC_LETTER_NUMBER
#  Mask constant for a UCharCategory. @stable ICU 2.1
GC_NO_MASK = 1 << GC_OTHER_NUMBER

#  Mask constant for a UCharCategory. @stable ICU 2.1
GC_ZS_MASK = 1 << GC_SPACE_SEPARATOR
#  Mask constant for a UCharCategory. @stable ICU 2.1
GC_ZL_MASK = 1 << GC_LINE_SEPARATOR
#  Mask constant for a UCharCategory. @stable ICU 2.1
GC_ZP_MASK = 1 << GC_PARAGRAPH_SEPARATOR

#  Mask constant for a UCharCategory. @stable ICU 2.1
GC_CC_MASK = 1 << GC_CONTROL_CHAR
#  Mask constant for a UCharCategory. @stable ICU 2.1
GC_CF_MASK = 1 << GC_FORMAT_CHAR
#  Mask constant for a UCharCategory. @stable ICU 2.1
GC_CO_MASK = 1 << GC_PRIVATE_USE_CHAR
#  Mask constant for a UCharCategory. @stable ICU 2.1
GC_CS_MASK = 1 << GC_SURROGATE

#  Mask constant for a UCharCategory. @stable ICU 2.1
GC_PD_MASK = 1 << GC_DASH_PUNCTUATION
#  Mask constant for a UCharCategory. @stable ICU 2.1
GC_PS_MASK = 1 << GC_START_PUNCTUATION
#  Mask constant for a UCharCategory. @stable ICU 2.1
GC_PE_MASK = 1 << GC_END_PUNCTUATION
#  Mask constant for a UCharCategory. @stable ICU 2.1
GC_PC_MASK = 1 << GC_CONNECTOR_PUNCTUATION
#  Mask constant for a UCharCategory. @stable ICU 2.1
GC_PO_MASK = 1 << GC_OTHER_PUNCTUATION

#  Mask constant for a UCharCategory. @stable ICU 2.1
GC_SM_MASK = 1 << GC_MATH_SYMBOL
#  Mask constant for a UCharCategory. @stable ICU 2.1
GC_SC_MASK = 1 << GC_CURRENCY_SYMBOL
#  Mask constant for a UCharCategory. @stable ICU 2.1
GC_SK_MASK = 1 << GC_MODIFIER_SYMBOL
#  Mask constant for a UCharCategory. @stable ICU 2.1
GC_SO_MASK = 1 << GC_OTHER_SYMBOL

#  Mask constant for a UCharCategory. @stable ICU 2.1
GC_PI_MASK = 1 << GC_INITIAL_PUNCTUATION
#  Mask constant for a UCharCategory. @stable ICU 2.1
GC_PF_MASK = 1 << GC_FINAL_PUNCTUATION


#  Mask constant for multiple UCharCategory bits (L Letters). @stable ICU 2.1
GC_L_MASK = (GC_LU_MASK|GC_LL_MASK|GC_LT_MASK|GC_LM_MASK|GC_LO_MASK)

#  Mask constant for multiple UCharCategory bits (LC Cased Letters). @stable ICU 2.1
GC_LC_MASK = (GC_LU_MASK|GC_LL_MASK|GC_LT_MASK)

#  Mask constant for multiple UCharCategory bits (M Marks). @stable ICU 2.1
GC_M_MASK = (GC_MN_MASK|GC_ME_MASK|GC_MC_MASK)

#  Mask constant for multiple UCharCategory bits (N Numbers). @stable ICU 2.1
GC_N_MASK = (GC_ND_MASK|GC_NL_MASK|GC_NO_MASK)

#  Mask constant for multiple UCharCategory bits (Z Separators). @stable ICU 2.1
GC_Z_MASK = (GC_ZS_MASK|GC_ZL_MASK|GC_ZP_MASK)

#  Mask constant for multiple UCharCategory bits (C Others). @stable ICU 2.1
GC_C_MASK = (GC_CN_MASK|GC_CC_MASK|GC_CF_MASK|GC_CO_MASK|GC_CS_MASK)

#  Mask constant for multiple UCharCategory bits (P Punctuation). @stable ICU 2.1
GC_P_MASK = (GC_PD_MASK|GC_PS_MASK|GC_PE_MASK|GC_PC_MASK|GC_PO_MASK|GC_PI_MASK|GC_PF_MASK)

#  Mask constant for multiple UCharCategory bits (S Symbols). @stable ICU 2.1
GC_S_MASK = (GC_SM_MASK|GC_SC_MASK|GC_SK_MASK|GC_SO_MASK)

generalCategories = {
    GC_GENERAL_OTHER_TYPES: 'Cn',
    GC_UPPERCASE_LETTER: 'Lu',
    GC_LOWERCASE_LETTER: 'Ll',
    GC_TITLECASE_LETTER: 'Lt',
    GC_MODIFIER_LETTER: 'Lm',
    GC_OTHER_LETTER: 'Lo',
    GC_NON_SPACING_MARK: 'Mn',
    GC_ENCLOSING_MARK: 'Me',
    GC_COMBINING_SPACING_MARK: 'Mc',
    GC_DECIMAL_DIGIT_NUMBER: 'Nd',
    GC_LETTER_NUMBER: 'Nl',
    GC_OTHER_NUMBER: 'No',
    GC_SPACE_SEPARATOR: 'Zs',
    GC_LINE_SEPARATOR: 'Zl',
    GC_PARAGRAPH_SEPARATOR: 'Zp',
    GC_CONTROL_CHAR: 'Cc',
    GC_FORMAT_CHAR: 'Cf',
    GC_PRIVATE_USE_CHAR: 'Co',
    GC_SURROGATE: 'Cs',
    GC_DASH_PUNCTUATION: 'Pd',
    GC_START_PUNCTUATION: 'Ps',
    GC_END_PUNCTUATION: 'Pe',
    GC_CONNECTOR_PUNCTUATION: 'Pc',
    GC_OTHER_PUNCTUATION: 'Po',
    GC_MATH_SYMBOL: 'Sm',
    GC_CURRENCY_SYMBOL: 'Sc',
    GC_MODIFIER_SYMBOL: 'Sk',
    GC_OTHER_SYMBOL: 'So',
    GC_INITIAL_PUNCTUATION: 'Pi',
    GC_FINAL_PUNCTUATION: 'Pf'
}
