import pytest
import student

@pytest.mark.parametrize(("string", "expected"), [
    ("", False),
    ("a", False),
    ("aa", False),
    ("aaaaa", False),
    ("bbbb", True),
    ("bbbbba", False)
])
def test_function(string, expected):
    function_name = 'one_or_more_b'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    student_function = getattr(student, function_name)
    actual = bool(student_function(string))

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"
