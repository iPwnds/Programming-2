import pytest
import student

@pytest.mark.parametrize(("string", "expected"), [
    ('', False),
    ('a', False),
    ('aa', False),
    ('aaa', True),
    ('abab', False),
    ('ababab', True),
    ('123123', False),
    ('123123123', True),
    ('1111', False),
    ('123123123123', False),
    ('111111', True),
    ('  ', False),
    ('   ', True)
])
def test_function(string, expected):
    function_name = 'thrice_repeated'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    student_function = getattr(student, function_name)
    actual = bool(student_function(string))

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"
