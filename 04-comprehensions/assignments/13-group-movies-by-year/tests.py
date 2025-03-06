import sys
sys.path.append('..')
import pytest
from movie import *
import student


def test_titles():
    module = student
    function_name = 'group_movies_by_year'

    if not hasattr(module, function_name):
        pytest.skip()

    def reference_function(movies):
        return {
            year: [movie.title for movie in movies if movie.year == year]
            for year in {movie.year for movie in movies}
        }

    actual_function = getattr(module, function_name)

    reference_result = reference_function(movies)
    actual_result = actual_function(movies)

    assert actual_result == reference_result
