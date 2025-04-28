import pytest
import student

@pytest.mark.parametrize(("string", "expected"), [
    ('<a href="xxx">lalala</a>', ("lalala", "xxx")),
    ('<a href="url">caption</a>', ("caption", "url")),
    ('<a>caption</a>', None),
    ('<a href="url">caption<a>', None),
    ('<a href=url>caption</a>', None),
    ('<a href="ajflk">iojfgkld</a>', ('iojfgkld', 'ajflk')),
    ('<a href="xxx">lalala', None),
    ('href="xxx">lalala<', None),
    ('<a href="xxx">lalala', None),
    ('href="xxx">lalala<', None)
])
def test_function(string, expected):
    function_name = 'parse_link'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    student_function = getattr(student, function_name)
    actual = student_function(string)

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"