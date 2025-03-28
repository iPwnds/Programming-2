import pytest
import student

@pytest.mark.parametrize(("string", "expected"), [
    ('', False),
    ('00:00:00', True),
    ('00:00:00.000', True),
    ('12:34:56.888', True),
    ('2:34:56.888', False),
    ('123:34:56.888', False),
    ('12:4:56.888', False),
    ('12:345:56.888', False),
    ('12:34:6.888', False),
    ('12:34:567.888', False),
    ('12:34:56.88', False),
    ('12:34:56.8888', False),
    ('ab:00:00', False)
])
def test_function(string, expected):
    function_name = 'is_valid_time'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    student_function = getattr(student, function_name)
    actual = bool(student_function(string))

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"
