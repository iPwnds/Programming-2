import pytest
import student

@pytest.mark.parametrize(("string", "expected"), [
    ('', False),
    ('1', False),
    ('2', False),
    ('41', False),
    ('135', True),
    ('1451', True),
    ('645040', True),
    ('1 2 3', True),
    ('64x65p1', True),
    ('abc', False)
])
def test_function(string, expected):
    function_name = 'contains_three_digits'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    student_function = getattr(student, function_name)
    actual = bool(student_function(string))

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"
