import sys
sys.path.append('..')
import pytest
from movie import *
import student


def movies_from_year(movies, year):
    return [movie.title for movie in movies if movie.year == year]


def movies_with_actor(movies, actor):
    return [movie.title for movie in movies if actor in movie.actors]


def divisors(n):
    return [k for k in range(1, n+1) if n % k == 0]

functions = {
    'movies_from_year': movies_from_year,
    'movies_with_actor': movies_with_actor,
    'divisors': divisors,
}


@pytest.mark.parametrize('year', range(1950, 2050))
def test_movies_from_year(year):
    function_name = 'movies_from_year'
    args = [year]

    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name} in student module")

    solution_function = functions[function_name]
    student_function = getattr(student, function_name)

    solution_result = solution_function(movies, *args)
    student_result = student_function(movies, *args)

    assert student_result == solution_result


@pytest.mark.parametrize('actor', {actor for movie in movies for actor in movie.actors})
def test_movies_with_actor(actor):
    function_name = 'movies_with_actor'
    args = [actor]

    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name} in student module")

    solution_function = functions[function_name]
    student_function = getattr(student, function_name)

    solution_result = solution_function(movies, *args)
    student_result = student_function(movies, *args)

    assert student_result == solution_result


@pytest.mark.parametrize('n', [1, 2, 3, 97, 2400])
def test_divisors(n):
    function_name = 'divisors'
    args = [n]

    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name} in student module")

    solution_function = functions[function_name]
    student_function = getattr(student, function_name)

    solution_result = solution_function(*args)
    student_result = student_function(*args)

    assert student_result == solution_result
