import pytest
import student

@pytest.mark.parametrize(("string", "expected"), [
    ('', False),
    ('a', False),
    ('b', False),
    ('aa', True),
    ('ab', False),
    ('abab', False),
    ('xyzxyz', False),
    ('ababa', False),
    ('123123123', False),
    ('  ', True),
    ('   ', False)
])
def test_function(string, expected):
    function_name = 'twice_repeated'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    student_function = getattr(student, function_name)
    actual = bool(student_function(string))

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"
