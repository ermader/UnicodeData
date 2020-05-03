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
