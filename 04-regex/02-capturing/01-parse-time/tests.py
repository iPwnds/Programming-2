import pytest
import student

@pytest.mark.parametrize(("string", "expected"), [
    ('00:00:00', (0, 0, 0, 0)),
    ('12:34:56', (12, 34, 56, 0)),
    ('12:34:56.000', (12, 34, 56, 0)),
    ('12:34:56.001', (12, 34, 56, 1)),
    ('12:34:56.491', (12, 34, 56, 491)),
    ('21:51:48.111', (21, 51, 48, 111)),
    ('', None),
    ('::', None),
    ('0:00:00', None),
    ('00:0:00', None),
    ('00:00:0', None),
    ('00:00:00.1', None),
    ('aa:bb:cc', None)
])
def test_function(string, expected):
    function_name = 'parse_time'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    student_function = getattr(student, function_name)
    actual = student_function(string)

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"
