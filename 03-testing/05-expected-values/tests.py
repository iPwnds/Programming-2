import pytest
import itertools
from mergesort import split_in_two, merge_sorted, merge_sort

# --- Tests for split_in_two ---

@pytest.mark.parametrize('ns', [
    list(range(n)) for n in range(101)
])
def test_split_in_two(ns):
    left, right = split_in_two(ns)
    # The concatenation should equal the original list
    assert left + right == ns
    # Lengths differ by at most one
    assert abs(len(left) - len(right)) <= 1

# --- Tests for merge_sorted ---

@pytest.mark.parametrize('left', [
    [],
    [1],
    [1, 2, 3],
    [2, 5, 5, 9],
    [4, 10, 15],
])
@pytest.mark.parametrize('right', [
    [],
    [1],
    [3, 4, 7],
    [2, 2, 8, 9],
    [5, 11, 20],
])
def test_merge_sorted(left, right):
    result = merge_sorted(left, right)
    # Check result is sorted and equal to sorted concatenation of left + right
    assert result == sorted(left + right)

# --- Tests for merge_sort ---

def generate_permutations(lst):
    return list(itertools.permutations(lst))

@pytest.mark.parametrize('expected', [
    [],
    [1],
    [1, 1, 1],
    [1, 2, 3],
    [3, 5, 7, 9],
    [2, 2, 4, 4, 6],
])
def test_merge_sort(expected):
    permutations = generate_permutations(expected)
    for ns in permutations:
        result = merge_sort(list(ns))
        assert result == expected