import pytest
import student

@pytest.mark.parametrize(("string", "expected"), [
    ("""
        <a href="a">fdf</a>
        fjklfjls
        <a href="b">qff</a>
        djqkljl
        <a href="abc">dfdg</a>
        fdjflkjdlf
        <a href="fiop">fdghh</a>
        fjdlfjlk
        <a href=""></a>
    """, ['a', 'b', 'abc', 'fiop', '']),
    ("""
        <a href="url1">text1</a>
        <a href="url2">text2</a>
        <a href="url3">text3</a>
    """, ['url1', 'url2', 'url3']),
])
def test_function(string, expected):
    function_name = 'collect_links'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    student_function = getattr(student, function_name)
    actual = student_function(string)

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"