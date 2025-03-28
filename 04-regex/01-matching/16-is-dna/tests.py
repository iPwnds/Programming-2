import pytest
import student


@pytest.mark.parametrize(("string", "expected"), [
    ('', True),
    ('a', False),
    ('A', True),
    ('b', False),
    ('B', False),
    ('c', False),
    ('C', True),
    ('d', False),
    ('D', False),
    ('g', False),
    ('G', True),
    ('h', False),
    ('H', False),
    ('t', False),
    ('T', True),
    ('u', False),
    ('U', False),
    ('GATTACA', True),
    ('GARTACA', False)
])
def test_function(string, expected):
    function_name = 'is_dna'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    student_function = getattr(student, function_name)
    actual = bool(student_function(string))

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"
