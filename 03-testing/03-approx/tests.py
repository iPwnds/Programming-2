import pytest
from pytest import approx
from mystatistics import average

@pytest.mark.parametrize("ns, expected", [
    ([1, 2, 3], 2),
    ([10, 10, 10, 10], 10),
    ([0.1, 0.1, 0.1], 0.1),
    ([0.1, 0.2, 0.3], 0.2),
    ([100, 200, 300], 200),
])
def test_average(ns, expected):
    assert average(ns) == approx(expected, abs=0.01)