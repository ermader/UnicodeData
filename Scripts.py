"""\
Base on uscript.h from ICU

Created on Apr 30, 2020

@author Eric Mader
"""

USCRIPT_INVALID_CODE = -1
USCRIPT_COMMON       =  0  # 'Zyyy'
USCRIPT_INHERITED    =  1  # 'Zinh' # "Code for inherited script", for non-spacing combining marks; also Qaai
USCRIPT_ARABIC       =  2  # 'Arab'
USCRIPT_ARMENIAN     =  3  # 'Armn'
USCRIPT_BENGALI      =  4  # 'Beng'
USCRIPT_BOPOMOFO     =  5  # 'Bopo'
USCRIPT_CHEROKEE     =  6  # 'Cher'
USCRIPT_COPTIC       =  7  # 'Copt'
USCRIPT_CYRILLIC     =  8  # 'Cyrl'
USCRIPT_DESERET      =  9  # 'Dsrt'
USCRIPT_DEVANAGARI   = 10  # 'Deva'
USCRIPT_ETHIOPIC     = 11  # 'Ethi'
USCRIPT_GEORGIAN     = 12  # 'Geor'
USCRIPT_GOTHIC       = 13  # 'Goth'
USCRIPT_GREEK        = 14  # 'Grek'
USCRIPT_GUJARATI     = 15  # 'Gujr'
USCRIPT_GURMUKHI     = 16  # 'Guru'
USCRIPT_HAN          = 17  # 'Hani'
USCRIPT_HANGUL       = 18  # 'Hang'
USCRIPT_HEBREW       = 19  # 'Hebr'
USCRIPT_HIRAGANA     = 20  # 'Hira'
USCRIPT_KANNADA      = 21  # 'Knda'
USCRIPT_KATAKANA     = 22  # 'Kana'
USCRIPT_KHMER        = 23  # 'Khmr'
USCRIPT_LAO          = 24  # 'Laoo'
USCRIPT_LATIN        = 25  # 'Latn'
USCRIPT_MALAYALAM    = 26  # 'Mlym'
USCRIPT_MONGOLIAN    = 27  # 'Mong'
USCRIPT_MYANMAR      = 28  # 'Mymr'
USCRIPT_OGHAM        = 29  # 'Ogam'
USCRIPT_OLD_ITALIC   = 30  # 'Ital'
USCRIPT_ORIYA        = 31  # 'Orya'
USCRIPT_RUNIC        = 32  # 'Runr'
USCRIPT_SINHALA      = 33  # 'Sinh'
USCRIPT_SYRIAC       = 34  # 'Syrc'
USCRIPT_TAMIL        = 35  # 'Taml'
USCRIPT_TELUGU       = 36  # 'Telu'
USCRIPT_THAANA       = 37  # 'Thaa'
USCRIPT_THAI         = 38  # 'Thai'
USCRIPT_TIBETAN      = 39  # 'Tibt'
USCRIPT_CANADIAN_ABORIGINAL = 40  # 'Cans'
USCRIPT_UCAS         = USCRIPT_CANADIAN_ABORIGINAL,
USCRIPT_YI           = 41  # 'Yiii'

# New scripts in Unicode 3.2
USCRIPT_TAGALOG      = 42  # 'Tglg'
USCRIPT_HANUNOO      = 43  # 'Hano'
USCRIPT_BUHID        = 44  # 'Buhd'
USCRIPT_TAGBANWA     = 45  # 'Tagb'

# New scripts in Unicode 4
USCRIPT_BRAILLE      = 46  # 'Brai'
USCRIPT_CYPRIOT      = 47  # 'Cprt'
USCRIPT_LIMBU        = 48  # 'Limb'
USCRIPT_LINEAR_B     = 49  # 'Linb'
USCRIPT_OSMANYA      = 50  # 'Osma'
USCRIPT_SHAVIAN      = 51  # 'Shaw'
USCRIPT_TAI_LE       = 52  # 'Tale'
USCRIPT_UGARITIC     = 53  # 'Ugar'

# New scripts in Unicode 4.0.1
USCRIPT_KATAKANA_OR_HIRAGANA = 54  # 'Hrkt'

# New scripts in Unicode 4.1
USCRIPT_BUGINESE      = 55  # 'Bugi'
USCRIPT_GLAGOLITIC    = 56  # 'Glag'
USCRIPT_KHAROSHTHI    = 57  # 'Khar'
USCRIPT_SYLOTI_NAGRI  = 58  # 'Sylo'
USCRIPT_NEW_TAI_LUE   = 59  # 'Talu'
USCRIPT_TIFINAGH      = 60  # 'Tfng'
USCRIPT_OLD_PERSIAN   = 61  # 'Xpeo'

# New script codes from Unicode and ISO 15924
USCRIPT_BALINESE                      = 62  # 'Bali'
USCRIPT_BATAK                         = 63  # 'Batk'
USCRIPT_BLISSYMBOLS                   = 64  # 'Blis'
USCRIPT_BRAHMI                        = 65  # 'Brah'
USCRIPT_CHAM                          = 66  # 'Cham'
USCRIPT_CIRTH                         = 67  # 'Cirt'
USCRIPT_OLD_CHURCH_SLAVONIC_CYRILLIC  = 68  # 'Cyrs'
USCRIPT_DEMOTIC_EGYPTIAN              = 69  # 'Egyd'
USCRIPT_HIERATIC_EGYPTIAN             = 70  # 'Egyh'
USCRIPT_EGYPTIAN_HIEROGLYPHS          = 71  # 'Egyp'
USCRIPT_KHUTSURI                      = 72  # 'Geok'
USCRIPT_SIMPLIFIED_HAN                = 73  # 'Hans'
USCRIPT_TRADITIONAL_HAN               = 74  # 'Hant'
USCRIPT_PAHAWH_HMONG                  = 75  # 'Hmng'
USCRIPT_OLD_HUNGARIAN                 = 76  # 'Hung'
USCRIPT_HARAPPAN_INDUS                = 77  # 'Inds'
USCRIPT_JAVANESE                      = 78  # 'Java'
USCRIPT_KAYAH_LI                      = 79  # 'Kali'
USCRIPT_LATIN_FRAKTUR                 = 80  # 'Latf'
USCRIPT_LATIN_GAELIC                  = 81  # 'Latg'
USCRIPT_LEPCHA                        = 82  # 'Lepc'
USCRIPT_LINEAR_A                      = 83  # 'Lina'
USCRIPT_MANDAIC                       = 84  # 'Mand'
USCRIPT_MANDAEAN                      = USCRIPT_MANDAIC,
USCRIPT_MAYAN_HIEROGLYPHS             = 85  # 'Maya'
USCRIPT_MEROITIC_HIEROGLYPHS          = 86  # 'Mero'
USCRIPT_MEROITIC                      = USCRIPT_MEROITIC_HIEROGLYPHS,
USCRIPT_NKO                           = 87  # 'Nkoo'
USCRIPT_ORKHON                        = 88  # 'Orkh'
USCRIPT_OLD_PERMIC                    = 89  # 'Perm'
USCRIPT_PHAGS_PA                      = 90  # 'Phag'
USCRIPT_PHOENICIAN                    = 91  # 'Phnx'
USCRIPT_MIAO                          = 92  # 'Plrd'
USCRIPT_PHONETIC_POLLARD              = USCRIPT_MIAO,
USCRIPT_RONGORONGO                    = 93  # 'Roro'
USCRIPT_SARATI                        = 94  # 'Sara'
USCRIPT_ESTRANGELO_SYRIAC             = 95  # 'Syre'
USCRIPT_WESTERN_SYRIAC                = 96  # 'Syrj'
USCRIPT_EASTERN_SYRIAC                = 97  # 'Syrn'
USCRIPT_TENGWAR                       = 98  # 'Teng'
USCRIPT_VAI                           = 99  # 'Vaii'
USCRIPT_VISIBLE_SPEECH                = 100  # 'Visp'
USCRIPT_CUNEIFORM                     = 101  # 'Xsux'
USCRIPT_UNWRITTEN_LANGUAGES           = 102  # 'Zxxx'
USCRIPT_UNKNOWN                       = 103  # 'Zzzz' # Unknown="Code for uncoded script", for unassigned code points
USCRIPT_CARIAN                        = 104  # 'Cari'
USCRIPT_JAPANESE                      = 105  # 'Jpan'
USCRIPT_LANNA                         = 106  # 'Lana'
USCRIPT_LYCIAN                        = 107  # 'Lyci'
USCRIPT_LYDIAN                        = 108  # 'Lydi'
USCRIPT_OL_CHIKI                      = 109  # 'Olck'
USCRIPT_REJANG                        = 110  # 'Rjng'
USCRIPT_SAURASHTRA                    = 111  # 'Saur'
USCRIPT_SIGN_WRITING                  = 112  # 'Sgnw'
USCRIPT_SUNDANESE                     = 113  # 'Sund'
USCRIPT_MOON                          = 114  # 'Moon'
USCRIPT_MEITEI_MAYEK                  = 115  # 'Mtei'
USCRIPT_IMPERIAL_ARAMAIC              = 116  # 'Armi'
USCRIPT_AVESTAN                       = 117  # 'Avst'
USCRIPT_CHAKMA                        = 118  # 'Cakm'
USCRIPT_KOREAN                        = 119  # 'Kore'
USCRIPT_KAITHI                        = 120  # 'Kthi'
USCRIPT_MANICHAEAN                    = 121  # 'Mani'
USCRIPT_INSCRIPTIONAL_PAHLAVI         = 122  # 'Phli'
USCRIPT_PSALTER_PAHLAVI               = 123  # 'Phlp'
USCRIPT_BOOK_PAHLAVI                  = 124  # 'Phlv'
USCRIPT_INSCRIPTIONAL_PARTHIAN        = 125  # 'Prti'
USCRIPT_SAMARITAN                     = 126  # 'Samr'
USCRIPT_TAI_VIET                      = 127  # 'Tavt'
USCRIPT_MATHEMATICAL_NOTATION         = 128  # 'Zmth'
USCRIPT_SYMBOLS                       = 129  # 'Zsym'
USCRIPT_BAMUM                         = 130  # 'Bamu'
USCRIPT_LISU                          = 131  # 'Lisu'
USCRIPT_NAKHI_GEBA                    = 132  # 'Nkgb'
USCRIPT_OLD_SOUTH_ARABIAN             = 133  # 'Sarb'
USCRIPT_BASSA_VAH                     = 134  # 'Bass'
USCRIPT_DUPLOYAN                      = 135  # 'Dupl'
USCRIPT_ELBASAN                       = 136  # 'Elba'
USCRIPT_GRANTHA                       = 137  # 'Gran'
USCRIPT_KPELLE                        = 138  # 'Kpel'
USCRIPT_LOMA                          = 139  # 'Loma'
USCRIPT_MENDE                         = 140  # 'Mend'
USCRIPT_MEROITIC_CURSIVE              = 141  # 'Merc'
USCRIPT_OLD_NORTH_ARABIAN             = 142  # 'Narb'
USCRIPT_NABATAEAN                     = 143  # 'Nbat'
USCRIPT_PALMYRENE                     = 144  # 'Palm'
USCRIPT_KHUDAWADI                     = 145  # 'Sind'
USCRIPT_SINDHI                        = USCRIPT_KHUDAWADI,
USCRIPT_WARANG_CITI                   = 146  # 'Wara'
USCRIPT_AFAKA                         = 147  # 'Afak'
USCRIPT_JURCHEN                       = 148  # 'Jurc'
USCRIPT_MRO                           = 149  # 'Mroo'
USCRIPT_NUSHU                         = 150  # 'Nshu'
USCRIPT_SHARADA                       = 151  # 'Shrd'
USCRIPT_SORA_SOMPENG                  = 152  # 'Sora'
USCRIPT_TAKRI                         = 153  # 'Takr'
USCRIPT_TANGUT                        = 154  # 'Tang'
USCRIPT_WOLEAI                        = 155  # 'Wole'
USCRIPT_ANATOLIAN_HIEROGLYPHS         = 156  # 'Hluw'
USCRIPT_KHOJKI                        = 157  # 'Khoj'
USCRIPT_TIRHUTA                       = 158  # 'Tirh'
USCRIPT_CAUCASIAN_ALBANIAN            = 159  # 'Aghb'
USCRIPT_MAHAJANI                      = 160  # 'Mahj'
USCRIPT_AHOM                          = 161  # 'Ahom'
USCRIPT_HATRAN                        = 162  # 'Hatr'
USCRIPT_MODI                          = 163  # 'Modi'
USCRIPT_MULTANI                       = 164  # 'Mult'
USCRIPT_PAU_CIN_HAU                   = 165  # 'Pauc'
USCRIPT_SIDDHAM                       = 166  # 'Sidd'
USCRIPT_ADLAM                         = 167  # 'Adlm'
USCRIPT_BHAIKSUKI                     = 168  # 'Bhks'
USCRIPT_MARCHEN                       = 169  # 'Marc'
USCRIPT_NEWA                          = 170  # 'Newa'
USCRIPT_OSAGE                         = 171  # 'Osge'
USCRIPT_HAN_WITH_BOPOMOFO             = 172  # 'Hanb'
USCRIPT_JAMO                          = 173  # 'Jamo'
USCRIPT_SYMBOLS_EMOJI                 = 174  # 'Zsye'
USCRIPT_MASARAM_GONDI                 = 175  # 'Gonm'
USCRIPT_SOYOMBO                       = 176  # 'Soyo'
USCRIPT_ZANABAZAR_SQUARE              = 177  # 'Zanb'
USCRIPT_DOGRA                         = 178  # 'Dogr'
USCRIPT_GUNJALA_GONDI                 = 179  # 'Gong'
USCRIPT_MAKASAR                       = 180  # 'Maka'
USCRIPT_MEDEFAIDRIN                   = 181  # 'Medf'
USCRIPT_HANIFI_ROHINGYA               = 182  # 'Rohg'
USCRIPT_SOGDIAN                       = 183  # 'Sogd'
USCRIPT_OLD_SOGDIAN                   = 184  # 'Sogo'
USCRIPT_ELYMAIC                       = 185  # 'Elym'
USCRIPT_NYIAKENG_PUACHUE_HMONG        = 186  # 'Hmnp'
USCRIPT_NANDINAGARI                   = 187  # 'Nand'
USCRIPT_WANCHO                        = 188  # 'Wcho'
USCRIPT_CHORASMIAN                    = 189  # 'Chrs'
USCRIPT_DIVES_AKURU                   = 190  # 'Diak'
USCRIPT_KHITAN_SMALL_SCRIPT           = 191  # 'Kits'
USCRIPT_YEZIDI                        = 192  # 'Yezi'

USCRIPT_CODE_LIMIT = 193

scriptCodes = {
    USCRIPT_COMMON: 'Zyyy',
    USCRIPT_INHERITED: 'Zinh', # "Code for inherited script", for non-spacing combining marks; also Qaai
    USCRIPT_ARABIC: 'Arab',
    USCRIPT_ARMENIAN: 'Armn',
    USCRIPT_BENGALI: 'Beng',
    USCRIPT_BOPOMOFO: 'Bopo',
    USCRIPT_CHEROKEE: 'Cher',
    USCRIPT_COPTIC: 'Copt',
    USCRIPT_CYRILLIC: 'Cyrl',
    USCRIPT_DESERET: 'Dsrt',
    USCRIPT_DEVANAGARI: 'Deva',
    USCRIPT_ETHIOPIC: 'Ethi',
    USCRIPT_GEORGIAN: 'Geor',
    USCRIPT_GOTHIC: 'Goth',
    USCRIPT_GREEK: 'Grek',
    USCRIPT_GUJARATI: 'Gujr',
    USCRIPT_GURMUKHI: 'Guru',
    USCRIPT_HAN: 'Hani',
    USCRIPT_HANGUL: 'Hang',
    USCRIPT_HEBREW: 'Hebr',
    USCRIPT_HIRAGANA: 'Hira',
    USCRIPT_KANNADA: 'Knda',
    USCRIPT_KATAKANA: 'Kana',
    USCRIPT_KHMER: 'Khmr',
    USCRIPT_LAO: 'Laoo',
    USCRIPT_LATIN: 'Latn',
    USCRIPT_MALAYALAM: 'Mlym',
    USCRIPT_MONGOLIAN: 'Mong',
    USCRIPT_MYANMAR: 'Mymr',
    USCRIPT_OGHAM: 'Ogam',
    USCRIPT_OLD_ITALIC: 'Ital',
    USCRIPT_ORIYA: 'Orya',
    USCRIPT_RUNIC: 'Runr',
    USCRIPT_SINHALA: 'Sinh',
    USCRIPT_SYRIAC: 'Syrc',
    USCRIPT_TAMIL: 'Taml',
    USCRIPT_TELUGU: 'Telu',
    USCRIPT_THAANA: 'Thaa',
    USCRIPT_THAI: 'Thai',
    USCRIPT_TIBETAN: 'Tibt',
    USCRIPT_CANADIAN_ABORIGINAL: 'Cans',
    USCRIPT_UCAS: 'Cans',
    USCRIPT_YI: 'Yiii',
    
    # New scripts in Unicode 3.2
    USCRIPT_TAGALOG: 'Tglg',
    USCRIPT_HANUNOO: 'Hano',
    USCRIPT_BUHID: 'Buhd',
    USCRIPT_TAGBANWA: 'Tagb',
    
    # New scripts in Unicode 4
    USCRIPT_BRAILLE: 'Brai',
    USCRIPT_CYPRIOT: 'Cprt',
    USCRIPT_LIMBU: 'Limb',
    USCRIPT_LINEAR_B: 'Linb',
    USCRIPT_OSMANYA: 'Osma',
    USCRIPT_SHAVIAN: 'Shaw',
    USCRIPT_TAI_LE: 'Tale',
    USCRIPT_UGARITIC: 'Ugar',
    
    # New scripts in Unicode 4.0.1
    USCRIPT_KATAKANA_OR_HIRAGANA: 'Hrkt',
    
    # New scripts in Unicode 4.1
    USCRIPT_BUGINESE: 'Bugi',
    USCRIPT_GLAGOLITIC: 'Glag',
    USCRIPT_KHAROSHTHI: 'Khar',
    USCRIPT_SYLOTI_NAGRI: 'Sylo',
    USCRIPT_NEW_TAI_LUE: 'Talu',
    USCRIPT_TIFINAGH: 'Tfng',
    USCRIPT_OLD_PERSIAN: 'Xpeo',
    
    # New script codes from Unicode and ISO 15924
    USCRIPT_BALINESE: 'Bali',
    USCRIPT_BATAK: 'Batk',
    USCRIPT_BLISSYMBOLS: 'Blis',
    USCRIPT_BRAHMI: 'Brah',
    USCRIPT_CHAM: 'Cham',
    USCRIPT_CIRTH: 'Cirt',
    USCRIPT_OLD_CHURCH_SLAVONIC_CYRILLIC: 'Cyrs',
    USCRIPT_DEMOTIC_EGYPTIAN: 'Egyd',
    USCRIPT_HIERATIC_EGYPTIAN: 'Egyh',
    USCRIPT_EGYPTIAN_HIEROGLYPHS: 'Egyp',
    USCRIPT_KHUTSURI: 'Geok',
    USCRIPT_SIMPLIFIED_HAN: 'Hans',
    USCRIPT_TRADITIONAL_HAN: 'Hant',
    USCRIPT_PAHAWH_HMONG: 'Hmng',
    USCRIPT_OLD_HUNGARIAN: 'Hung',
    USCRIPT_HARAPPAN_INDUS: 'Inds',
    USCRIPT_JAVANESE: 'Java',
    USCRIPT_KAYAH_LI: 'Kali',
    USCRIPT_LATIN_FRAKTUR: 'Latf',
    USCRIPT_LATIN_GAELIC: 'Latg',
    USCRIPT_LEPCHA: 'Lepc',
    USCRIPT_LINEAR_A: 'Lina',
    USCRIPT_MANDAIC: 'Mand',
    USCRIPT_MANDAEAN: 'Mand',
    USCRIPT_MAYAN_HIEROGLYPHS: 'Maya',
    USCRIPT_MEROITIC_HIEROGLYPHS: 'Mero',
    USCRIPT_MEROITIC: 'Mero',
    USCRIPT_NKO: 'Nkoo',
    USCRIPT_ORKHON: 'Orkh',
    USCRIPT_OLD_PERMIC: 'Perm',
    USCRIPT_PHAGS_PA: 'Phag',
    USCRIPT_PHOENICIAN: 'Phnx',
    USCRIPT_MIAO: 'Plrd',
    USCRIPT_PHONETIC_POLLARD: 'Plrd',
    USCRIPT_RONGORONGO: 'Roro',
    USCRIPT_SARATI: 'Sara',
    USCRIPT_ESTRANGELO_SYRIAC: 'Syre',
    USCRIPT_WESTERN_SYRIAC: 'Syrj',
    USCRIPT_EASTERN_SYRIAC: 'Syrn',
    USCRIPT_TENGWAR: 'Teng',
    USCRIPT_VAI: 'Vaii',
    USCRIPT_VISIBLE_SPEECH: 'Visp',
    USCRIPT_CUNEIFORM: 'Xsux',
    USCRIPT_UNWRITTEN_LANGUAGES: 'Zxxx',
    USCRIPT_UNKNOWN: 'Zzzz', # Unknown="Code for uncoded script", for unassigned code points
    USCRIPT_CARIAN: 'Cari',
    USCRIPT_JAPANESE: 'Jpan',
    USCRIPT_LANNA: 'Lana',
    USCRIPT_LYCIAN: 'Lyci',
    USCRIPT_LYDIAN: 'Lydi',
    USCRIPT_OL_CHIKI: 'Olck',
    USCRIPT_REJANG: 'Rjng',
    USCRIPT_SAURASHTRA: 'Saur',
    USCRIPT_SIGN_WRITING: 'Sgnw',
    USCRIPT_SUNDANESE: 'Sund',
    USCRIPT_MOON: 'Moon',
    USCRIPT_MEITEI_MAYEK: 'Mtei',
    USCRIPT_IMPERIAL_ARAMAIC: 'Armi',
    USCRIPT_AVESTAN: 'Avst',
    USCRIPT_CHAKMA: 'Cakm',
    USCRIPT_KOREAN: 'Kore',
    USCRIPT_KAITHI: 'Kthi',
    USCRIPT_MANICHAEAN: 'Mani',
    USCRIPT_INSCRIPTIONAL_PAHLAVI: 'Phli',
    USCRIPT_PSALTER_PAHLAVI: 'Phlp',
    USCRIPT_BOOK_PAHLAVI: 'Phlv',
    USCRIPT_INSCRIPTIONAL_PARTHIAN: 'Prti',
    USCRIPT_SAMARITAN: 'Samr',
    USCRIPT_TAI_VIET: 'Tavt',
    USCRIPT_MATHEMATICAL_NOTATION: 'Zmth',
    USCRIPT_SYMBOLS: 'Zsym',
    USCRIPT_BAMUM: 'Bamu',
    USCRIPT_LISU: 'Lisu',
    USCRIPT_NAKHI_GEBA: 'Nkgb',
    USCRIPT_OLD_SOUTH_ARABIAN: 'Sarb',
    USCRIPT_BASSA_VAH: 'Bass',
    USCRIPT_DUPLOYAN: 'Dupl',
    USCRIPT_ELBASAN: 'Elba',
    USCRIPT_GRANTHA: 'Gran',
    USCRIPT_KPELLE: 'Kpel',
    USCRIPT_LOMA: 'Loma',
    USCRIPT_MENDE: 'Mend',
    USCRIPT_MEROITIC_CURSIVE: 'Merc',
    USCRIPT_OLD_NORTH_ARABIAN: 'Narb',
    USCRIPT_NABATAEAN: 'Nbat',
    USCRIPT_PALMYRENE: 'Palm',
    USCRIPT_KHUDAWADI: 'Sind',
    USCRIPT_SINDHI: 'Sind',
    USCRIPT_WARANG_CITI: 'Wara',
    USCRIPT_AFAKA: 'Afak',
    USCRIPT_JURCHEN: 'Jurc',
    USCRIPT_MRO: 'Mroo',
    USCRIPT_NUSHU: 'Nshu',
    USCRIPT_SHARADA: 'Shrd',
    USCRIPT_SORA_SOMPENG: 'Sora',
    USCRIPT_TAKRI: 'Takr',
    USCRIPT_TANGUT: 'Tang',
    USCRIPT_WOLEAI: 'Wole',
    USCRIPT_ANATOLIAN_HIEROGLYPHS: 'Hluw',
    USCRIPT_KHOJKI: 'Khoj',
    USCRIPT_TIRHUTA: 'Tirh',
    USCRIPT_CAUCASIAN_ALBANIAN: 'Aghb',
    USCRIPT_MAHAJANI: 'Mahj',
    USCRIPT_AHOM: 'Ahom',
    USCRIPT_HATRAN: 'Hatr',
    USCRIPT_MODI: 'Modi',
    USCRIPT_MULTANI: 'Mult',
    USCRIPT_PAU_CIN_HAU: 'Pauc',
    USCRIPT_SIDDHAM: 'Sidd',
    USCRIPT_ADLAM: 'Adlm',
    USCRIPT_BHAIKSUKI: 'Bhks',
    USCRIPT_MARCHEN: 'Marc',
    USCRIPT_NEWA: 'Newa',
    USCRIPT_OSAGE: 'Osge',
    USCRIPT_HAN_WITH_BOPOMOFO: 'Hanb',
    USCRIPT_JAMO: 'Jamo',
    USCRIPT_SYMBOLS_EMOJI: 'Zsye',
    USCRIPT_MASARAM_GONDI: 'Gonm',
    USCRIPT_SOYOMBO: 'Soyo',
    USCRIPT_ZANABAZAR_SQUARE: 'Zanb',
    USCRIPT_DOGRA: 'Dogr',
    USCRIPT_GUNJALA_GONDI: 'Gong',
    USCRIPT_MAKASAR: 'Maka',
    USCRIPT_MEDEFAIDRIN: 'Medf',
    USCRIPT_HANIFI_ROHINGYA: 'Rohg',
    USCRIPT_SOGDIAN: 'Sogd',
    USCRIPT_OLD_SOGDIAN: 'Sogo',
    USCRIPT_ELYMAIC: 'Elym',
    USCRIPT_NYIAKENG_PUACHUE_HMONG: 'Hmnp',
    USCRIPT_NANDINAGARI: 'Nand',
    USCRIPT_WANCHO: 'Wcho',
    USCRIPT_CHORASMIAN: 'Chrs',
    USCRIPT_DIVES_AKURU: 'Diak',
    USCRIPT_KHITAN_SMALL_SCRIPT: 'Kits',
    USCRIPT_YEZIDI: 'Yezi',
}