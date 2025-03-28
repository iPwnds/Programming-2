import pytest
import student

@pytest.mark.parametrize(("string", "expected"), [
    ('', False),
    ('a@ucll.be', True),
    ('a.b@ucll.be', True),
    ('a@student.ucll.be', True),
    ('1@student.ucll.be', True),
    ('a.b@student.ucll.be', True),
    ('a1.b@student.ucll.be', True),
    ('1.b@student.ucll.be', True),
    ('1.5b@student.ucll.be', True),
    ('abc.def@gmail.com', False),
    ('abc.def ucll.be', False),
    ('....@ucll.be', True)
])
def test_function(string, expected):
    function_name = 'is_valid_email_address'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    student_function = getattr(student, function_name)
    actual = bool(student_function(string))

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"
