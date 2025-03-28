import pytest
import student

@pytest.mark.parametrize(("string", "expected"), [
    ('', False),
    ('ababa', True),
    ('xyxyx', True),
    ('aabbaabbaa', True),
    ('ababc', False),
    ('babab', True),
    ('ababax', False),
    ('aaaaa', True),
    ('12121', True),
    ('23212', False)
])
def test_function(string, expected):
    function_name = 'ababa'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    student_function = getattr(student, function_name)
    actual = bool(student_function(string))

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"
