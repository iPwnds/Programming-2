from itertools import islice
import student

def fizzbuzz():
    current = 1
    while True:
        result = ''
        if current % 3 == 0:
            result += 'fizz'
        if current % 5 == 0:
            result += 'buzz'
        # If result is still empty, set it to str(current)
        result = result or str(current)
        yield result
        current += 1



def test_fizzbuzz():
    expected = islice(fizzbuzz(), 1000)
    actual = islice(student.fizzbuzz(), 1000)
    assert list(expected) == list(actual)
