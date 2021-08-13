'''\
Created on Apr 24, 2020

Build the unicode_data.db file.

@author: emader
'''

# The shelve method ends up taking as much time as parsing the .xml file.
# So, we should either leave well enough alone, or look at an optimized trie of some sort.

# def build():
#     start = timer()
#     _populateCharacterData()
#     end = timer()
#     print(f"Reading the Unicode Character Data File took {end - start} seconds.")
#
#     start = timer()
#     dataShelf = shelve.open(_dbPath, 'n')
#     dataShelf["ucd"] = _characterData
#     dataShelf.close()
#     end = timer()
#     print(f"Writing unicode_data.db took {end - start} seconds.")


if __name__ == "__main__":
    pass
    # UnicodeData.build()