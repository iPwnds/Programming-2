import pytest
import student

@pytest.mark.parametrize(("string", "expected"), [
    ("", False),
    ("a", False),
    ("aa", False),
    ("b", False),
    ("bb", False),
    ("abc", True),
    ("abcd", False)
])  
def test_function(string, expected):
    function_name = 'equals_abc'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    student_function = getattr(student, function_name)
    actual = bool(student_function(string))

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"
