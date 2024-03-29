"""
Functions for testing property enumeration

Created on August 17, 2021

@author Eric Mader
"""

import typing

def testEnum(enumerator: typing.Callable[[int, int], typing.Iterator[tuple[range, typing.Any]]], start: int, limit: int, expectedFunction: typing.Callable[[int], int], valueMapper: typing.Optional[typing.Callable[[int], typing.Any]] = None):
    if not valueMapper: valueMapper = lambda v: v

    results = [(range, value) for range, value in enumerator(start, limit)]

    firstRange, _ = results[0]
    lastRange, _ = results[-1]
    assert firstRange.start == start, f"enumeration started at {firstRange.start:04X}, should have started at {start:04X}."
    assert lastRange.stop == limit, f"enumeration stopped at {lastRange.stop:04X}, should have stopped at {limit:04X}."

    for valueRange, value in results:
        for ch in valueRange:
            expectedValue = expectedFunction(ch)
            assert value == expectedValue, f"{ch:04X}: got value {valueMapper(value)}, expected {valueMapper(expectedValue)}."
