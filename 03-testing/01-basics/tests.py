from intervals import overlapping_intervals


def test_overlapping_intervals():
    # Regular overlaps
    assert overlapping_intervals((1, 5), (3, 6))
    assert overlapping_intervals((3, 6), (1, 5))
    assert overlapping_intervals((2, 5), (5, 10))
    assert overlapping_intervals((5, 10), (2, 5))

    # Non-overlapping
    assert not overlapping_intervals((2, 5), (7, 10))
    assert not overlapping_intervals((7, 10), (2, 5))

    # Touching at a single point
    assert overlapping_intervals((2, 5), (5, 5))  # (5, 5) is a valid point overlap
    assert not overlapping_intervals((6, 6), (7, 7))  # two single-point intervals, not overlapping

    # Empty intervals
    assert not overlapping_intervals((8, 6), (6, 9))  # first is empty
    assert not overlapping_intervals((3, 2), (1, 5))  # first is empty
    assert not overlapping_intervals((1, 5), (7, 6))  # second is empty
    assert not overlapping_intervals((7, 6), (5, 4))  # both empty

    # Fully overlapping
    assert overlapping_intervals((2, 8), (3, 6))
    assert overlapping_intervals((3, 6), (2, 8))

    # One interval inside the other
    assert overlapping_intervals((2, 8), (4, 5))
    assert overlapping_intervals((4, 5), (2, 8))

    # Identical intervals
    assert overlapping_intervals((2, 5), (2, 5))