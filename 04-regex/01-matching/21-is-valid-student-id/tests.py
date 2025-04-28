import pytest
import student

@pytest.mark.parametrize(("string", "expected"), [
    ('', False),
    ('r1234567', True),
    ('r123456', False),
    ('r12345678', False),
    ('s12345678', False),
    ('s1234567', True),
    ('s123456', False),
    ('q1234567', False),
    ('R1234567', True),
    ('R123456', False),
    ('R12345678', False),
    ('S12345678', False),
    ('S1234567', True),
    ('S123456', False),
    ('Q1234567', False),
    (' r1234567 ', False),
    ('r4545458', True),
    ('rabcdefg', False)
])
def test_function(string, expected):
    function_name = 'is_valid_student_id'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    student_function = getattr(student, function_name)
    actual = bool(student_function(string))

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"
