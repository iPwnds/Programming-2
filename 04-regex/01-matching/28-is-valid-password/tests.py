import pytest
import student
import re

@pytest.mark.parametrize("string", [
    *[f'{a}{b}{c}{d}'
      for a in ['A', 'FQPIQFK', 'fjkla']
      for b in ['g', 'pfoajaz', '9512']
      for c in ['+', '-', '*', '/', '.', '@', 'F']
      for d in ['1', '4312948', 'FQZJFP'] ],
    'ABCabc123@+/',
    'ABCabcA123A@+A/',
    'ABCabc11123@+/',
])
def test_function(string):
    function_name = 'is_valid_password'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    student_function = getattr(student, function_name)

    actual = bool(student_function(string))
    expected = bool(sol_is_valid_password(string))

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"

def sol_is_valid_password(string):
    positive_regexes = [
        r'.{12,}',
        r'[0-9]',
        r'[a-z]',
        r'[A-Z]',
        r'[-+/.*@]',
    ]

    negative_regexes = [
        r'(.)\1{2}',
        r'(.)(.*\1){3}'
    ]

    for regex in positive_regexes:
        if not re.search(regex, string):
            return False

    for regex in negative_regexes:
        if re.search(regex, string):
            return False

    return True
