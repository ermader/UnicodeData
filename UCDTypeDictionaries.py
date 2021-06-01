"""/
UCDTypeDictionaries.py, based on ppucd.txt from ICU

Generated by UCDReader.py on May 31, 2021 at 02:26:00 PM HST
"""

from uchar_h import *
from uscript_h import *

bidiClassNames = {
    U_RIGHT_TO_LEFT_ARABIC: "AL",
    U_ARABIC_NUMBER: "AN",
    U_BLOCK_SEPARATOR: "B",
    U_BOUNDARY_NEUTRAL: "BN",
    U_COMMON_NUMBER_SEPARATOR: "CS",
    U_EUROPEAN_NUMBER: "EN",
    U_EUROPEAN_NUMBER_SEPARATOR: "ES",
    U_EUROPEAN_NUMBER_TERMINATOR: "ET",
    U_FIRST_STRONG_ISOLATE: "FSI",
    U_LEFT_TO_RIGHT: "L",
    U_LEFT_TO_RIGHT_EMBEDDING: "LRE",
    U_LEFT_TO_RIGHT_ISOLATE: "LRI",
    U_LEFT_TO_RIGHT_OVERRIDE: "LRO",
    U_NON_SPACING_MARK: "NSM",
    U_OTHER_NEUTRAL: "ON",
    U_POP_DIRECTIONAL_FORMAT: "PDF",
    U_POP_DIRECTIONAL_ISOLATE: "PDI",
    U_RIGHT_TO_LEFT: "R",
    U_RIGHT_TO_LEFT_EMBEDDING: "RLE",
    U_RIGHT_TO_LEFT_ISOLATE: "RLI",
    U_RIGHT_TO_LEFT_OVERRIDE: "RLO",
    U_SEGMENT_SEPARATOR: "S",
    U_WHITE_SPACE_NEUTRAL: "WS"
}

blockNames = {
    UBLOCK_BASIC_LATIN: "ASCII",
    UBLOCK_ADLAM: "Adlam",
    UBLOCK_AEGEAN_NUMBERS: "Aegean Numbers",
    UBLOCK_AHOM: "Ahom",
    UBLOCK_ALCHEMICAL_SYMBOLS: "Alchemical",
    UBLOCK_ALPHABETIC_PRESENTATION_FORMS: "Alphabetic PF",
    UBLOCK_ANATOLIAN_HIEROGLYPHS: "Anatolian Hieroglyphs",
    UBLOCK_ANCIENT_GREEK_MUSICAL_NOTATION: "Ancient Greek Music",
    UBLOCK_ANCIENT_GREEK_NUMBERS: "Ancient Greek Numbers",
    UBLOCK_ANCIENT_SYMBOLS: "Ancient Symbols",
    UBLOCK_ARABIC: "Arabic",
    UBLOCK_ARABIC_EXTENDED_A: "Arabic Ext A",
    UBLOCK_ARABIC_MATHEMATICAL_ALPHABETIC_SYMBOLS: "Arabic Math",
    UBLOCK_ARABIC_PRESENTATION_FORMS_A: "Arabic PF A",
    UBLOCK_ARABIC_PRESENTATION_FORMS_B: "Arabic PF B",
    UBLOCK_ARABIC_SUPPLEMENT: "Arabic Sup",
    UBLOCK_ARMENIAN: "Armenian",
    UBLOCK_ARROWS: "Arrows",
    UBLOCK_AVESTAN: "Avestan",
    UBLOCK_BALINESE: "Balinese",
    UBLOCK_BAMUM: "Bamum",
    UBLOCK_BAMUM_SUPPLEMENT: "Bamum Sup",
    UBLOCK_BASSA_VAH: "Bassa Vah",
    UBLOCK_BATAK: "Batak",
    UBLOCK_BENGALI: "Bengali",
    UBLOCK_BHAIKSUKI: "Bhaiksuki",
    UBLOCK_BLOCK_ELEMENTS: "Block Elements",
    UBLOCK_BOPOMOFO: "Bopomofo",
    UBLOCK_BOPOMOFO_EXTENDED: "Bopomofo Ext",
    UBLOCK_BOX_DRAWING: "Box Drawing",
    UBLOCK_BRAHMI: "Brahmi",
    UBLOCK_BRAILLE_PATTERNS: "Braille",
    UBLOCK_BUGINESE: "Buginese",
    UBLOCK_BUHID: "Buhid",
    UBLOCK_BYZANTINE_MUSICAL_SYMBOLS: "Byzantine Music",
    UBLOCK_CJK_UNIFIED_IDEOGRAPHS: "CJK",
    UBLOCK_CJK_COMPATIBILITY: "CJK Compat",
    UBLOCK_CJK_COMPATIBILITY_FORMS: "CJK Compat Forms",
    UBLOCK_CJK_COMPATIBILITY_IDEOGRAPHS: "CJK Compat Ideographs",
    UBLOCK_CJK_COMPATIBILITY_IDEOGRAPHS_SUPPLEMENT: "CJK Compat Ideographs Sup",
    UBLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_A: "CJK Ext A",
    UBLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_B: "CJK Ext B",
    UBLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_C: "CJK Ext C",
    UBLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_D: "CJK Ext D",
    UBLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_E: "CJK Ext E",
    UBLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_F: "CJK Ext F",
    UBLOCK_CJK_UNIFIED_IDEOGRAPHS_EXTENSION_G: "CJK Ext G",
    UBLOCK_CJK_RADICALS_SUPPLEMENT: "CJK Radicals Sup",
    UBLOCK_CJK_STROKES: "CJK Strokes",
    UBLOCK_CJK_SYMBOLS_AND_PUNCTUATION: "CJK Symbols",
    UBLOCK_CARIAN: "Carian",
    UBLOCK_CAUCASIAN_ALBANIAN: "Caucasian Albanian",
    UBLOCK_CHAKMA: "Chakma",
    UBLOCK_CHAM: "Cham",
    UBLOCK_CHEROKEE: "Cherokee",
    UBLOCK_CHEROKEE_SUPPLEMENT: "Cherokee Sup",
    UBLOCK_CHESS_SYMBOLS: "Chess Symbols",
    UBLOCK_CHORASMIAN: "Chorasmian",
    UBLOCK_HANGUL_COMPATIBILITY_JAMO: "Compat Jamo",
    UBLOCK_CONTROL_PICTURES: "Control Pictures",
    UBLOCK_COPTIC: "Coptic",
    UBLOCK_COPTIC_EPACT_NUMBERS: "Coptic Epact Numbers",
    UBLOCK_COUNTING_ROD_NUMERALS: "Counting Rod",
    UBLOCK_CUNEIFORM: "Cuneiform",
    UBLOCK_CUNEIFORM_NUMBERS_AND_PUNCTUATION: "Cuneiform Numbers",
    UBLOCK_CURRENCY_SYMBOLS: "Currency Symbols",
    UBLOCK_CYPRIOT_SYLLABARY: "Cypriot Syllabary",
    UBLOCK_CYRILLIC: "Cyrillic",
    UBLOCK_CYRILLIC_EXTENDED_A: "Cyrillic Ext A",
    UBLOCK_CYRILLIC_EXTENDED_B: "Cyrillic Ext B",
    UBLOCK_CYRILLIC_EXTENDED_C: "Cyrillic Ext C",
    UBLOCK_CYRILLIC_SUPPLEMENT: "Cyrillic Sup",
    UBLOCK_DESERET: "Deseret",
    UBLOCK_DEVANAGARI: "Devanagari",
    UBLOCK_DEVANAGARI_EXTENDED: "Devanagari Ext",
    UBLOCK_COMBINING_DIACRITICAL_MARKS: "Diacriticals",
    UBLOCK_COMBINING_DIACRITICAL_MARKS_EXTENDED: "Diacriticals Ext",
    UBLOCK_COMBINING_MARKS_FOR_SYMBOLS: "Diacriticals For Symbols",
    UBLOCK_COMBINING_DIACRITICAL_MARKS_SUPPLEMENT: "Diacriticals Sup",
    UBLOCK_DINGBATS: "Dingbats",
    UBLOCK_DIVES_AKURU: "Dives Akuru",
    UBLOCK_DOGRA: "Dogra",
    UBLOCK_DOMINO_TILES: "Domino",
    UBLOCK_DUPLOYAN: "Duployan",
    UBLOCK_EARLY_DYNASTIC_CUNEIFORM: "Early Dynastic Cuneiform",
    UBLOCK_EGYPTIAN_HIEROGLYPH_FORMAT_CONTROLS: "Egyptian Hieroglyph Format Controls",
    UBLOCK_EGYPTIAN_HIEROGLYPHS: "Egyptian Hieroglyphs",
    UBLOCK_ELBASAN: "Elbasan",
    UBLOCK_ELYMAIC: "Elymaic",
    UBLOCK_EMOTICONS: "Emoticons",
    UBLOCK_ENCLOSED_ALPHANUMERICS: "Enclosed Alphanum",
    UBLOCK_ENCLOSED_ALPHANUMERIC_SUPPLEMENT: "Enclosed Alphanum Sup",
    UBLOCK_ENCLOSED_CJK_LETTERS_AND_MONTHS: "Enclosed CJK",
    UBLOCK_ENCLOSED_IDEOGRAPHIC_SUPPLEMENT: "Enclosed Ideographic Sup",
    UBLOCK_ETHIOPIC: "Ethiopic",
    UBLOCK_ETHIOPIC_EXTENDED: "Ethiopic Ext",
    UBLOCK_ETHIOPIC_EXTENDED_A: "Ethiopic Ext A",
    UBLOCK_ETHIOPIC_SUPPLEMENT: "Ethiopic Sup",
    UBLOCK_GEOMETRIC_SHAPES: "Geometric Shapes",
    UBLOCK_GEOMETRIC_SHAPES_EXTENDED: "Geometric Shapes Ext",
    UBLOCK_GEORGIAN: "Georgian",
    UBLOCK_GEORGIAN_EXTENDED: "Georgian Ext",
    UBLOCK_GEORGIAN_SUPPLEMENT: "Georgian Sup",
    UBLOCK_GLAGOLITIC: "Glagolitic",
    UBLOCK_GLAGOLITIC_SUPPLEMENT: "Glagolitic Sup",
    UBLOCK_GOTHIC: "Gothic",
    UBLOCK_GRANTHA: "Grantha",
    UBLOCK_GREEK: "Greek",
    UBLOCK_GREEK_EXTENDED: "Greek Ext",
    UBLOCK_GUJARATI: "Gujarati",
    UBLOCK_GUNJALA_GONDI: "Gunjala Gondi",
    UBLOCK_GURMUKHI: "Gurmukhi",
    UBLOCK_HALFWIDTH_AND_FULLWIDTH_FORMS: "Half And Full Forms",
    UBLOCK_COMBINING_HALF_MARKS: "Half Marks",
    UBLOCK_HANGUL_SYLLABLES: "Hangul",
    UBLOCK_HANIFI_ROHINGYA: "Hanifi Rohingya",
    UBLOCK_HANUNOO: "Hanunoo",
    UBLOCK_HATRAN: "Hatran",
    UBLOCK_HEBREW: "Hebrew",
    UBLOCK_HIGH_PRIVATE_USE_SURROGATES: "High PU Surrogates",
    UBLOCK_HIGH_SURROGATES: "High Surrogates",
    UBLOCK_HIRAGANA: "Hiragana",
    UBLOCK_IDEOGRAPHIC_DESCRIPTION_CHARACTERS: "IDC",
    UBLOCK_IPA_EXTENSIONS: "IPA Ext",
    UBLOCK_IDEOGRAPHIC_SYMBOLS_AND_PUNCTUATION: "Ideographic Symbols",
    UBLOCK_IMPERIAL_ARAMAIC: "Imperial Aramaic",
    UBLOCK_COMMON_INDIC_NUMBER_FORMS: "Indic Number Forms",
    UBLOCK_INDIC_SIYAQ_NUMBERS: "Indic Siyaq Numbers",
    UBLOCK_INSCRIPTIONAL_PAHLAVI: "Inscriptional Pahlavi",
    UBLOCK_INSCRIPTIONAL_PARTHIAN: "Inscriptional Parthian",
    UBLOCK_HANGUL_JAMO: "Jamo",
    UBLOCK_HANGUL_JAMO_EXTENDED_A: "Jamo Ext A",
    UBLOCK_HANGUL_JAMO_EXTENDED_B: "Jamo Ext B",
    UBLOCK_JAVANESE: "Javanese",
    UBLOCK_KAITHI: "Kaithi",
    UBLOCK_KANA_EXTENDED_A: "Kana Ext A",
    UBLOCK_KANA_SUPPLEMENT: "Kana Sup",
    UBLOCK_KANBUN: "Kanbun",
    UBLOCK_KANGXI_RADICALS: "Kangxi",
    UBLOCK_KANNADA: "Kannada",
    UBLOCK_KATAKANA: "Katakana",
    UBLOCK_KATAKANA_PHONETIC_EXTENSIONS: "Katakana Ext",
    UBLOCK_KAYAH_LI: "Kayah Li",
    UBLOCK_KHAROSHTHI: "Kharoshthi",
    UBLOCK_KHITAN_SMALL_SCRIPT: "Khitan Small Script",
    UBLOCK_KHMER: "Khmer",
    UBLOCK_KHMER_SYMBOLS: "Khmer Symbols",
    UBLOCK_KHOJKI: "Khojki",
    UBLOCK_KHUDAWADI: "Khudawadi",
    UBLOCK_LAO: "Lao",
    UBLOCK_LATIN_1_SUPPLEMENT: "Latin 1 Sup",
    UBLOCK_LATIN_EXTENDED_A: "Latin Ext A",
    UBLOCK_LATIN_EXTENDED_ADDITIONAL: "Latin Ext Additional",
    UBLOCK_LATIN_EXTENDED_B: "Latin Ext B",
    UBLOCK_LATIN_EXTENDED_C: "Latin Ext C",
    UBLOCK_LATIN_EXTENDED_D: "Latin Ext D",
    UBLOCK_LATIN_EXTENDED_E: "Latin Ext E",
    UBLOCK_LEPCHA: "Lepcha",
    UBLOCK_LETTERLIKE_SYMBOLS: "Letterlike Symbols",
    UBLOCK_LIMBU: "Limbu",
    UBLOCK_LINEAR_A: "Linear A",
    UBLOCK_LINEAR_B_IDEOGRAMS: "Linear B Ideograms",
    UBLOCK_LINEAR_B_SYLLABARY: "Linear B Syllabary",
    UBLOCK_LISU: "Lisu",
    UBLOCK_LISU_SUPPLEMENT: "Lisu Sup",
    UBLOCK_LOW_SURROGATES: "Low Surrogates",
    UBLOCK_LYCIAN: "Lycian",
    UBLOCK_LYDIAN: "Lydian",
    UBLOCK_MAHAJANI: "Mahajani",
    UBLOCK_MAHJONG_TILES: "Mahjong",
    UBLOCK_MAKASAR: "Makasar",
    UBLOCK_MALAYALAM: "Malayalam",
    UBLOCK_MANDAIC: "Mandaic",
    UBLOCK_MANICHAEAN: "Manichaean",
    UBLOCK_MARCHEN: "Marchen",
    UBLOCK_MASARAM_GONDI: "Masaram Gondi",
    UBLOCK_MATHEMATICAL_ALPHANUMERIC_SYMBOLS: "Math Alphanum",
    UBLOCK_MATHEMATICAL_OPERATORS: "Math Operators",
    UBLOCK_MAYAN_NUMERALS: "Mayan Numerals",
    UBLOCK_MEDEFAIDRIN: "Medefaidrin",
    UBLOCK_MEETEI_MAYEK: "Meetei Mayek",
    UBLOCK_MEETEI_MAYEK_EXTENSIONS: "Meetei Mayek Ext",
    UBLOCK_MENDE_KIKAKUI: "Mende Kikakui",
    UBLOCK_MEROITIC_CURSIVE: "Meroitic Cursive",
    UBLOCK_MEROITIC_HIEROGLYPHS: "Meroitic Hieroglyphs",
    UBLOCK_MIAO: "Miao",
    UBLOCK_MISCELLANEOUS_SYMBOLS_AND_ARROWS: "Misc Arrows",
    UBLOCK_MISCELLANEOUS_MATHEMATICAL_SYMBOLS_A: "Misc Math Symbols A",
    UBLOCK_MISCELLANEOUS_MATHEMATICAL_SYMBOLS_B: "Misc Math Symbols B",
    UBLOCK_MISCELLANEOUS_SYMBOLS_AND_PICTOGRAPHS: "Misc Pictographs",
    UBLOCK_MISCELLANEOUS_SYMBOLS: "Misc Symbols",
    UBLOCK_MISCELLANEOUS_TECHNICAL: "Misc Technical",
    UBLOCK_MODI: "Modi",
    UBLOCK_SPACING_MODIFIER_LETTERS: "Modifier Letters",
    UBLOCK_MODIFIER_TONE_LETTERS: "Modifier Tone Letters",
    UBLOCK_MONGOLIAN: "Mongolian",
    UBLOCK_MONGOLIAN_SUPPLEMENT: "Mongolian Sup",
    UBLOCK_MRO: "Mro",
    UBLOCK_MULTANI: "Multani",
    UBLOCK_MUSICAL_SYMBOLS: "Music",
    UBLOCK_MYANMAR: "Myanmar",
    UBLOCK_MYANMAR_EXTENDED_A: "Myanmar Ext A",
    UBLOCK_MYANMAR_EXTENDED_B: "Myanmar Ext B",
    UBLOCK_NO_BLOCK: "NB",
    UBLOCK_NKO: "NKo",
    UBLOCK_NABATAEAN: "Nabataean",
    UBLOCK_NANDINAGARI: "Nandinagari",
    UBLOCK_NEW_TAI_LUE: "New Tai Lue",
    UBLOCK_NEWA: "Newa",
    UBLOCK_NUMBER_FORMS: "Number Forms",
    UBLOCK_NUSHU: "Nushu",
    UBLOCK_NYIAKENG_PUACHUE_HMONG: "Nyiakeng Puachue Hmong",
    UBLOCK_OPTICAL_CHARACTER_RECOGNITION: "OCR",
    UBLOCK_OGHAM: "Ogham",
    UBLOCK_OL_CHIKI: "Ol Chiki",
    UBLOCK_OLD_HUNGARIAN: "Old Hungarian",
    UBLOCK_OLD_ITALIC: "Old Italic",
    UBLOCK_OLD_NORTH_ARABIAN: "Old North Arabian",
    UBLOCK_OLD_PERMIC: "Old Permic",
    UBLOCK_OLD_PERSIAN: "Old Persian",
    UBLOCK_OLD_SOGDIAN: "Old Sogdian",
    UBLOCK_OLD_SOUTH_ARABIAN: "Old South Arabian",
    UBLOCK_OLD_TURKIC: "Old Turkic",
    UBLOCK_ORIYA: "Oriya",
    UBLOCK_ORNAMENTAL_DINGBATS: "Ornamental Dingbats",
    UBLOCK_OSAGE: "Osage",
    UBLOCK_OSMANYA: "Osmanya",
    UBLOCK_OTTOMAN_SIYAQ_NUMBERS: "Ottoman Siyaq Numbers",
    UBLOCK_PRIVATE_USE_AREA: "PUA",
    UBLOCK_PAHAWH_HMONG: "Pahawh Hmong",
    UBLOCK_PALMYRENE: "Palmyrene",
    UBLOCK_PAU_CIN_HAU: "Pau Cin Hau",
    UBLOCK_PHAGS_PA: "Phags Pa",
    UBLOCK_PHAISTOS_DISC: "Phaistos",
    UBLOCK_PHOENICIAN: "Phoenician",
    UBLOCK_PHONETIC_EXTENSIONS: "Phonetic Ext",
    UBLOCK_PHONETIC_EXTENSIONS_SUPPLEMENT: "Phonetic Ext Sup",
    UBLOCK_PLAYING_CARDS: "Playing Cards",
    UBLOCK_PSALTER_PAHLAVI: "Psalter Pahlavi",
    UBLOCK_GENERAL_PUNCTUATION: "Punctuation",
    UBLOCK_REJANG: "Rejang",
    UBLOCK_RUMI_NUMERAL_SYMBOLS: "Rumi",
    UBLOCK_RUNIC: "Runic",
    UBLOCK_SAMARITAN: "Samaritan",
    UBLOCK_SAURASHTRA: "Saurashtra",
    UBLOCK_SHARADA: "Sharada",
    UBLOCK_SHAVIAN: "Shavian",
    UBLOCK_SHORTHAND_FORMAT_CONTROLS: "Shorthand Format Controls",
    UBLOCK_SIDDHAM: "Siddham",
    UBLOCK_SINHALA: "Sinhala",
    UBLOCK_SINHALA_ARCHAIC_NUMBERS: "Sinhala Archaic Numbers",
    UBLOCK_SMALL_FORM_VARIANTS: "Small Forms",
    UBLOCK_SMALL_KANA_EXTENSION: "Small Kana Ext",
    UBLOCK_SOGDIAN: "Sogdian",
    UBLOCK_SORA_SOMPENG: "Sora Sompeng",
    UBLOCK_SOYOMBO: "Soyombo",
    UBLOCK_SPECIALS: "Specials",
    UBLOCK_SUNDANESE: "Sundanese",
    UBLOCK_SUNDANESE_SUPPLEMENT: "Sundanese Sup",
    UBLOCK_SUPPLEMENTAL_ARROWS_A: "Sup Arrows A",
    UBLOCK_SUPPLEMENTAL_ARROWS_B: "Sup Arrows B",
    UBLOCK_SUPPLEMENTAL_ARROWS_C: "Sup Arrows C",
    UBLOCK_SUPPLEMENTAL_MATHEMATICAL_OPERATORS: "Sup Math Operators",
    UBLOCK_SUPPLEMENTARY_PRIVATE_USE_AREA_A: "Sup PUA A",
    UBLOCK_SUPPLEMENTARY_PRIVATE_USE_AREA_B: "Sup PUA B",
    UBLOCK_SUPPLEMENTAL_PUNCTUATION: "Sup Punctuation",
    UBLOCK_SUPPLEMENTAL_SYMBOLS_AND_PICTOGRAPHS: "Sup Symbols And Pictographs",
    UBLOCK_SUPERSCRIPTS_AND_SUBSCRIPTS: "Super And Sub",
    UBLOCK_SUTTON_SIGNWRITING: "Sutton SignWriting",
    UBLOCK_SYLOTI_NAGRI: "Syloti Nagri",
    UBLOCK_SYMBOLS_AND_PICTOGRAPHS_EXTENDED_A: "Symbols And Pictographs Ext A",
    UBLOCK_SYMBOLS_FOR_LEGACY_COMPUTING: "Symbols For Legacy Computing",
    UBLOCK_SYRIAC: "Syriac",
    UBLOCK_SYRIAC_SUPPLEMENT: "Syriac Sup",
    UBLOCK_TAGALOG: "Tagalog",
    UBLOCK_TAGBANWA: "Tagbanwa",
    UBLOCK_TAGS: "Tags",
    UBLOCK_TAI_LE: "Tai Le",
    UBLOCK_TAI_THAM: "Tai Tham",
    UBLOCK_TAI_VIET: "Tai Viet",
    UBLOCK_TAI_XUAN_JING_SYMBOLS: "Tai Xuan Jing",
    UBLOCK_TAKRI: "Takri",
    UBLOCK_TAMIL: "Tamil",
    UBLOCK_TAMIL_SUPPLEMENT: "Tamil Sup",
    UBLOCK_TANGUT: "Tangut",
    UBLOCK_TANGUT_COMPONENTS: "Tangut Components",
    UBLOCK_TANGUT_SUPPLEMENT: "Tangut Sup",
    UBLOCK_TELUGU: "Telugu",
    UBLOCK_THAANA: "Thaana",
    UBLOCK_THAI: "Thai",
    UBLOCK_TIBETAN: "Tibetan",
    UBLOCK_TIFINAGH: "Tifinagh",
    UBLOCK_TIRHUTA: "Tirhuta",
    UBLOCK_TRANSPORT_AND_MAP_SYMBOLS: "Transport And Map",
    UBLOCK_UNIFIED_CANADIAN_ABORIGINAL_SYLLABICS: "UCAS",
    UBLOCK_UNIFIED_CANADIAN_ABORIGINAL_SYLLABICS_EXTENDED: "UCAS Ext",
    UBLOCK_UGARITIC: "Ugaritic",
    UBLOCK_VARIATION_SELECTORS: "VS",
    UBLOCK_VARIATION_SELECTORS_SUPPLEMENT: "VS Sup",
    UBLOCK_VAI: "Vai",
    UBLOCK_VEDIC_EXTENSIONS: "Vedic Ext",
    UBLOCK_VERTICAL_FORMS: "Vertical Forms",
    UBLOCK_WANCHO: "Wancho",
    UBLOCK_WARANG_CITI: "Warang Citi",
    UBLOCK_YEZIDI: "Yezidi",
    UBLOCK_YI_RADICALS: "Yi Radicals",
    UBLOCK_YI_SYLLABLES: "Yi Syllables",
    UBLOCK_YIJING_HEXAGRAM_SYMBOLS: "Yijing",
    UBLOCK_ZANABAZAR_SQUARE: "Zanabazar Square"
}

decompositionTypeNames = {
    U_DT_CANONICAL: "Can",
    U_DT_COMPAT: "Com",
    U_DT_CIRCLE: "Enc",
    U_DT_FINAL: "Fin",
    U_DT_FONT: "Font",
    U_DT_FRACTION: "Fra",
    U_DT_INITIAL: "Init",
    U_DT_ISOLATED: "Iso",
    U_DT_MEDIAL: "Med",
    U_DT_NARROW: "Nar",
    U_DT_NOBREAK: "Nb",
    U_DT_NONE: "None",
    U_DT_SMALL: "Sml",
    U_DT_SQUARE: "Sqr",
    U_DT_SUB: "Sub",
    U_DT_SUPER: "Sup",
    U_DT_VERTICAL: "Vert",
    U_DT_WIDE: "Wide"
}

eastAsianWidthNames = {
    U_EA_AMBIGUOUS: "A",
    U_EA_FULLWIDTH: "F",
    U_EA_HALFWIDTH: "H",
    U_EA_NEUTRAL: "N",
    U_EA_NARROW: "Na",
    U_EA_WIDE: "W"
}

generalCategoryNames = {
    U_CONTROL_CHAR: "Cc",
    U_FORMAT_CHAR: "Cf",
    U_UNASSIGNED: "Cn",
    U_PRIVATE_USE_CHAR: "Co",
    U_SURROGATE: "Cs",
    U_LOWERCASE_LETTER: "Ll",
    U_MODIFIER_LETTER: "Lm",
    U_OTHER_LETTER: "Lo",
    U_TITLECASE_LETTER: "Lt",
    U_UPPERCASE_LETTER: "Lu",
    U_COMBINING_SPACING_MARK: "Mc",
    U_ENCLOSING_MARK: "Me",
    U_NON_SPACING_MARK: "Mn",
    U_DECIMAL_DIGIT_NUMBER: "Nd",
    U_LETTER_NUMBER: "Nl",
    U_OTHER_NUMBER: "No",
    U_CONNECTOR_PUNCTUATION: "Pc",
    U_DASH_PUNCTUATION: "Pd",
    U_END_PUNCTUATION: "Pe",
    U_FINAL_PUNCTUATION: "Pf",
    U_INITIAL_PUNCTUATION: "Pi",
    U_OTHER_PUNCTUATION: "Po",
    U_START_PUNCTUATION: "Ps",
    U_CURRENCY_SYMBOL: "Sc",
    U_MODIFIER_SYMBOL: "Sk",
    U_MATH_SYMBOL: "Sm",
    U_OTHER_SYMBOL: "So",
    U_LINE_SEPARATOR: "Zl",
    U_PARAGRAPH_SEPARATOR: "Zp",
    U_SPACE_SEPARATOR: "Zs"
}

graphemeClusterBreakNames = {
    U_GCB_CONTROL: "CN",
    U_GCB_CR: "CR",
    U_GCB_E_BASE: "EB",
    U_GCB_E_BASE_GAZ: "EBG",
    U_GCB_E_MODIFIER: "EM",
    U_GCB_EXTEND: "EX",
    U_GCB_GLUE_AFTER_ZWJ: "GAZ",
    U_GCB_L: "L",
    U_GCB_LF: "LF",
    U_GCB_LV: "LV",
    U_GCB_LVT: "LVT",
    U_GCB_PREPEND: "PP",
    U_GCB_REGIONAL_INDICATOR: "RI",
    U_GCB_SPACING_MARK: "SM",
    U_GCB_T: "T",
    U_GCB_V: "V",
    U_GCB_OTHER: "XX",
    U_GCB_ZWJ: "ZWJ"
}

hangulSyllableTypeNames = {
    U_HST_LEADING_JAMO: "L",
    U_HST_LV_SYLLABLE: "LV",
    U_HST_LVT_SYLLABLE: "LVT",
    U_HST_NOT_APPLICABLE: "NA",
    U_HST_TRAILING_JAMO: "T",
    U_HST_VOWEL_JAMO: "V"
}

indicPositionalCategoryNames = {
    U_INPC_BOTTOM: "Bottom",
    U_INPC_BOTTOM_AND_LEFT: "Bottom And Left",
    U_INPC_BOTTOM_AND_RIGHT: "Bottom And Right",
    U_INPC_LEFT: "Left",
    U_INPC_LEFT_AND_RIGHT: "Left And Right",
    U_INPC_NA: "NA",
    U_INPC_OVERSTRUCK: "Overstruck",
    U_INPC_RIGHT: "Right",
    U_INPC_TOP: "Top",
    U_INPC_TOP_AND_BOTTOM: "Top And Bottom",
    U_INPC_TOP_AND_BOTTOM_AND_LEFT: "Top And Bottom And Left",
    U_INPC_TOP_AND_BOTTOM_AND_RIGHT: "Top And Bottom And Right",
    U_INPC_TOP_AND_LEFT: "Top And Left",
    U_INPC_TOP_AND_LEFT_AND_RIGHT: "Top And Left And Right",
    U_INPC_TOP_AND_RIGHT: "Top And Right",
    U_INPC_VISUAL_ORDER_LEFT: "Visual Order Left"
}

indicSyllabicCategoryNames = {
    U_INSC_AVAGRAHA: "Avagraha",
    U_INSC_BINDU: "Bindu",
    U_INSC_BRAHMI_JOINING_NUMBER: "Brahmi Joining Number",
    U_INSC_CANTILLATION_MARK: "Cantillation Mark",
    U_INSC_CONSONANT: "Consonant",
    U_INSC_CONSONANT_DEAD: "Consonant Dead",
    U_INSC_CONSONANT_FINAL: "Consonant Final",
    U_INSC_CONSONANT_HEAD_LETTER: "Consonant Head Letter",
    U_INSC_CONSONANT_INITIAL_POSTFIXED: "Consonant Initial Postfixed",
    U_INSC_CONSONANT_KILLER: "Consonant Killer",
    U_INSC_CONSONANT_MEDIAL: "Consonant Medial",
    U_INSC_CONSONANT_PLACEHOLDER: "Consonant Placeholder",
    U_INSC_CONSONANT_PRECEDING_REPHA: "Consonant Preceding Repha",
    U_INSC_CONSONANT_PREFIXED: "Consonant Prefixed",
    U_INSC_CONSONANT_SUBJOINED: "Consonant Subjoined",
    U_INSC_CONSONANT_SUCCEEDING_REPHA: "Consonant Succeeding Repha",
    U_INSC_CONSONANT_WITH_STACKER: "Consonant With Stacker",
    U_INSC_GEMINATION_MARK: "Gemination Mark",
    U_INSC_INVISIBLE_STACKER: "Invisible Stacker",
    U_INSC_JOINER: "Joiner",
    U_INSC_MODIFYING_LETTER: "Modifying Letter",
    U_INSC_NON_JOINER: "Non Joiner",
    U_INSC_NUKTA: "Nukta",
    U_INSC_NUMBER: "Number",
    U_INSC_NUMBER_JOINER: "Number Joiner",
    U_INSC_OTHER: "Other",
    U_INSC_PURE_KILLER: "Pure Killer",
    U_INSC_REGISTER_SHIFTER: "Register Shifter",
    U_INSC_SYLLABLE_MODIFIER: "Syllable Modifier",
    U_INSC_TONE_LETTER: "Tone Letter",
    U_INSC_TONE_MARK: "Tone Mark",
    U_INSC_VIRAMA: "Virama",
    U_INSC_VISARGA: "Visarga",
    U_INSC_VOWEL: "Vowel",
    U_INSC_VOWEL_DEPENDENT: "Vowel Dependent",
    U_INSC_VOWEL_INDEPENDENT: "Vowel Independent"
}

joiningGroupNames = {
    U_JG_AFRICAN_FEH: "African Feh",
    U_JG_AFRICAN_NOON: "African Noon",
    U_JG_AFRICAN_QAF: "African Qaf",
    U_JG_AIN: "Ain",
    U_JG_ALAPH: "Alaph",
    U_JG_ALEF: "Alef",
    U_JG_BEH: "Beh",
    U_JG_BETH: "Beth",
    U_JG_BURUSHASKI_YEH_BARREE: "Burushaski Yeh Barree",
    U_JG_DAL: "Dal",
    U_JG_DALATH_RISH: "Dalath Rish",
    U_JG_E: "E",
    U_JG_FARSI_YEH: "Farsi Yeh",
    U_JG_FE: "Fe",
    U_JG_FEH: "Feh",
    U_JG_FINAL_SEMKATH: "Final Semkath",
    U_JG_GAF: "Gaf",
    U_JG_GAMAL: "Gamal",
    U_JG_HAH: "Hah",
    U_JG_HANIFI_ROHINGYA_KINNA_YA: "Hanifi Rohingya Kinna Ya",
    U_JG_HANIFI_ROHINGYA_PA: "Hanifi Rohingya Pa",
    U_JG_HE: "He",
    U_JG_HEH: "Heh",
    U_JG_HEH_GOAL: "Heh Goal",
    U_JG_HETH: "Heth",
    U_JG_KAF: "Kaf",
    U_JG_KAPH: "Kaph",
    U_JG_KHAPH: "Khaph",
    U_JG_KNOTTED_HEH: "Knotted Heh",
    U_JG_LAM: "Lam",
    U_JG_LAMADH: "Lamadh",
    U_JG_MALAYALAM_BHA: "Malayalam Bha",
    U_JG_MALAYALAM_JA: "Malayalam Ja",
    U_JG_MALAYALAM_LLA: "Malayalam Lla",
    U_JG_MALAYALAM_LLLA: "Malayalam Llla",
    U_JG_MALAYALAM_NGA: "Malayalam Nga",
    U_JG_MALAYALAM_NNA: "Malayalam Nna",
    U_JG_MALAYALAM_NNNA: "Malayalam Nnna",
    U_JG_MALAYALAM_NYA: "Malayalam Nya",
    U_JG_MALAYALAM_RA: "Malayalam Ra",
    U_JG_MALAYALAM_SSA: "Malayalam Ssa",
    U_JG_MALAYALAM_TTA: "Malayalam Tta",
    U_JG_MANICHAEAN_ALEPH: "Manichaean Aleph",
    U_JG_MANICHAEAN_AYIN: "Manichaean Ayin",
    U_JG_MANICHAEAN_BETH: "Manichaean Beth",
    U_JG_MANICHAEAN_DALETH: "Manichaean Daleth",
    U_JG_MANICHAEAN_DHAMEDH: "Manichaean Dhamedh",
    U_JG_MANICHAEAN_FIVE: "Manichaean Five",
    U_JG_MANICHAEAN_GIMEL: "Manichaean Gimel",
    U_JG_MANICHAEAN_HETH: "Manichaean Heth",
    U_JG_MANICHAEAN_HUNDRED: "Manichaean Hundred",
    U_JG_MANICHAEAN_KAPH: "Manichaean Kaph",
    U_JG_MANICHAEAN_LAMEDH: "Manichaean Lamedh",
    U_JG_MANICHAEAN_MEM: "Manichaean Mem",
    U_JG_MANICHAEAN_NUN: "Manichaean Nun",
    U_JG_MANICHAEAN_ONE: "Manichaean One",
    U_JG_MANICHAEAN_PE: "Manichaean Pe",
    U_JG_MANICHAEAN_QOPH: "Manichaean Qoph",
    U_JG_MANICHAEAN_RESH: "Manichaean Resh",
    U_JG_MANICHAEAN_SADHE: "Manichaean Sadhe",
    U_JG_MANICHAEAN_SAMEKH: "Manichaean Samekh",
    U_JG_MANICHAEAN_TAW: "Manichaean Taw",
    U_JG_MANICHAEAN_TEN: "Manichaean Ten",
    U_JG_MANICHAEAN_TETH: "Manichaean Teth",
    U_JG_MANICHAEAN_THAMEDH: "Manichaean Thamedh",
    U_JG_MANICHAEAN_TWENTY: "Manichaean Twenty",
    U_JG_MANICHAEAN_WAW: "Manichaean Waw",
    U_JG_MANICHAEAN_YODH: "Manichaean Yodh",
    U_JG_MANICHAEAN_ZAYIN: "Manichaean Zayin",
    U_JG_MEEM: "Meem",
    U_JG_MIM: "Mim",
    U_JG_NO_JOINING_GROUP: "No Joining Group",
    U_JG_NOON: "Noon",
    U_JG_NUN: "Nun",
    U_JG_NYA: "Nya",
    U_JG_PE: "Pe",
    U_JG_QAF: "Qaf",
    U_JG_QAPH: "Qaph",
    U_JG_REH: "Reh",
    U_JG_REVERSED_PE: "Reversed Pe",
    U_JG_ROHINGYA_YEH: "Rohingya Yeh",
    U_JG_SAD: "Sad",
    U_JG_SADHE: "Sadhe",
    U_JG_SEEN: "Seen",
    U_JG_SEMKATH: "Semkath",
    U_JG_SHIN: "Shin",
    U_JG_STRAIGHT_WAW: "Straight Waw",
    U_JG_SWASH_KAF: "Swash Kaf",
    U_JG_SYRIAC_WAW: "Syriac Waw",
    U_JG_TAH: "Tah",
    U_JG_TAW: "Taw",
    U_JG_TEH_MARBUTA: "Teh Marbuta",
    U_JG_HAMZA_ON_HEH_GOAL: "Teh Marbuta Goal",
    U_JG_TETH: "Teth",
    U_JG_WAW: "Waw",
    U_JG_YEH: "Yeh",
    U_JG_YEH_BARREE: "Yeh Barree",
    U_JG_YEH_WITH_TAIL: "Yeh With Tail",
    U_JG_YUDH: "Yudh",
    U_JG_YUDH_HE: "Yudh He",
    U_JG_ZAIN: "Zain",
    U_JG_ZHAIN: "Zhain"
}

joiningTypeNames = {
    U_JT_JOIN_CAUSING: "C",
    U_JT_DUAL_JOINING: "D",
    U_JT_LEFT_JOINING: "L",
    U_JT_RIGHT_JOINING: "R",
    U_JT_TRANSPARENT: "T",
    U_JT_NON_JOINING: "U"
}

lineBreakNames = {
    U_LB_AMBIGUOUS: "AI",
    U_LB_ALPHABETIC: "AL",
    U_LB_BREAK_BOTH: "B2",
    U_LB_BREAK_AFTER: "BA",
    U_LB_BREAK_BEFORE: "BB",
    U_LB_MANDATORY_BREAK: "BK",
    U_LB_CONTINGENT_BREAK: "CB",
    U_LB_CONDITIONAL_JAPANESE_STARTER: "CJ",
    U_LB_CLOSE_PUNCTUATION: "CL",
    U_LB_COMBINING_MARK: "CM",
    U_LB_CLOSE_PARENTHESIS: "CP",
    U_LB_CARRIAGE_RETURN: "CR",
    U_LB_E_BASE: "EB",
    U_LB_E_MODIFIER: "EM",
    U_LB_EXCLAMATION: "EX",
    U_LB_GLUE: "GL",
    U_LB_H2: "H2",
    U_LB_H3: "H3",
    U_LB_HEBREW_LETTER: "HL",
    U_LB_HYPHEN: "HY",
    U_LB_IDEOGRAPHIC: "ID",
    U_LB_INSEPARABLE: "IN",
    U_LB_INFIX_NUMERIC: "IS",
    U_LB_JL: "JL",
    U_LB_JT: "JT",
    U_LB_JV: "JV",
    U_LB_LINE_FEED: "LF",
    U_LB_NEXT_LINE: "NL",
    U_LB_NONSTARTER: "NS",
    U_LB_NUMERIC: "NU",
    U_LB_OPEN_PUNCTUATION: "OP",
    U_LB_POSTFIX_NUMERIC: "PO",
    U_LB_PREFIX_NUMERIC: "PR",
    U_LB_QUOTATION: "QU",
    U_LB_REGIONAL_INDICATOR: "RI",
    U_LB_COMPLEX_CONTEXT: "SA",
    U_LB_SURROGATE: "SG",
    U_LB_SPACE: "SP",
    U_LB_BREAK_SYMBOLS: "SY",
    U_LB_WORD_JOINER: "WJ",
    U_LB_UNKNOWN: "XX",
    U_LB_ZWSPACE: "ZW",
    U_LB_ZWJ: "ZWJ"
}

numberTypeNames = {
    U_NT_DECIMAL: "De",
    U_NT_DIGIT: "Di",
    U_NT_NONE: "None",
    U_NT_NUMERIC: "Nu"
}

sentenceBreakNames = {
    U_SB_ATERM: "AT",
    U_SB_CLOSE: "CL",
    U_SB_CR: "CR",
    U_SB_EXTEND: "EX",
    U_SB_FORMAT: "FO",
    U_SB_OLETTER: "LE",
    U_SB_LF: "LF",
    U_SB_LOWER: "LO",
    U_SB_NUMERIC: "NU",
    U_SB_SCONTINUE: "SC",
    U_SB_SEP: "SE",
    U_SB_SP: "SP",
    U_SB_STERM: "ST",
    U_SB_UPPER: "UP",
    U_SB_OTHER: "XX"
}

scriptNames = {
    USCRIPT_ADLAM: "Adlm",
    USCRIPT_AFAKA: "Afak",
    USCRIPT_CAUCASIAN_ALBANIAN: "Aghb",
    USCRIPT_AHOM: "Ahom",
    USCRIPT_ARABIC: "Arab",
    USCRIPT_IMPERIAL_ARAMAIC: "Armi",
    USCRIPT_ARMENIAN: "Armn",
    USCRIPT_AVESTAN: "Avst",
    USCRIPT_BALINESE: "Bali",
    USCRIPT_BAMUM: "Bamu",
    USCRIPT_BASSA_VAH: "Bass",
    USCRIPT_BATAK: "Batk",
    USCRIPT_BENGALI: "Beng",
    USCRIPT_BHAIKSUKI: "Bhks",
    USCRIPT_BLISSYMBOLS: "Blis",
    USCRIPT_BOPOMOFO: "Bopo",
    USCRIPT_BRAHMI: "Brah",
    USCRIPT_BRAILLE: "Brai",
    USCRIPT_BUGINESE: "Bugi",
    USCRIPT_BUHID: "Buhd",
    USCRIPT_CHAKMA: "Cakm",
    USCRIPT_CANADIAN_ABORIGINAL: "Cans",
    USCRIPT_CARIAN: "Cari",
    USCRIPT_CHAM: "Cham",
    USCRIPT_CHEROKEE: "Cher",
    USCRIPT_CHORASMIAN: "Chrs",
    USCRIPT_CIRTH: "Cirt",
    USCRIPT_COPTIC: "Copt",
    USCRIPT_CYPRIOT: "Cprt",
    USCRIPT_CYRILLIC: "Cyrl",
    USCRIPT_OLD_CHURCH_SLAVONIC_CYRILLIC: "Cyrs",
    USCRIPT_DEVANAGARI: "Deva",
    USCRIPT_DIVES_AKURU: "Diak",
    USCRIPT_DOGRA: "Dogr",
    USCRIPT_DESERET: "Dsrt",
    USCRIPT_DUPLOYAN: "Dupl",
    USCRIPT_DEMOTIC_EGYPTIAN: "Egyd",
    USCRIPT_HIERATIC_EGYPTIAN: "Egyh",
    USCRIPT_EGYPTIAN_HIEROGLYPHS: "Egyp",
    USCRIPT_ELBASAN: "Elba",
    USCRIPT_ELYMAIC: "Elym",
    USCRIPT_ETHIOPIC: "Ethi",
    USCRIPT_KHUTSURI: "Geok",
    USCRIPT_GEORGIAN: "Geor",
    USCRIPT_GLAGOLITIC: "Glag",
    USCRIPT_GUNJALA_GONDI: "Gong",
    USCRIPT_MASARAM_GONDI: "Gonm",
    USCRIPT_GOTHIC: "Goth",
    USCRIPT_GRANTHA: "Gran",
    USCRIPT_GREEK: "Grek",
    USCRIPT_GUJARATI: "Gujr",
    USCRIPT_GURMUKHI: "Guru",
    USCRIPT_HAN_WITH_BOPOMOFO: "Hanb",
    USCRIPT_HANGUL: "Hang",
    USCRIPT_HAN: "Hani",
    USCRIPT_HANUNOO: "Hano",
    USCRIPT_SIMPLIFIED_HAN: "Hans",
    USCRIPT_TRADITIONAL_HAN: "Hant",
    USCRIPT_HATRAN: "Hatr",
    USCRIPT_HEBREW: "Hebr",
    USCRIPT_HIRAGANA: "Hira",
    USCRIPT_ANATOLIAN_HIEROGLYPHS: "Hluw",
    USCRIPT_PAHAWH_HMONG: "Hmng",
    USCRIPT_NYIAKENG_PUACHUE_HMONG: "Hmnp",
    USCRIPT_KATAKANA_OR_HIRAGANA: "Hrkt",
    USCRIPT_OLD_HUNGARIAN: "Hung",
    USCRIPT_HARAPPAN_INDUS: "Inds",
    USCRIPT_OLD_ITALIC: "Ital",
    USCRIPT_JAMO: "Jamo",
    USCRIPT_JAVANESE: "Java",
    USCRIPT_JAPANESE: "Jpan",
    USCRIPT_JURCHEN: "Jurc",
    USCRIPT_KAYAH_LI: "Kali",
    USCRIPT_KATAKANA: "Kana",
    USCRIPT_KHAROSHTHI: "Khar",
    USCRIPT_KHMER: "Khmr",
    USCRIPT_KHOJKI: "Khoj",
    USCRIPT_KHITAN_SMALL_SCRIPT: "Kits",
    USCRIPT_KANNADA: "Knda",
    USCRIPT_KOREAN: "Kore",
    USCRIPT_KPELLE: "Kpel",
    USCRIPT_KAITHI: "Kthi",
    USCRIPT_LANNA: "Lana",
    USCRIPT_LAO: "Laoo",
    USCRIPT_LATIN_FRAKTUR: "Latf",
    USCRIPT_LATIN_GAELIC: "Latg",
    USCRIPT_LATIN: "Latn",
    USCRIPT_LEPCHA: "Lepc",
    USCRIPT_LIMBU: "Limb",
    USCRIPT_LINEAR_A: "Lina",
    USCRIPT_LINEAR_B: "Linb",
    USCRIPT_LISU: "Lisu",
    USCRIPT_LOMA: "Loma",
    USCRIPT_LYCIAN: "Lyci",
    USCRIPT_LYDIAN: "Lydi",
    USCRIPT_MAHAJANI: "Mahj",
    USCRIPT_MAKASAR: "Maka",
    USCRIPT_MANDAIC: "Mand",
    USCRIPT_MANICHAEAN: "Mani",
    USCRIPT_MARCHEN: "Marc",
    USCRIPT_MAYAN_HIEROGLYPHS: "Maya",
    USCRIPT_MEDEFAIDRIN: "Medf",
    USCRIPT_MENDE: "Mend",
    USCRIPT_MEROITIC_CURSIVE: "Merc",
    USCRIPT_MEROITIC_HIEROGLYPHS: "Mero",
    USCRIPT_MALAYALAM: "Mlym",
    USCRIPT_MODI: "Modi",
    USCRIPT_MONGOLIAN: "Mong",
    USCRIPT_MOON: "Moon",
    USCRIPT_MRO: "Mroo",
    USCRIPT_MEITEI_MAYEK: "Mtei",
    USCRIPT_MULTANI: "Mult",
    USCRIPT_MYANMAR: "Mymr",
    USCRIPT_NANDINAGARI: "Nand",
    USCRIPT_OLD_NORTH_ARABIAN: "Narb",
    USCRIPT_NABATAEAN: "Nbat",
    USCRIPT_NEWA: "Newa",
    USCRIPT_NAKHI_GEBA: "Nkgb",
    USCRIPT_NKO: "Nkoo",
    USCRIPT_NUSHU: "Nshu",
    USCRIPT_OGHAM: "Ogam",
    USCRIPT_OL_CHIKI: "Olck",
    USCRIPT_ORKHON: "Orkh",
    USCRIPT_ORIYA: "Orya",
    USCRIPT_OSAGE: "Osge",
    USCRIPT_OSMANYA: "Osma",
    USCRIPT_PALMYRENE: "Palm",
    USCRIPT_PAU_CIN_HAU: "Pauc",
    USCRIPT_OLD_PERMIC: "Perm",
    USCRIPT_PHAGS_PA: "Phag",
    USCRIPT_INSCRIPTIONAL_PAHLAVI: "Phli",
    USCRIPT_PSALTER_PAHLAVI: "Phlp",
    USCRIPT_BOOK_PAHLAVI: "Phlv",
    USCRIPT_PHOENICIAN: "Phnx",
    USCRIPT_MIAO: "Plrd",
    USCRIPT_INSCRIPTIONAL_PARTHIAN: "Prti",
    USCRIPT_REJANG: "Rjng",
    USCRIPT_HANIFI_ROHINGYA: "Rohg",
    USCRIPT_RONGORONGO: "Roro",
    USCRIPT_RUNIC: "Runr",
    USCRIPT_SAMARITAN: "Samr",
    USCRIPT_SARATI: "Sara",
    USCRIPT_OLD_SOUTH_ARABIAN: "Sarb",
    USCRIPT_SAURASHTRA: "Saur",
    USCRIPT_SIGN_WRITING: "Sgnw",
    USCRIPT_SHAVIAN: "Shaw",
    USCRIPT_SHARADA: "Shrd",
    USCRIPT_SIDDHAM: "Sidd",
    USCRIPT_KHUDAWADI: "Sind",
    USCRIPT_SINHALA: "Sinh",
    USCRIPT_SOGDIAN: "Sogd",
    USCRIPT_OLD_SOGDIAN: "Sogo",
    USCRIPT_SORA_SOMPENG: "Sora",
    USCRIPT_SOYOMBO: "Soyo",
    USCRIPT_SUNDANESE: "Sund",
    USCRIPT_SYLOTI_NAGRI: "Sylo",
    USCRIPT_SYRIAC: "Syrc",
    USCRIPT_ESTRANGELO_SYRIAC: "Syre",
    USCRIPT_WESTERN_SYRIAC: "Syrj",
    USCRIPT_EASTERN_SYRIAC: "Syrn",
    USCRIPT_TAGBANWA: "Tagb",
    USCRIPT_TAKRI: "Takr",
    USCRIPT_TAI_LE: "Tale",
    USCRIPT_NEW_TAI_LUE: "Talu",
    USCRIPT_TAMIL: "Taml",
    USCRIPT_TANGUT: "Tang",
    USCRIPT_TAI_VIET: "Tavt",
    USCRIPT_TELUGU: "Telu",
    USCRIPT_TENGWAR: "Teng",
    USCRIPT_TIFINAGH: "Tfng",
    USCRIPT_TAGALOG: "Tglg",
    USCRIPT_THAANA: "Thaa",
    USCRIPT_THAI: "Thai",
    USCRIPT_TIBETAN: "Tibt",
    USCRIPT_TIRHUTA: "Tirh",
    USCRIPT_UGARITIC: "Ugar",
    USCRIPT_VAI: "Vaii",
    USCRIPT_VISIBLE_SPEECH: "Visp",
    USCRIPT_WARANG_CITI: "Wara",
    USCRIPT_WANCHO: "Wcho",
    USCRIPT_WOLEAI: "Wole",
    USCRIPT_OLD_PERSIAN: "Xpeo",
    USCRIPT_CUNEIFORM: "Xsux",
    USCRIPT_YEZIDI: "Yezi",
    USCRIPT_YI: "Yiii",
    USCRIPT_ZANABAZAR_SQUARE: "Zanb",
    USCRIPT_INHERITED: "Zinh",
    USCRIPT_MATHEMATICAL_NOTATION: "Zmth",
    USCRIPT_SYMBOLS_EMOJI: "Zsye",
    USCRIPT_SYMBOLS: "Zsym",
    USCRIPT_UNWRITTEN_LANGUAGES: "Zxxx",
    USCRIPT_COMMON: "Zyyy",
    USCRIPT_UNKNOWN: "Zzzz"
}

verticalOrientationNames = {
    U_VO_ROTATED: "R",
    U_VO_TRANSFORMED_ROTATED: "Tr",
    U_VO_TRANSFORMED_UPRIGHT: "Tu",
    U_VO_UPRIGHT: "U"
}

wordBreakNames = {
    U_WB_CR: "CR",
    U_WB_DOUBLE_QUOTE: "DQ",
    U_WB_E_BASE: "EB",
    U_WB_E_BASE_GAZ: "EBG",
    U_WB_E_MODIFIER: "EM",
    U_WB_EXTENDNUMLET: "EX",
    U_WB_EXTEND: "Extend",
    U_WB_FORMAT: "FO",
    U_WB_GLUE_AFTER_ZWJ: "GAZ",
    U_WB_HEBREW_LETTER: "HL",
    U_WB_KATAKANA: "KA",
    U_WB_ALETTER: "LE",
    U_WB_LF: "LF",
    U_WB_MIDNUMLET: "MB",
    U_WB_MIDLETTER: "ML",
    U_WB_MIDNUM: "MN",
    U_WB_NEWLINE: "NL",
    U_WB_NUMERIC: "NU",
    U_WB_REGIONAL_INDICATOR: "RI",
    U_WB_SINGLE_QUOTE: "SQ",
    U_WB_WSEGSPACE: "WSegSpace",
    U_WB_OTHER: "XX",
    U_WB_ZWJ: "ZWJ"
}

