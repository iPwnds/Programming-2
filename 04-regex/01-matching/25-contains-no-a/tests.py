import pytest
import student

@pytest.mark.parametrize(("string", "expected"), [
    ('', True),
    ('a', False),
    ('x', True),
    ('aaaa', False),
    ('bbbbbbbbb', True),
    ('dkofgpq', True),
    ('jfopajkl', False)
])
def test_function(string, expected):
    function_name = 'contains_no_a'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    student_function = getattr(student, function_name)
    actual = bool(student_function(string))

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"
