import pytest
from typing import List, Tuple
from onepoint.katas.flatten import flatten

test_case_1 = (
    (1, [2, 3], 4, 5, [6, [7]]),
    [1, 2, 3, 4, 5, 6, 7]
)

test_case_2 = (
    ('a', ['b', 2], 3, None, [[4], ['c']]),
    ['a', 'b', 2, 3, None, 4, 'c']
)


@pytest.mark.parametrize(
    "input, expected",
    [
        test_case_1,
        test_case_2
    ]
)
def test_flatten_should_flatten(input: Tuple, expected: List):
    # Given
    # When
    actual = flatten(input)

    # Then
    assert actual == expected
