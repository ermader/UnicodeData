"""\
Tests for Trie enumerators

Created on June 17, 2020

@author Eric Mader
"""

def printEnumResults(results, valueFunction=None):
    if not valueFunction: valueFunction = lambda v: v

    resultRanges = []
    for valueRange, value in results:
        resultRanges.append(f"[{valueRange.start:04X}, {valueRange.stop:04X}]: {valueFunction(value)}")

    print(", ".join(resultRanges))

def testEnum(enumerator, start, limit, valueFunction, expectedFunction, valueMapper=None):
    if not valueMapper: valueMapper = lambda v: v

    print(f"Testing enumeration from {start:04X} to {limit:04X}:")
    results = [(range, value) for range, value in enumerator(start=start, limit=limit, valueFunction=valueFunction)]

    passed = True
    for valueRange, value in results:
        for ch in valueRange:
            expectedValue = expectedFunction(ch)
            if expectedValue != value:
                print(f"    {ch:04X}: got gc = {valueMapper(value)}, expected {valueMapper(expectedValue)}")
                passed = False

    (firstRange, _) = results[0]
    (lastRange, _) = results[-1]
    if firstRange.start < start:
        print(f"    enumeration started early at {firstRange.start:0xX}")
    elif firstRange.start > start:
        print(f"    enumeration started late at {firstRange.start}")

    if lastRange.stop < limit:
        print(f"    enumeration stopped early at {lastRange.stop:04X}")
    elif lastRange.stop > limit:
        print(f"    enumeration stopped late at {lastRange.stop:04X}")
    elif passed: print("    passed!")

