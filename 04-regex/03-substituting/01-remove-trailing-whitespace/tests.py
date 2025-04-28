import pytest
import student

@pytest.mark.parametrize(("string", "expected"), [
        ('fdjfkld jfjs fjdslfk'.strip(), 'fdjfkld jfjs fjdslfk'),
        ('fdjfkld jfjs fjdslfk ', 'fdjfkld jfjs fjdslfk'),
        ('fdjfkld jfjs fjdslfk\t', 'fdjfkld jfjs fjdslfk'),
        ('fdjfkld jfjs fjdslfk       ', 'fdjfkld jfjs fjdslfk'),
        ('x  \ny   ', 'x\ny'),
        ('''
        fdf qqip saofp k        \t\x20
        fjdklfj f sfjslkf     \x20
        fdjfkldjf      \x20''',  
        '''
        fdf qqip saofp k
        fjdklfj f sfjslkf
        fdjfkldjf''')
])
def test_function(string, expected):
    function_name = 'remove_trailing_whitespace'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    student_function = getattr(student, function_name)
    actual = student_function(string)

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"
