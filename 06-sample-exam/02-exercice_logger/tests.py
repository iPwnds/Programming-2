import pytest
from starter_code import Swim

def test_constructor_success():
    swim = Swim(date="2025-05-20", distance=2.0, duration=30.0)
    assert swim.date == "2025-05-20"
    assert swim.distance == 2.0
    assert swim.duration == 30.0

def test_constructor_invalid_distance():
    with pytest.raises(ValueError):
        Swim("2025-05-20", 0.0, 30.0)

def test_constructor_invalid_duration():
    with pytest.raises(ValueError):
        Swim("2025-05-20", 2, 0)

def test_constructor_invalid_speed():
    with pytest.raises(ValueError):
        Swim("2025-05-20", 1, 5)

def test_constructor_invalid_date():
    with pytest.raises(ValueError):
        Swim("2025/05/20", 2, 30)

@pytest.mark.parametrize(
    "distance, duration, expected",
    [
        (1.0,  30.0,  80),
        (2.5,  45.0,  333),
        (0.5,  15.0,  40),
    ]
)
def test_calories(distance, duration, expected):
    swim = Swim("2025-05-20", distance, duration)
    assert swim.calories == expected


