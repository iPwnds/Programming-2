import pytest
import student

@pytest.mark.parametrize(("string", "expected"), [
    ('1/2/3', '2/1/3'),
    ('12/11/2019', '11/12/2019'), 
    ('12/11/2019 6/7/1899', '11/12/2019 7/6/1899'),
    ('12/11/2019 fjklfjl 6/7/1899','11/12/2019 fjklfjl 7/6/1899')
])
def test_function(string, expected):
    function_name = 'correct_dates'
    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name}")

    student_function = getattr(student, function_name)
    actual = student_function(string)

    assert expected == actual, f"Wrong result for {string}, expected {expected}, received {actual}"
