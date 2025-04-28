import pytest
import student

@pytest.mark.parametrize(("string", "expected"), [
    ("", False),
    ("abc", False),
    ("abcabc", False),
    ("abc" * 9, False),
    ("abc" * 10, True),
    ("abc" * 11, True),
    ("abc" * 15, True),
    ("aabbccc", False),
    ("abcx", False),
    ("xabc", False),
    ("abca", False),
    ("abcab", False)
])
def test_function(string, expected):
    function_name = 'ten_or_more_abc'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    student_function = getattr(student, function_name)
    actual = bool(student_function(string))

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"
