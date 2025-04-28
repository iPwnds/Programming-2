import pytest
import student


@pytest.mark.parametrize(("string", "expected"), [
    ("", True),
    ("abc", True),
    ("abcabc", True),
    ("abcabcabc", True),
    ("aabbccc", False),
    ("abcx", False),
    ("xabc", False),
    ("abca", False),
    ("abcab", False)
])
def test_function(string, expected):
    function_name = 'zero_or_more_abc'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    student_function = getattr(student, function_name)
    actual = bool(student_function(string))

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"
