"""/
HeaderToPython. Translate ICU .h files to Pyton

Created on May 6, 2021

@author Eric Mader
"""

from datetime import datetime
import os
import re

#
# Making the translation "pretty" is a secondary goal - it just needs
# to be functional. i.e. don't worry about comments and blank lines.
#
# Make a routine that returns non-blank lines w/ comments stripped.
# (Maybe make comments at the end of a non-blank line available)
# (Maybe have a way to get comments from lines only have a commenyt)
#

def firstToken(line):
    return re.findall(r"([^\s]+)", line)[0]

def getTrailingComment(line):
    comment = None
    if (m := re.search(r"/\*\*?(.+?)\*/", line)) or (m := re.search(r"//\s*([^$]+)$", line)):
        comment = line[m.start(1):m.end(1)]
        line = line[:m.start()].strip()

    return line, comment

def nextLine(file):
    inComment = False
    inConditional = False
    inMacro = False
    while (line := file.readline()):
        line = line.strip()
        if not line: continue  # skip over empty lines
        if line.startswith("//"): continue  # skip full-line comment
        if line.startswith("/*"):
            if line.endswith("*/"):
                continue  # skip a single line comment
            else:
                inComment = True
                continue

        if inComment:
            if line.endswith("*/"):
                inComment = False
            continue

        if line.startswith("#if"):
            if not line.endswith("_H__"):
                inConditional = True
            continue  # ignore #ifndef __HEADER_H__

        if inConditional:
            if line.startswith("#endif"):
                inConditional = False
            continue

        if line.startswith("#endif"): continue  # ignore "endif for __HEADER_H__

        if line.startswith("#define") and line.endswith("\\"):
            inMacro = True
            macroLine = line[:-1]
            continue

        if inMacro:
            if not line.endswith("\\"):
                inMacro = False
                return getTrailingComment(macroLine + line)
            else:
                macroLine += line[:-1].strip()
            continue

        return getTrailingComment(line)
        # if (ix := line.find("//")) >= 0 or (ix := line.find("/*")) >= 0:
        #     line = line[:ix].strip()
        #
        # return line, comment

def test():
    headerFile = open("/Users/emader/Downloads/icu69/icu4c/source/common/unicode/uchar.h")

    while (nl := nextLine(headerFile)):
        line, comment = nl
        token = firstToken(line)
        # if token == "//":
        #     print(f"#{line[2:-1]}")
        # elif token.startswith("/*") and line.endswith("*/\n"):
        #     print(f"#{line[len(token):-3]}")
        if token == "#define":
            # optional argument list, optional value
            name, value = re.findall(r"#define (\w+(?:\(\w+(?:,\s*\w+)?\))?)(?:\s+(.+))?", line)[0]
            # should check if value is { xxx }...
            if value and not "(" in name:
                if comment:
                    print(f"{name} = {value}  # {comment}")
                else:
                    print(f"{name} = {value}")
        elif token == "enum" or (token == "typedef" and re.search(r"typedef\s+enum\s*\w*\s*\{", line)):
            nextValue = 0
            variables = {}
            prevName = None
            while (elc := nextLine(headerFile)):
                eline, comment = elc
                if re.search(r"\}\s*\w*\s*;", eline): break
                # if not eline:
                #     print()
                #     continue
                #
                # if eline.startswith("/*"):
                #     while (cline := headerFile.readline().strip()) != "*/":
                #         pass
                #     continue

                # an id followed by optional = value followed by optional comma
                name, value = re.findall(r"(\w+)(?:\s*=\s*([^,]+))?(?:,|\s)?", eline)[0]
                if not value:
                    value = str(nextValue)

                if comment:
                    print(f"{name} = {value}  # {comment}")
                else:
                    print(f"{name} = {value}")

                #
                # Maybe keep all the names and check for value as an expression
                # involving any previous names...
                #
                # e.g.:
                # U_EXTENDED_CHAR_NAME = U_UNICODE_CHAR_NAME+2,
                # U_CHAR_NAME_ALIAS
                #
                # (Might have to use eval() to make this work...)
                #
                # if value != prevName:

                if re.fullmatch(r"[0-9]+", value):
                    intValue = int(value)
                elif re.fullmatch(r"0[xX][0-9a-fA-F]+", value):
                    intValue = int(value, 16)
                else:
                    intValue = eval(value, variables)

                variables[name] = intValue
                nextValue = intValue + 1

                prevName = name
        # print(line)


if __name__ == "__main__":
    test()
