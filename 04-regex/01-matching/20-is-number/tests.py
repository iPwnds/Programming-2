import pytest
import student

@pytest.mark.parametrize(("string", "expected"), [
    ('', False),
    ('0', True),
    ('1', True),
    ('2', True),
    ('3', True),
    ('4', True),
    ('5', True),
    ('6', True),
    ('7', True),
    ('8', True),
    ('9', True),
    ('12.34', True),
    ('12.', False),
    ('.23', False),
    ('8394018', True),
    ('38209.83491', True),
    ('1111111,1111', False),
    ('1111111a.1111', False)
])
def test_function(string, expected):
    function_name = 'is_number'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    student_function = getattr(student, function_name)
    actual = bool(student_function(string))

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"
