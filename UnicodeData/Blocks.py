"""\
Based on UBlockCode from uchar.h in ICU

Created on May 4, 2020

@author Eric Mader
"""

UBLOCK_NO_BLOCK = 0  # [none] Special range indicating No_Block

# @stable ICU 2.0
UBLOCK_BASIC_LATIN = 1  # [0000]

# @stable ICU 2.0
UBLOCK_LATIN_1_SUPPLEMENT = 2  # [0080]

# @stable ICU 2.0
UBLOCK_LATIN_EXTENDED_A = 3  # [0100]

# @stable ICU 2.0
UBLOCK_LATIN_EXTENDED_B = 4  # [0180]

# @stable ICU 2.0
UBLOCK_IPA_EXTENSIONS = 5  # [0250]

# @stable ICU 2.0
UBLOCK_SPACING_MODIFIER_LETTERS = 6  # [02B0]

# @stable ICU 2.0
UBLOCK_COMBINING_DIACRITICAL_MARKS = 7  # [0300]

# Unicode 3.2 renames this block to "Greek and Coptic".
# @ stable ICU 2.0

UBLOCK_GREEK = 8  # [0370]

# @stable ICU 2.0
UBLOCK_CYRILLIC = 9  # [0400]

# @stable ICU 2.0
UBLOCK_ARMENIAN = 10  # [0530]

# @stable ICU 2.0
UBLOCK_HEBREW = 11  # [0590]

# @stable ICU 2.0
UBLOCK_ARABIC = 12  # [0600]

# @stable ICU 2.0
UBLOCK_SYRIAC = 13  # [0700]

# @stable ICU 2.0
UBLOCK_THAANA = 14  # [0780]

# @stable ICU 2.0
UBLOCK_DEVANAGARI = 15  # [0900]

# @stable ICU 2.0
UBLOCK_BENGALI = 16  # [0980]

# @stable ICU 2.0
UBLOCK_GURMUKHI = 17  # [0A00]

# @stable ICU 2.0
UBLOCK_GUJARATI = 18  # [0A80]

# @stable ICU 2.0
UBLOCK_ORIYA = 19  # [0B00]

# @stable ICU 2.0
UBLOCK_TAMIL = 20  # [0B80]

# @stable ICU 2.0
UBLOCK_TELUGU = 21  # [0C00]

# @stable ICU 2.0
UBLOCK_KANNADA = 22  # [0C80]

# @stable ICU 2.0
UBLOCK_MALAYALAM = 23  # [0D00]

# @stable ICU 2.0
UBLOCK_SINHALA = 24  # [0D80]

# @stable ICU 2.0
UBLOCK_THAI = 25  # [0E00]

# @stable ICU 2.0
UBLOCK_LAO = 26  # [0E80]

# @stable ICU 2.0
UBLOCK_TIBETAN = 27  # [0F00]

# @stable ICU 2.0
UBLOCK_MYANMAR = 28  # [1000]

# @stable ICU 2.0
UBLOCK_GEORGIAN = 29  # [10A0]

# @stable ICU 2.0
UBLOCK_HANGUL_JAMO = 30  # [1100]

# @stable ICU 2.0
UBLOCK_ETHIOPIC = 31  # [1200]

# @stable ICU 2.0
UBLOCK_CHEROKEE = 32  # [13A0]

# @stable ICU 2.0
UBLOCK_UNIFIED_CANADIAN_ABORIGINAL_SYLLABICS = 33  # [1400]

# @stable ICU 2.0
UBLOCK_OGHAM = 34  # [1680]

# @stable ICU 2.0
UBLOCK_RUNIC = 35  # [16A0]

# @stable ICU 2.0
UBLOCK_KHMER = 36  # [1780]

# @stable ICU 2.0
UBLOCK_MONGOLIAN = 37  # [1800]

# @stable ICU 2.0
UBLOCK_LATIN_EXTENDED_ADDITIONAL = 38  # [1E00]

# @stable ICU 2.0
UBLOCK_GREEK_EXTENDED = 39  # [1F00]

# @stable ICU 2.0
UBLOCK_GENERAL_PUNCTUATION = 40  # [2000]

# @stable ICU 2.0
UBLOCK_SUPERSCRIPTS_AND_SUBSCRIPTS = 41  # [2070]

# @stable ICU 2.0
UBLOCK_CURRENCY_SYMBOLS = 42  # [20A0]

# Unicode 3.2 renames this block to "Diacriticals for Symbols".
# @ stable ICU 2.0

UBLOCK_COMBINING_MARKS_FOR_SYMBOLS = 43  # [20D0]

# @stable ICU 2.0
UBLOCK_LETTERLIKE_SYMBOLS = 44  # [2100]

# @stable ICU 2.0
UBLOCK_NUMBER_FORMS = 45  # [2150]

# @stable ICU 2.0
UBLOCK_ARROWS = 46  # [2190]

# @stable ICU 2.0
UBLOCK_MATHEMATICAL_OPERATORS = 47  # [2200]

# @stable ICU 2.0
UBLOCK_MISCELLANEOUS_TECHNICAL = 48  # [2300]

# @stable ICU 2.0
UBLOCK_CONTROL_PICTURES = 49  # [2400]

# @stable ICU 2.0
UBLOCK_OPTICAL_CHARACTER_RECOGNITION = 50  # [2440]

# @stable ICU 2.0
UBLOCK_ENCLOSED_ALPHANUMERICS = 51  # [2460]

# @stable ICU 2.0
UBLOCK_BOX_DRAWING = 52  # [2500]

# @stable ICU 2.0
UBLOCK_BLOCK_ELEMENTS = 53  # [2580]

# @stable ICU 2.0
UBLOCK_GEOMETRIC_SHAPES = 54  # [25A0]

# @stable ICU 2.0
UBLOCK_MISCELLANEOUS_SYMBOLS = 55  # [2600]

# @stable ICU 2.0
UBLOCK_DINGBATS = 56  # [2700]

# @stable ICU 2.0
UBLOCK_BRAILLE_PATTERNS = 57  # [2800]

# @stable ICU 2.0
UBLOCK_CJK_RADICALS_SUPPLEMENT = 58  # [2E80]

# @stable ICU 2.0
UBLOCK_KANGXI_RADICALS = 59  # [2F00]

# @stable ICU 2.0
UBLOCK_IDEOGRAPHIC_DESCRIPTION_CHARACTERS = 60  # [2FF0]

# @stable ICU 2.0
UBLOCK_CJK_SYMBOLS_AND_PUNCTUATION = 61  # [3000]

# @stable ICU 2.0
UBLOCK_HIRAGANA = 62  # [3040]

# @stable ICU 2.0
UBLOCK_KATAKANA = 63  # [30A0]

# @stable ICU 2.0
UBLOCK_BOPOMOFO = 64  # [3100]

# @stable ICU 2.0
UBLOCK_HANGUL_COMPATIBILITY_JAMO = 65  # [3130]

# @stable ICU 2.0
UBLOCK_KANBUN = 66  # [3190]

# @stable ICU 2.0
UBLOCK_BOPOMOFO_EXTENDED = 67  # [31A0]

# @stable ICU 2.0
UBLOCK_ENCLOSED_CJK_LETTERS_AND_MONTHS = 68  # [3200]

# @stable ICU 2.0
UBLOCK_CJK_COMPATIBILITY = 69  # [3300]

# @stable ICU 2.0
UBLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_A = 70  # [3400]

# @stable ICU 2.0
UBLOCK_CJK_UNIFIED_IDEOGRAPHS = 71  # [4E00]

# @stable ICU 2.0
UBLOCK_YI_SYLLABLES = 72  # [A000]

# @stable ICU 2.0
UBLOCK_YI_RADICALS = 73  # [A490]

# @stable ICU 2.0
UBLOCK_HANGUL_SYLLABLES = 74  # [AC00]

# @stable ICU 2.0
UBLOCK_HIGH_SURROGATES = 75  # [D800]

# @stable ICU 2.0
UBLOCK_HIGH_PRIVATE_USE_SURROGATES = 76  # [DB80]

# @stable ICU 2.0
UBLOCK_LOW_SURROGATES = 77  # [DC00]

# Same as UBLOCK_PRIVATE_USE.
# Until Unicode 3.1.1, the corresponding block name was "Private Use",
# and multiple code point ranges had this block.
# *Unicode 3.2 renames the block for the BMP PUA to "Private Use Area" and
# adds eparate blocks
#
# @ stable ICU 2.0

UBLOCK_PRIVATE_USE_AREA = 78  # [E000]
#
# Same as UBLOCK_PRIVATE_USE_AREA.
# Until Unicode 3.1.1, the corresponding block name was "Private Use",
# and multiple code point ranges had this block.
# Unicode 3.2 renames the block for the BMP PUA to "Private Use Area" and
# adds separate blocks for the supplementary PUAs.
#
#* @ stable ICU 2.0

UBLOCK_PRIVATE_USE = UBLOCK_PRIVATE_USE_AREA,

# @stable ICU 2.0
UBLOCK_CJK_COMPATIBILITY_IDEOGRAPHS = 79  # [F900]

# @stable ICU 2.0
UBLOCK_ALPHABETIC_PRESENTATION_FORMS = 80  # [FB00]

# @stable ICU 2.0
UBLOCK_ARABIC_PRESENTATION_FORMS_A = 81  # [FB50]

# @stable ICU 2.0
UBLOCK_COMBINING_HALF_MARKS = 82  # [FE20]

# @stable ICU 2.0
UBLOCK_CJK_COMPATIBILITY_FORMS = 83  # [FE30]

# @stable ICU 2.0
UBLOCK_SMALL_FORM_VARIANTS = 84  # [FE50]

# @stable ICU 2.0
UBLOCK_ARABIC_PRESENTATION_FORMS_B = 85  # [FE70]

# @stable ICU 2.0
UBLOCK_SPECIALS = 86  # [FFF0]

# @stable ICU 2.0
UBLOCK_HALFWIDTH_AND_FULLWIDTH_FORMS = 87  # [FF00]

#  New blocks in Unicode 3.1

# @stable ICU 2.0
UBLOCK_OLD_ITALIC = 88  # [10300]
# @stable ICU 2.0
UBLOCK_GOTHIC = 89  # [10330]
# @stable ICU 2.0
UBLOCK_DESERET = 90  # [10400]
# @stable ICU 2.0
UBLOCK_BYZANTINE_MUSICAL_SYMBOLS = 91  # [1D000]
# @stable ICU 2.0
UBLOCK_MUSICAL_SYMBOLS = 92  # [1D100]
# @stable ICU 2.0
UBLOCK_MATHEMATICAL_ALPHANUMERIC_SYMBOLS = 93  # [1D400]
# @stable ICU 2.0
UBLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_B = 94  # [20000]
# @stable ICU 2.0
UBLOCK_CJK_COMPATIBILITY_IDEOGRAPHS_SUPPLEMENT = 95  # [2F800]
# @stable ICU 2.0
UBLOCK_TAGS = 96  # [E0000]

#  New blocks in Unicode 3.2

# @stable ICU 3.0
UBLOCK_CYRILLIC_SUPPLEMENT = 97  # [0500]
#
# Unicode 4.0.1 renames the "Cyrillic Supary" block to "Cyrillic Sup".
# @ stable ICU 2.2

UBLOCK_CYRILLIC_SUPPLEMENTARY = UBLOCK_CYRILLIC_SUPPLEMENT,
# @stable ICU 2.2
UBLOCK_TAGALOG = 98  # [1700]
# @stable ICU 2.2
UBLOCK_HANUNOO = 99  # [1720]
# @stable ICU 2.2
UBLOCK_BUHID = 100  # [1740]
# @stable ICU 2.2
UBLOCK_TAGBANWA = 101  # [1760]
# @stable ICU 2.2
UBLOCK_MISCELLANEOUS_MATHEMATICAL_SYMBOLS_A = 102  # [27C0]
# @stable ICU 2.2
UBLOCK_SUPPLEMENTAL_ARROWS_A = 103  # [27F0]
# @stable ICU 2.2
UBLOCK_SUPPLEMENTAL_ARROWS_B = 104  # [2900]
# @stable ICU 2.2
UBLOCK_MISCELLANEOUS_MATHEMATICAL_SYMBOLS_B = 105  # [2980]
# @stable ICU 2.2
UBLOCK_SUPPLEMENTAL_MATHEMATICAL_OPERATORS = 106  # [2A00]
# @stable ICU 2.2
UBLOCK_KATAKANA_PHONETIC_EXTENSIONS = 107  # [31F0]
# @stable ICU 2.2
UBLOCK_VARIATION_SELECTORS = 108  # [FE00]
# @stable ICU 2.2
UBLOCK_SUPPLEMENTARY_PRIVATE_USE_AREA_A = 109  # [F0000]
# @stable ICU 2.2
UBLOCK_SUPPLEMENTARY_PRIVATE_USE_AREA_B = 110  # [100000]

#  New blocks in Unicode 4

# @stable ICU 2.6
UBLOCK_LIMBU = 111  # [1900]
# @stable ICU 2.6
UBLOCK_TAI_LE = 112  # [1950]
# @stable ICU 2.6
UBLOCK_KHMER_SYMBOLS = 113  # [19E0]
# @stable ICU 2.6
UBLOCK_PHONETIC_EXTENSIONS = 114  # [1D00]
# @stable ICU 2.6
UBLOCK_MISCELLANEOUS_SYMBOLS_AND_ARROWS = 115  # [2B00]
# @stable ICU 2.6
UBLOCK_YIJING_HEXAGRAM_SYMBOLS = 116  # [4DC0]
# @stable ICU 2.6
UBLOCK_LINEAR_B_SYLLABARY = 117  # [10000]
# @stable ICU 2.6
UBLOCK_LINEAR_B_IDEOGRAMS = 118  # [10080]
# @stable ICU 2.6
UBLOCK_AEGEAN_NUMBERS = 119  # [10100]
# @stable ICU 2.6
UBLOCK_UGARITIC = 120  # [10380]
# @stable ICU 2.6
UBLOCK_SHAVIAN = 121  # [10450]
# @stable ICU 2.6
UBLOCK_OSMANYA = 122  # [10480]
# @stable ICU 2.6
UBLOCK_CYPRIOT_SYLLABARY = 123  # [10800]
# @stable ICU 2.6
UBLOCK_TAI_XUAN_JING_SYMBOLS = 124  # [1D300]
# @stable ICU 2.6
UBLOCK_VARIATION_SELECTORS_SUPPLEMENT = 125  # [E0100]

#  New blocks in Unicode 4.1

# @stable ICU 3.4
UBLOCK_ANCIENT_GREEK_MUSICAL_NOTATION = 126  # [1D200]
# @stable ICU 3.4
UBLOCK_ANCIENT_GREEK_NUMBERS = 127  # [10140]
# @stable ICU 3.4
UBLOCK_ARABIC_SUPPLEMENT = 128  # [0750]
# @stable ICU 3.4
UBLOCK_BUGINESE = 129  # [1A00]
# @stable ICU 3.4
UBLOCK_CJK_STROKES = 130  # [31C0]
# @stable ICU 3.4
UBLOCK_COMBINING_DIACRITICAL_MARKS_SUPPLEMENT = 131  # [1DC0]
# @stable ICU 3.4
UBLOCK_COPTIC = 132  # [2C80]
# @stable ICU 3.4
UBLOCK_ETHIOPIC_EXTENDED = 133  # [2D80]
# @stable ICU 3.4
UBLOCK_ETHIOPIC_SUPPLEMENT = 134  # [1380]
# @stable ICU 3.4
UBLOCK_GEORGIAN_SUPPLEMENT = 135  # [2D00]
# @stable ICU 3.4
UBLOCK_GLAGOLITIC = 136  # [2C00]
# @stable ICU 3.4
UBLOCK_KHAROSHTHI = 137  # [10A00]
# @stable ICU 3.4
UBLOCK_MODIFIER_TONE_LETTERS = 138  # [A700]
# @stable ICU 3.4
UBLOCK_NEW_TAI_LUE = 139  # [1980]
# @stable ICU 3.4
UBLOCK_OLD_PERSIAN = 140  # [103A0]
# @stable ICU 3.4
UBLOCK_PHONETIC_EXTENSIONS_SUPPLEMENT = 141  # [1D80]
# @stable ICU 3.4
UBLOCK_SUPPLEMENTAL_PUNCTUATION = 142  # [2E00]
# @stable ICU 3.4
UBLOCK_SYLOTI_NAGRI = 143  # [A800]
# @stable ICU 3.4
UBLOCK_TIFINAGH = 144  # [2D30]
# @stable ICU 3.4
UBLOCK_VERTICAL_FORMS = 145  # [FE10]

#  New blocks in Unicode 5.0

# @stable ICU 3.6
UBLOCK_NKO = 146  # [07C0]
# @stable ICU 3.6
UBLOCK_BALINESE = 147  # [1B00]
# @stable ICU 3.6
UBLOCK_LATIN_EXTENDED_C = 148  # [2C60]
# @stable ICU 3.6
UBLOCK_LATIN_EXTENDED_D = 149  # [A720]
# @stable ICU 3.6
UBLOCK_PHAGS_PA = 150  # [A840]
# @stable ICU 3.6
UBLOCK_PHOENICIAN = 151  # [10900]
# @stable ICU 3.6
UBLOCK_CUNEIFORM = 152  # [12000]
# @stable ICU 3.6
UBLOCK_CUNEIFORM_NUMBERS_AND_PUNCTUATION = 153  # [12400]
# @stable ICU 3.6
UBLOCK_COUNTING_ROD_NUMERALS = 154  # [1D360]

#  New blocks in Unicode 5.1

# @stable ICU 4.0
UBLOCK_SUNDANESE = 155  # [1B80]
# @stable ICU 4.0
UBLOCK_LEPCHA = 156  # [1C00]
# @stable ICU 4.0
UBLOCK_OL_CHIKI = 157  # [1C50]
# @stable ICU 4.0
UBLOCK_CYRILLIC_EXTENDED_A = 158  # [2DE0]
# @stable ICU 4.0
UBLOCK_VAI = 159  # [A500]
# @stable ICU 4.0
UBLOCK_CYRILLIC_EXTENDED_B = 160  # [A640]
# @stable ICU 4.0
UBLOCK_SAURASHTRA = 161  # [A880]
# @stable ICU 4.0
UBLOCK_KAYAH_LI = 162  # [A900]
# @stable ICU 4.0
UBLOCK_REJANG = 163  # [A930]
# @stable ICU 4.0
UBLOCK_CHAM = 164  # [AA00]
# @stable ICU 4.0
UBLOCK_ANCIENT_SYMBOLS = 165  # [10190]
# @stable ICU 4.0
UBLOCK_PHAISTOS_DISC = 166  # [101D0]
# @stable ICU 4.0
UBLOCK_LYCIAN = 167  # [10280]
# @stable ICU 4.0
UBLOCK_CARIAN = 168  # [102A0]
# @stable ICU 4.0
UBLOCK_LYDIAN = 169  # [10920]
# @stable ICU 4.0
UBLOCK_MAHJONG_TILES = 170  # [1F000]
# @stable ICU 4.0
UBLOCK_DOMINO_TILES = 171  # [1F030]

#  New blocks in Unicode 5.2

# @stable ICU 4.4
UBLOCK_SAMARITAN = 172  # [0800]
# @stable ICU 4.4
UBLOCK_UNIFIED_CANADIAN_ABORIGINAL_SYLLABICS_EXTENDED = 173  # [18B0]
# @stable ICU 4.4
UBLOCK_TAI_THAM = 174  # [1A20]
# @stable ICU 4.4
UBLOCK_VEDIC_EXTENSIONS = 175  # [1CD0]
# @stable ICU 4.4
UBLOCK_LISU = 176  # [A4D0]
# @stable ICU 4.4
UBLOCK_BAMUM = 177  # [A6A0]
# @stable ICU 4.4
UBLOCK_COMMON_INDIC_NUMBER_FORMS = 178  # [A830]
# @stable ICU 4.4
UBLOCK_DEVANAGARI_EXTENDED = 179  # [A8E0]
# @stable ICU 4.4
UBLOCK_HANGUL_JAMO_EXTENDED_A = 180  # [A960]
# @stable ICU 4.4
UBLOCK_JAVANESE = 181  # [A980]
# @stable ICU 4.4
UBLOCK_MYANMAR_EXTENDED_A = 182  # [AA60]
# @stable ICU 4.4
UBLOCK_TAI_VIET = 183  # [AA80]
# @stable ICU 4.4
UBLOCK_MEETEI_MAYEK = 184  # [ABC0]
# @stable ICU 4.4
UBLOCK_HANGUL_JAMO_EXTENDED_B = 185  # [D7B0]
# @stable ICU 4.4
UBLOCK_IMPERIAL_ARAMAIC = 186  # [10840]
# @stable ICU 4.4
UBLOCK_OLD_SOUTH_ARABIAN = 187  # [10A60]
# @stable ICU 4.4
UBLOCK_AVESTAN = 188  # [10B00]
# @stable ICU 4.4
UBLOCK_INSCRIPTIONAL_PARTHIAN = 189  # [10B40]
# @stable ICU 4.4
UBLOCK_INSCRIPTIONAL_PAHLAVI = 190  # [10B60]
# @stable ICU 4.4
UBLOCK_OLD_TURKIC = 191  # [10C00]
# @stable ICU 4.4
UBLOCK_RUMI_NUMERAL_SYMBOLS = 192  # [10E60]
# @stable ICU 4.4
UBLOCK_KAITHI = 193  # [11080]
# @stable ICU 4.4
UBLOCK_EGYPTIAN_HIEROGLYPHS = 194  # [13000]
# @stable ICU 4.4
UBLOCK_ENCLOSED_ALPHANUMERIC_SUPPLEMENT = 195  # [1F100]
# @stable ICU 4.4
UBLOCK_ENCLOSED_IDEOGRAPHIC_SUPPLEMENT = 196  # [1F200]
# @stable ICU 4.4
UBLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_C = 197  # [2A700]

#  New blocks in Unicode 6.0

# @stable ICU 4.6
UBLOCK_MANDAIC = 198  # [0840]
# @stable ICU 4.6
UBLOCK_BATAK = 199  # [1BC0]
# @stable ICU 4.6
UBLOCK_ETHIOPIC_EXTENDED_A = 200  # [AB00]
# @stable ICU 4.6
UBLOCK_BRAHMI = 201  # [11000]
# @stable ICU 4.6
UBLOCK_BAMUM_SUPPLEMENT = 202  # [16800]
# @stable ICU 4.6
UBLOCK_KANA_SUPPLEMENT = 203  # [1B000]
# @stable ICU 4.6
UBLOCK_PLAYING_CARDS = 204  # [1F0A0]
# @stable ICU 4.6
UBLOCK_MISCELLANEOUS_SYMBOLS_AND_PICTOGRAPHS = 205  # [1F300]
# @stable ICU 4.6
UBLOCK_EMOTICONS = 206  # [1F600]
# @stable ICU 4.6
UBLOCK_TRANSPORT_AND_MAP_SYMBOLS = 207  # [1F680]
# @stable ICU 4.6
UBLOCK_ALCHEMICAL_SYMBOLS = 208  # [1F700]
# @stable ICU 4.6
UBLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_D = 209  # [2B740]

#  New blocks in Unicode 6.1

# @stable ICU 49
UBLOCK_ARABIC_EXTENDED_A = 210  # [08A0]
# @stable ICU 49
UBLOCK_ARABIC_MATHEMATICAL_ALPHABETIC_SYMBOLS = 211  # [1EE00]
# @stable ICU 49
UBLOCK_CHAKMA = 212  # [11100]
# @stable ICU 49
UBLOCK_MEETEI_MAYEK_EXTENSIONS = 213  # [AAE0]
# @stable ICU 49
UBLOCK_MEROITIC_CURSIVE = 214  # [109A0]
# @stable ICU 49
UBLOCK_MEROITIC_HIEROGLYPHS = 215  # [10980]
# @stable ICU 49
UBLOCK_MIAO = 216  # [16F00]
# @stable ICU 49
UBLOCK_SHARADA = 217  # [11180]
# @stable ICU 49
UBLOCK_SORA_SOMPENG = 218  # [110D0]
# @stable ICU 49
UBLOCK_SUNDANESE_SUPPLEMENT = 219  # [1CC0]
# @stable ICU 49
UBLOCK_TAKRI = 220  # [11680]

#  New blocks in Unicode 7.0

# @stable ICU 54
UBLOCK_BASSA_VAH = 221  # [16AD0]
# @stable ICU 54
UBLOCK_CAUCASIAN_ALBANIAN = 222  # [10530]
# @stable ICU 54
UBLOCK_COPTIC_EPACT_NUMBERS = 223  # [102E0]
# @stable ICU 54
UBLOCK_COMBINING_DIACRITICAL_MARKS_EXTENDED = 224  # [1AB0]
# @stable ICU 54
UBLOCK_DUPLOYAN = 225  # [1BC00]
# @stable ICU 54
UBLOCK_ELBASAN = 226  # [10500]
# @stable ICU 54
UBLOCK_GEOMETRIC_SHAPES_EXTENDED = 227  # [1F780]
# @stable ICU 54
UBLOCK_GRANTHA = 228  # [11300]
# @stable ICU 54
UBLOCK_KHOJKI = 229  # [11200]
# @stable ICU 54
UBLOCK_KHUDAWADI = 230  # [112B0]
# @stable ICU 54
UBLOCK_LATIN_EXTENDED_E = 231  # [AB30]
# @stable ICU 54
UBLOCK_LINEAR_A = 232  # [10600]
# @stable ICU 54
UBLOCK_MAHAJANI = 233  # [11150]
# @stable ICU 54
UBLOCK_MANICHAEAN = 234  # [10AC0]
# @stable ICU 54
UBLOCK_MENDE_KIKAKUI = 235  # [1E800]
# @stable ICU 54
UBLOCK_MODI = 236  # [11600]
# @stable ICU 54
UBLOCK_MRO = 237  # [16A40]
# @stable ICU 54
UBLOCK_MYANMAR_EXTENDED_B = 238  # [A9E0]
# @stable ICU 54
UBLOCK_NABATAEAN = 239  # [10880]
# @stable ICU 54
UBLOCK_OLD_NORTH_ARABIAN = 240  # [10A80]
# @stable ICU 54
UBLOCK_OLD_PERMIC = 241  # [10350]
# @stable ICU 54
UBLOCK_ORNAMENTAL_DINGBATS = 242  # [1F650]
# @stable ICU 54
UBLOCK_PAHAWH_HMONG = 243  # [16B00]
# @stable ICU 54
UBLOCK_PALMYRENE = 244  # [10860]
# @stable ICU 54
UBLOCK_PAU_CIN_HAU = 245  # [11AC0]
# @stable ICU 54
UBLOCK_PSALTER_PAHLAVI = 246  # [10B80]
# @stable ICU 54
UBLOCK_SHORTHAND_FORMAT_CONTROLS = 247  # [1BCA0]
# @stable ICU 54
UBLOCK_SIDDHAM = 248  # [11580]
# @stable ICU 54
UBLOCK_SINHALA_ARCHAIC_NUMBERS = 249  # [111E0]
# @stable ICU 54
UBLOCK_SUPPLEMENTAL_ARROWS_C = 250  # [1F800]
# @stable ICU 54
UBLOCK_TIRHUTA = 251  # [11480]
# @stable ICU 54
UBLOCK_WARANG_CITI = 252  # [118A0]

#  New blocks in Unicode 8.0

# @stable ICU 56
UBLOCK_AHOM = 253  # [11700]
# @stable ICU 56
UBLOCK_ANATOLIAN_HIEROGLYPHS = 254  # [14400]
# @stable ICU 56
UBLOCK_CHEROKEE_SUPPLEMENT = 255  # [AB70]
# @stable ICU 56
UBLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_E = 256  # [2B820]
# @stable ICU 56
UBLOCK_EARLY_DYNASTIC_CUNEIFORM = 257  # [12480]
# @stable ICU 56
UBLOCK_HATRAN = 258  # [108E0]
# @stable ICU 56
UBLOCK_MULTANI = 259  # [11280]
# @stable ICU 56
UBLOCK_OLD_HUNGARIAN = 260  # [10C80]
# @stable ICU 56
UBLOCK_SUPPLEMENTAL_SYMBOLS_AND_PICTOGRAPHS = 261  # [1F900]
# @stable ICU 56
UBLOCK_SUTTON_SIGNWRITING = 262  # [1D800]

#  New blocks in Unicode 9.0

# @stable ICU 58
UBLOCK_ADLAM = 263  # [1E900]
# @stable ICU 58
UBLOCK_BHAIKSUKI = 264  # [11C00]
# @stable ICU 58
UBLOCK_CYRILLIC_EXTENDED_C = 265  # [1C80]
# @stable ICU 58
UBLOCK_GLAGOLITIC_SUPPLEMENT = 266  # [1E000]
# @stable ICU 58
UBLOCK_IDEOGRAPHIC_SYMBOLS_AND_PUNCTUATION = 267  # [16FE0]
# @stable ICU 58
UBLOCK_MARCHEN = 268  # [11C70]
# @stable ICU 58
UBLOCK_MONGOLIAN_SUPPLEMENT = 269  # [11660]
# @stable ICU 58
UBLOCK_NEWA = 270  # [11400]
# @stable ICU 58
UBLOCK_OSAGE = 271  # [104B0]
# @stable ICU 58
UBLOCK_TANGUT = 272  # [17000]
# @stable ICU 58
UBLOCK_TANGUT_COMPONENTS = 273  # [18800]

# New blocks in Unicode 10.0

# @stable ICU 60
UBLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_F = 274  # [2CEB0]
# @stable ICU 60
UBLOCK_KANA_EXTENDED_A = 275  # [1B100]
# @stable ICU 60
UBLOCK_MASARAM_GONDI = 276  # [11D00]
# @stable ICU 60
UBLOCK_NUSHU = 277  # [1B170]
# @stable ICU 60
UBLOCK_SOYOMBO = 278  # [11A50]
# @stable ICU 60
UBLOCK_SYRIAC_SUPPLEMENT = 279  # [0860]
# @stable ICU 60
UBLOCK_ZANABAZAR_SQUARE = 280  # [11A00]

# New blocks in Unicode 11.0

# @stable ICU 62
UBLOCK_CHESS_SYMBOLS = 281  # [1FA00]
# @stable ICU 62
UBLOCK_DOGRA = 282  # [11800]
# @stable ICU 62
UBLOCK_GEORGIAN_EXTENDED = 283  # [1C90]
# @stable ICU 62
UBLOCK_GUNJALA_GONDI = 284  # [11D60]
# @stable ICU 62
UBLOCK_HANIFI_ROHINGYA = 285  # [10D00]
# @stable ICU 62
UBLOCK_INDIC_SIYAQ_NUMBERS = 286  # [1EC70]
# @stable ICU 62
UBLOCK_MAKASAR = 287  # [11EE0]
# @stable ICU 62
UBLOCK_MAYAN_NUMERALS = 288  # [1D2E0]
# @stable ICU 62
UBLOCK_MEDEFAIDRIN = 289  # [16E40]
# @stable ICU 62
UBLOCK_OLD_SOGDIAN = 290  # [10F00]
# @stable ICU 62
UBLOCK_SOGDIAN = 291  # [10F30]

# New blocks in Unicode 12.0

# @stable ICU 64
UBLOCK_EGYPTIAN_HIEROGLYPH_FORMAT_CONTROLS = 292  # [13430]
# @stable ICU 64
UBLOCK_ELYMAIC = 293  # [10FE0]
# @stable ICU 64
UBLOCK_NANDINAGARI = 294  # [119A0]
# @stable ICU 64
UBLOCK_NYIAKENG_PUACHUE_HMONG = 295  # [1E100]
# @stable ICU 64
UBLOCK_OTTOMAN_SIYAQ_NUMBERS = 296  # [1ED00]
# @stable ICU 64
UBLOCK_SMALL_KANA_EXTENSION = 297  # [1B130]
# @stable ICU 64
UBLOCK_SYMBOLS_AND_PICTOGRAPHS_EXTENDED_A = 298  # [1FA70]
# @stable ICU 64
UBLOCK_TAMIL_SUPPLEMENT = 299  # [11FC0]
# @stable ICU 64
UBLOCK_WANCHO = 300  # [1E2C0]

# New blocks in Unicode 13.0

# @stable ICU 66
UBLOCK_CHORASMIAN = 301  # [10FB0]
# @stable ICU 66
UBLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_G = 302  # [30000]
# @stable ICU 66
UBLOCK_DIVES_AKURU = 303  # [11900]
# @stable ICU 66
UBLOCK_KHITAN_SMALL_SCRIPT = 304  # [18B00]
# @stable ICU 66
UBLOCK_LISU_SUPPLEMENT = 305  # [11FB0]
# @stable ICU 66
UBLOCK_SYMBOLS_FOR_LEGACY_COMPUTING = 306  # [1FB00]
# @stable ICU 66
UBLOCK_TANGUT_SUPPLEMENT = 307  # [18D00]
# @stable ICU 66
UBLOCK_YEZIDI = 308  # [10E80]

blockNames = {
    UBLOCK_NO_BLOCK: "No Block",
    UBLOCK_BASIC_LATIN: "ASCII",
    UBLOCK_LATIN_1_SUPPLEMENT: "Latin 1 Sup",
    UBLOCK_LATIN_EXTENDED_A: "Latin Ext A",
    UBLOCK_LATIN_EXTENDED_B: "Latin Ext B",
    UBLOCK_IPA_EXTENSIONS: "IPA Ext",
    UBLOCK_SPACING_MODIFIER_LETTERS: "Modifier Letters",
    UBLOCK_COMBINING_DIACRITICAL_MARKS: "Diacriticals",
    UBLOCK_GREEK: "Greek",
    UBLOCK_CYRILLIC: "Cyrillic",
    UBLOCK_ARMENIAN: "Armenian",
    UBLOCK_HEBREW: "Hebrew",
    UBLOCK_ARABIC: "Arabic",
    UBLOCK_SYRIAC: "Syriac",
    UBLOCK_THAANA: "Thaana",
    UBLOCK_DEVANAGARI: "Devanagari",
    UBLOCK_BENGALI: "Bengali",
    UBLOCK_GURMUKHI: "Gurmukhi",
    UBLOCK_GUJARATI: "Gujarati",
    UBLOCK_ORIYA: "Oriya",
    UBLOCK_TAMIL: "Tamil",
    UBLOCK_TELUGU: "Telugu",
    UBLOCK_KANNADA: "Kannada",
    UBLOCK_MALAYALAM: "Malayalam",
    UBLOCK_SINHALA: "Sinhala",
    UBLOCK_THAI: "Thai",
    UBLOCK_LAO: "Lao",
    UBLOCK_TIBETAN: "Tibetan",
    UBLOCK_MYANMAR: "Myanmar",
    UBLOCK_GEORGIAN: "Georgian",
    UBLOCK_HANGUL_JAMO: "Jamo",
    UBLOCK_ETHIOPIC: "Ethiopic",
    UBLOCK_CHEROKEE: "Cherokee",
    UBLOCK_UNIFIED_CANADIAN_ABORIGINAL_SYLLABICS: "UCAS",
    UBLOCK_OGHAM: "Ogham",
    UBLOCK_RUNIC: "Runic",
    UBLOCK_KHMER: "Khmer",
    UBLOCK_MONGOLIAN: "Mongolian",
    UBLOCK_LATIN_EXTENDED_ADDITIONAL: "Latin Ext Additional",
    UBLOCK_GREEK_EXTENDED: "Greek Ext",
    UBLOCK_GENERAL_PUNCTUATION: "Punctuation",
    UBLOCK_SUPERSCRIPTS_AND_SUBSCRIPTS: "Super And Sub",
    UBLOCK_CURRENCY_SYMBOLS: "Currency Symbols",
    UBLOCK_COMBINING_MARKS_FOR_SYMBOLS: "Diacriticals For Symbols",
    UBLOCK_LETTERLIKE_SYMBOLS: "Letterlike Symbols",
    UBLOCK_NUMBER_FORMS: "Number Forms",
    UBLOCK_ARROWS: "Arrows",
    UBLOCK_MATHEMATICAL_OPERATORS: "Math Operators",
    UBLOCK_MISCELLANEOUS_TECHNICAL: "Misc Technical",
    UBLOCK_CONTROL_PICTURES: "Control Pictures",
    UBLOCK_OPTICAL_CHARACTER_RECOGNITION: "OCR",
    UBLOCK_ENCLOSED_ALPHANUMERICS: "Enclosed Alphanum",
    UBLOCK_BOX_DRAWING: "Box Drawing",
    UBLOCK_BLOCK_ELEMENTS: "Block Elements",
    UBLOCK_GEOMETRIC_SHAPES: "Geometric Shapes",
    UBLOCK_MISCELLANEOUS_SYMBOLS: "Misc Symbols",
    UBLOCK_DINGBATS: "Dingbats",
    UBLOCK_BRAILLE_PATTERNS: "Braille",
    UBLOCK_CJK_RADICALS_SUPPLEMENT: "CJK Radicals Sup",
    UBLOCK_KANGXI_RADICALS: "Kangxi",
    UBLOCK_IDEOGRAPHIC_DESCRIPTION_CHARACTERS: "IDC",
    UBLOCK_CJK_SYMBOLS_AND_PUNCTUATION: "CJK Symbols",
    UBLOCK_HIRAGANA: "Hiragana",
    UBLOCK_KATAKANA: "Katakana",
    UBLOCK_BOPOMOFO: "Bopomofo",
    UBLOCK_HANGUL_COMPATIBILITY_JAMO: "Compat Jamo",
    UBLOCK_KANBUN: "Kanbun",
    UBLOCK_BOPOMOFO_EXTENDED: "Bopomofo Ext",
    UBLOCK_ENCLOSED_CJK_LETTERS_AND_MONTHS: "Enclosed CJK",
    UBLOCK_CJK_COMPATIBILITY: "CJK Compat",
    UBLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_A: "CJK Ext A",
    UBLOCK_CJK_UNIFIED_IDEOGRAPHS: "CJK",
    UBLOCK_YI_SYLLABLES: "Yi Syllables",
    UBLOCK_YI_RADICALS: "Yi Radicals",
    UBLOCK_HANGUL_SYLLABLES: "Hangul",
    UBLOCK_HIGH_SURROGATES: "High Surrogates",
    UBLOCK_HIGH_PRIVATE_USE_SURROGATES: "High Private Use Surrogates",
    UBLOCK_LOW_SURROGATES: "Low Surrogates",
    UBLOCK_PRIVATE_USE_AREA: "Private Use Area",
    UBLOCK_CJK_COMPATIBILITY_IDEOGRAPHS: "CJK Compat Ideographs",
    UBLOCK_ALPHABETIC_PRESENTATION_FORMS: "Alphabetic PF",
    UBLOCK_ARABIC_PRESENTATION_FORMS_A: "Arabic PF A",
    UBLOCK_COMBINING_HALF_MARKS: "Half Marks",
    UBLOCK_CJK_COMPATIBILITY_FORMS: "CJK Compat Forms",
    UBLOCK_SMALL_FORM_VARIANTS: "Small Forms",
    UBLOCK_ARABIC_PRESENTATION_FORMS_B: "Arabic PF B",
    UBLOCK_SPECIALS: "Specials",
    UBLOCK_HALFWIDTH_AND_FULLWIDTH_FORMS: "Half And Full Forms",
    UBLOCK_OLD_ITALIC: "Old Italic",
    UBLOCK_GOTHIC: "Gothic",
    UBLOCK_DESERET: "Deseret",
    UBLOCK_BYZANTINE_MUSICAL_SYMBOLS: "Byzantine Music",
    UBLOCK_MUSICAL_SYMBOLS: "Music",
    UBLOCK_MATHEMATICAL_ALPHANUMERIC_SYMBOLS: "Math Alphanum",
    UBLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_B: "CJK Ext B",
    UBLOCK_CJK_COMPATIBILITY_IDEOGRAPHS_SUPPLEMENT: "CJK Compat Ideographs Sup",
    UBLOCK_TAGS: "Tags",
    UBLOCK_CYRILLIC_SUPPLEMENT: "Cyrillic Sup",
    UBLOCK_TAGALOG: "Tagalog",
    UBLOCK_HANUNOO: "Hanunoo",
    UBLOCK_BUHID: "Buhid",
    UBLOCK_TAGBANWA: "Tagbanwa",
    UBLOCK_MISCELLANEOUS_MATHEMATICAL_SYMBOLS_A: "Misc Math Symbols A",
    UBLOCK_SUPPLEMENTAL_ARROWS_A: "Sup Arrows A",
    UBLOCK_SUPPLEMENTAL_ARROWS_B: "Sup Arrows B",
    UBLOCK_MISCELLANEOUS_MATHEMATICAL_SYMBOLS_B: "Misc Math Symbols B",
    UBLOCK_SUPPLEMENTAL_MATHEMATICAL_OPERATORS: "Sup Math Operators",
    UBLOCK_KATAKANA_PHONETIC_EXTENSIONS: "Katakana Ext",
    UBLOCK_VARIATION_SELECTORS: "VS",
    UBLOCK_SUPPLEMENTARY_PRIVATE_USE_AREA_A: "Supary Private Use Area A",
    UBLOCK_SUPPLEMENTARY_PRIVATE_USE_AREA_B: "Supary Private Use Area B",
    UBLOCK_LIMBU: "Limbu",
    UBLOCK_TAI_LE: "Tai Le",
    UBLOCK_KHMER_SYMBOLS: "Khmer Symbols",
    UBLOCK_PHONETIC_EXTENSIONS: "Phonetic Ext",
    UBLOCK_MISCELLANEOUS_SYMBOLS_AND_ARROWS: "Misc Arrows",
    UBLOCK_YIJING_HEXAGRAM_SYMBOLS: "Yijing",
    UBLOCK_LINEAR_B_SYLLABARY: "Linear B Syllabary",
    UBLOCK_LINEAR_B_IDEOGRAMS: "Linear B Ideograms",
    UBLOCK_AEGEAN_NUMBERS: "Aegean Numbers",
    UBLOCK_UGARITIC: "Ugaritic",
    UBLOCK_SHAVIAN: "Shavian",
    UBLOCK_OSMANYA: "Osmanya",
    UBLOCK_CYPRIOT_SYLLABARY: "Cypriot Syllabary",
    UBLOCK_TAI_XUAN_JING_SYMBOLS: "Tai Xuan Jing",
    UBLOCK_VARIATION_SELECTORS_SUPPLEMENT: "VS Sup",
    UBLOCK_ANCIENT_GREEK_MUSICAL_NOTATION: "Ancient Greek Music",
    UBLOCK_ANCIENT_GREEK_NUMBERS: "Ancient Greek Numbers",
    UBLOCK_ARABIC_SUPPLEMENT: "Arabic Sup",
    UBLOCK_BUGINESE: "Buginese",
    UBLOCK_CJK_STROKES: "CJK Strokes",
    UBLOCK_COMBINING_DIACRITICAL_MARKS_SUPPLEMENT: "Diacriticals Sup",
    UBLOCK_COPTIC: "Coptic",
    UBLOCK_ETHIOPIC_EXTENDED: "Ethiopic Ext",
    UBLOCK_ETHIOPIC_SUPPLEMENT: "Ethiopic Sup",
    UBLOCK_GEORGIAN_SUPPLEMENT: "Georgian Sup",
    UBLOCK_GLAGOLITIC: "Glagolitic",
    UBLOCK_KHAROSHTHI: "Kharoshthi",
    UBLOCK_MODIFIER_TONE_LETTERS: "Modifier Tone Letters",
    UBLOCK_NEW_TAI_LUE: "New Tai Lue",
    UBLOCK_OLD_PERSIAN: "Old Persian",
    UBLOCK_PHONETIC_EXTENSIONS_SUPPLEMENT: "Phonetic Ext Sup",
    UBLOCK_SUPPLEMENTAL_PUNCTUATION: "Sup Punctuation",
    UBLOCK_SYLOTI_NAGRI: "Syloti Nagri",
    UBLOCK_TIFINAGH: "Tifinagh",
    UBLOCK_VERTICAL_FORMS: "Vertical Forms",
    UBLOCK_NKO: "NKo",
    UBLOCK_BALINESE: "Balinese",
    UBLOCK_LATIN_EXTENDED_C: "Latin Ext C",
    UBLOCK_LATIN_EXTENDED_D: "Latin Ext D",
    UBLOCK_PHAGS_PA: "Phags Pa",
    UBLOCK_PHOENICIAN: "Phoenician",
    UBLOCK_CUNEIFORM: "Cuneiform",
    UBLOCK_CUNEIFORM_NUMBERS_AND_PUNCTUATION: "Cuneiform Numbers",
    UBLOCK_COUNTING_ROD_NUMERALS: "Counting Rod",
    UBLOCK_SUNDANESE: "Sundanese",
    UBLOCK_LEPCHA: "Lepcha",
    UBLOCK_OL_CHIKI: "Ol Chiki",
    UBLOCK_CYRILLIC_EXTENDED_A: "Cyrillic Ext A",
    UBLOCK_VAI: "Vai",
    UBLOCK_CYRILLIC_EXTENDED_B: "Cyrillic Ext B",
    UBLOCK_SAURASHTRA: "Saurashtra",
    UBLOCK_KAYAH_LI: "Kayah Li",
    UBLOCK_REJANG: "Rejang",
    UBLOCK_CHAM: "Cham",
    UBLOCK_ANCIENT_SYMBOLS: "Ancient Symbols",
    UBLOCK_PHAISTOS_DISC: "Phaistos",
    UBLOCK_LYCIAN: "Lycian",
    UBLOCK_CARIAN: "Carian",
    UBLOCK_LYDIAN: "Lydian",
    UBLOCK_MAHJONG_TILES: "Mahjong",
    UBLOCK_DOMINO_TILES: "Domino",
    UBLOCK_SAMARITAN: "Samaritan",
    UBLOCK_UNIFIED_CANADIAN_ABORIGINAL_SYLLABICS_EXTENDED: "UCAS Ext",
    UBLOCK_TAI_THAM: "Tai Tham",
    UBLOCK_VEDIC_EXTENSIONS: "Vedic Ext",
    UBLOCK_LISU: "Lisu",
    UBLOCK_BAMUM: "Bamum",
    UBLOCK_COMMON_INDIC_NUMBER_FORMS: "Indic Number Forms",
    UBLOCK_DEVANAGARI_EXTENDED: "Devanagari Ext",
    UBLOCK_HANGUL_JAMO_EXTENDED_A: "Jamo Ext A",
    UBLOCK_JAVANESE: "Javanese",
    UBLOCK_MYANMAR_EXTENDED_A: "Myanmar Ext A",
    UBLOCK_TAI_VIET: "Tai Viet",
    UBLOCK_MEETEI_MAYEK: "Meetei Mayek",
    UBLOCK_HANGUL_JAMO_EXTENDED_B: "Jamo Ext B",
    UBLOCK_IMPERIAL_ARAMAIC: "Imperial Aramaic",
    UBLOCK_OLD_SOUTH_ARABIAN: "Old South Arabian",
    UBLOCK_AVESTAN: "Avestan",
    UBLOCK_INSCRIPTIONAL_PARTHIAN: "Inscriptional Parthian",
    UBLOCK_INSCRIPTIONAL_PAHLAVI: "Inscriptional Pahlavi",
    UBLOCK_OLD_TURKIC: "Old Turkic",
    UBLOCK_RUMI_NUMERAL_SYMBOLS: "Rumi",
    UBLOCK_KAITHI: "Kaithi",
    UBLOCK_EGYPTIAN_HIEROGLYPHS: "Egyptian Hieroglyphs",
    UBLOCK_ENCLOSED_ALPHANUMERIC_SUPPLEMENT: "Enclosed Alphanum Sup",
    UBLOCK_ENCLOSED_IDEOGRAPHIC_SUPPLEMENT: "Enclosed Ideographic Sup",
    UBLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_C: "CJK Ext C",
    UBLOCK_MANDAIC: "Mandaic",
    UBLOCK_BATAK: "Batak",
    UBLOCK_ETHIOPIC_EXTENDED_A: "Ethiopic Ext A",
    UBLOCK_BRAHMI: "Brahmi",
    UBLOCK_BAMUM_SUPPLEMENT: "Bamum Sup",
    UBLOCK_KANA_SUPPLEMENT: "Kana Sup",
    UBLOCK_PLAYING_CARDS: "Playing Cards",
    UBLOCK_MISCELLANEOUS_SYMBOLS_AND_PICTOGRAPHS: "Misc Pictographs",
    UBLOCK_EMOTICONS: "Emoticons",
    UBLOCK_TRANSPORT_AND_MAP_SYMBOLS: "Transport And Map",
    UBLOCK_ALCHEMICAL_SYMBOLS: "Alchemical",
    UBLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_D: "CJK Ext D",
    UBLOCK_ARABIC_EXTENDED_A: "Arabic Ext A",
    UBLOCK_ARABIC_MATHEMATICAL_ALPHABETIC_SYMBOLS: "Arabic Math",
    UBLOCK_CHAKMA: "Chakma",
    UBLOCK_MEETEI_MAYEK_EXTENSIONS: "Meetei Mayek Ext",
    UBLOCK_MEROITIC_CURSIVE: "Meroitic Cursive",
    UBLOCK_MEROITIC_HIEROGLYPHS: "Meroitic Hieroglyphs",
    UBLOCK_MIAO: "Miao",
    UBLOCK_SHARADA: "Sharada",
    UBLOCK_SORA_SOMPENG: "Sora Sompeng",
    UBLOCK_SUNDANESE_SUPPLEMENT: "Sundanese Sup",
    UBLOCK_TAKRI: "Takri",
    UBLOCK_BASSA_VAH: "Bassa Vah",
    UBLOCK_CAUCASIAN_ALBANIAN: "Caucasian Albanian",
    UBLOCK_COPTIC_EPACT_NUMBERS: "Coptic Epact Numbers",
    UBLOCK_COMBINING_DIACRITICAL_MARKS_EXTENDED: "Diacriticals Ext",
    UBLOCK_DUPLOYAN: "Duployan",
    UBLOCK_ELBASAN: "Elbasan",
    UBLOCK_GEOMETRIC_SHAPES_EXTENDED: "Geometric Shapes Ext",
    UBLOCK_GRANTHA: "Grantha",
    UBLOCK_KHOJKI: "Khojki",
    UBLOCK_KHUDAWADI: "Khudawadi",
    UBLOCK_LATIN_EXTENDED_E: "Latin Ext E",
    UBLOCK_LINEAR_A: "Linear A",
    UBLOCK_MAHAJANI: "Mahajani",
    UBLOCK_MANICHAEAN: "Manichaean",
    UBLOCK_MENDE_KIKAKUI: "Mende Kikakui",
    UBLOCK_MODI: "Modi",
    UBLOCK_MRO: "Mro",
    UBLOCK_MYANMAR_EXTENDED_B: "Myanmar Ext B",
    UBLOCK_NABATAEAN: "Nabataean",
    UBLOCK_OLD_NORTH_ARABIAN: "Old North Arabian",
    UBLOCK_OLD_PERMIC: "Old Permic",
    UBLOCK_ORNAMENTAL_DINGBATS: "Ornamental Dingbats",
    UBLOCK_PAHAWH_HMONG: "Pahawh Hmong",
    UBLOCK_PALMYRENE: "Palmyrene",
    UBLOCK_PAU_CIN_HAU: "Pau Cin Hau",
    UBLOCK_PSALTER_PAHLAVI: "Psalter Pahlavi",
    UBLOCK_SHORTHAND_FORMAT_CONTROLS: "Shorthand Format Controls",
    UBLOCK_SIDDHAM: "Siddham",
    UBLOCK_SINHALA_ARCHAIC_NUMBERS: "Sinhala Archaic Numbers",
    UBLOCK_SUPPLEMENTAL_ARROWS_C: "Sup Arrows C",
    UBLOCK_TIRHUTA: "Tirhuta",
    UBLOCK_WARANG_CITI: "Warang Citi",
    UBLOCK_AHOM: "Ahom",
    UBLOCK_ANATOLIAN_HIEROGLYPHS: "Anatolian Hieroglyphs",
    UBLOCK_CHEROKEE_SUPPLEMENT: "Cherokee Sup",
    UBLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_E: "CJK Ext E",
    UBLOCK_EARLY_DYNASTIC_CUNEIFORM: "Early Dynastic Cuneiform",
    UBLOCK_HATRAN: "Hatran",
    UBLOCK_MULTANI: "Multani",
    UBLOCK_OLD_HUNGARIAN: "Old Hungarian",
    UBLOCK_SUPPLEMENTAL_SYMBOLS_AND_PICTOGRAPHS: "Sup Symbols And Pictographs",
    UBLOCK_SUTTON_SIGNWRITING: "Sutton SignWriting",
    UBLOCK_ADLAM: "Adlam",
    UBLOCK_BHAIKSUKI: "Bhaiksuki",
    UBLOCK_CYRILLIC_EXTENDED_C: "Cyrillic Ext C",
    UBLOCK_GLAGOLITIC_SUPPLEMENT: "Glagolitic Sup",
    UBLOCK_IDEOGRAPHIC_SYMBOLS_AND_PUNCTUATION: "Ideographic Symbols",
    UBLOCK_MARCHEN: "Marchen",
    UBLOCK_MONGOLIAN_SUPPLEMENT: "Mongolian Sup",
    UBLOCK_NEWA: "Newa",
    UBLOCK_OSAGE: "Osage",
    UBLOCK_TANGUT: "Tangut",
    UBLOCK_TANGUT_COMPONENTS: "Tangut Components",
    UBLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_F: "CJK Ext F",
    UBLOCK_KANA_EXTENDED_A: "Kana Ext A",
    UBLOCK_MASARAM_GONDI: "Masaram Gondi",
    UBLOCK_NUSHU: "Nushu",
    UBLOCK_SOYOMBO: "Soyombo",
    UBLOCK_SYRIAC_SUPPLEMENT: "Syriac Sup",
    UBLOCK_ZANABAZAR_SQUARE: "Zanabazar Square",
    UBLOCK_CHESS_SYMBOLS: "Chess Symbols",
    UBLOCK_DOGRA: "Dogra",
    UBLOCK_GEORGIAN_EXTENDED: "Georgian Ext",
    UBLOCK_GUNJALA_GONDI: "Gunjala Gondi",
    UBLOCK_HANIFI_ROHINGYA: "Hanifi Rohingya",
    UBLOCK_INDIC_SIYAQ_NUMBERS: "Indic Siyaq Numbers",
    UBLOCK_MAKASAR: "Makasar",
    UBLOCK_MAYAN_NUMERALS: "Mayan Numerals",
    UBLOCK_MEDEFAIDRIN: "Medefaidrin",
    UBLOCK_OLD_SOGDIAN: "Old Sogdian",
    UBLOCK_SOGDIAN: "Sogdian",
    UBLOCK_EGYPTIAN_HIEROGLYPH_FORMAT_CONTROLS: "Egyptian Hieroglyph Format Controls",
    UBLOCK_ELYMAIC: "Elymaic",
    UBLOCK_NANDINAGARI: "Nandinagari",
    UBLOCK_NYIAKENG_PUACHUE_HMONG: "Nyiakeng Puachue Hmong",
    UBLOCK_OTTOMAN_SIYAQ_NUMBERS: "Ottoman Siyaq Numbers",
    UBLOCK_SMALL_KANA_EXTENSION: "Small Kana Ext",
    UBLOCK_SYMBOLS_AND_PICTOGRAPHS_EXTENDED_A: "Symbols And Pictographs Ext A",
    UBLOCK_TAMIL_SUPPLEMENT: "Tamil Sup",
    UBLOCK_WANCHO: "Wancho",
    UBLOCK_CHORASMIAN: "Chorasmian",
    UBLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_G: "CJK Ext G",
    UBLOCK_DIVES_AKURU: "Dives Akuru",
    UBLOCK_KHITAN_SMALL_SCRIPT: "Khitan Small Script",
    UBLOCK_LISU_SUPPLEMENT: "Lisu Sup",
    UBLOCK_SYMBOLS_FOR_LEGACY_COMPUTING: "Symbols For Legacy Computing",
    UBLOCK_TANGUT_SUPPLEMENT: "Tangut Sup",
    UBLOCK_YEZIDI: "Yezidi",
}

