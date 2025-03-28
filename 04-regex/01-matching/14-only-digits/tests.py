import pytest
import student


@pytest.mark.parametrize(("string", "expected"),[
    ('', True),
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
    ('00', True),
    ('11', True),
    ('22', True),
    ('33', True),
    ('44', True),
    ('55', True),
    ('66', True),
    ('77', True),
    ('88', True),
    ('99', True),
    ('48865', True),
    ('a', False),
    ('15 98', False),
    ('4879 ', False)
])
def test_function(string, expected):
    function_name = 'only_digits'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    student_function = getattr(student, function_name)
    actual = bool(student_function(string))

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"
