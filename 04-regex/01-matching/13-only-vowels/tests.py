import pytest
import student


@pytest.mark.parametrize(("string", "expected"), [
    ('', True),
    ('a', True),
    ('e', True),
    ('i', True),
    ('o', True),
    ('u', True),
    ('aaaa', True),
    ('aeiou', True),
    ('x', False),
    ('y', False),
    ('aebou', False),
])
def test_function(string, expected):
    function_name = 'only_vowels'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    student_function = getattr(student, function_name)
    actual = bool(student_function(string))

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"
