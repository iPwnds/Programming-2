import pytest
import student

@pytest.mark.parametrize(("string", "expected"), [
    ('', ''),
    ('a', 'a'),
    ('aa', 'aa'),
    ('aa aa', 'aa'),
    ('aa a', 'aa a'),
    ('a a b b', 'a b'),
    ('aaa aaa bb bb c c', 'aaa bb c'),
    ('a b a b', 'a b a b'),
    ('a a a a b', 'a b')
])
def test_function(string, expected):
    function_name = 'remove_repeated_words'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    student_function = getattr(student, function_name)
    actual = student_function(string)

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"
