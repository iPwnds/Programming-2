import pytest
import student

@pytest.mark.parametrize(("string", "expected"), [
        ('a@c.com', ["a@c.com"]),
        ('111@AFF.com', ["111@AFF.com"]), 
        ('*a@b*', ["a@b"]),
        ("""
        a@c.com fsjdf jfslk fkls fjl df
        jalfkj b@d.be fjdlkf jfkljdlkf
        qpoiopc fdfqpof ifppopo fkpqo
        qfjlkl xyz@ppp.fr jkfljqlkj
        opfpqsjkl<...@...>
        """, ["a@c.com", "b@d.be", "xyz@ppp.fr", "...@..." ])
])
def test_function(string, expected):
    function_name = 'scrape_email_addresses'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    student_function = getattr(student, function_name)
    actual = student_function(string)

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"
