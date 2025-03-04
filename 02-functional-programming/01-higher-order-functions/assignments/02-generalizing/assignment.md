# Generalizing

## Movies
For these exercises there are no tests. Paste the contents of `movie.py` into your `student.py` file and call your
functions with the list movies to test whether your code gives the expected results.

### count_movies_from_year
The following function counts the number of movies in this year (2025). Generalize it into a function
`count_movies_from_year` so that it can count the number of movies in any given year.

```python
def count_movies_from_current_year(movies):
    counter = 0
    for movie in movies:
        if movie.year == 2025:
            counter += 1
    return counter
```

### select_movies_with_actor
The following function returns a list with all the movies in which "Tom Hanks" played. Generalize it to more general
function `select_movies_with_actor` that can select all the movies of any given actor:
```python
def select_movies_with_tom_hanks(movies):
    result_movies = []
    for movie in movies:
        if "Tom Hanks" in movies.actors:
            result_movies.append(movie)
    return result_movies
```

### sum_movie_duration_from_period
The following function sums the total duration of all movies made in the 90's. Generalize it into a function `sum_movie_duration_from_period` that can sum the duration of all movies in any given time period (defined by a given
start- and end-year)
```python
def sum_movie_duration_in_90s(movies):
    total_duration = 0
    for movie in movies:
        if movie.year >= 1990 and movie.year < 2000:
            total_duration += movie.duration
    return total_duration
```

### get_directors_for_actor
The following function returns a set of directors that worked with the actor "Tom Hanks". Can you generalize it into a
function `get_directors_of_actor` that can return a list of directors that have worked with any given actor?
```python
def get_directors_of_tom_hanks(movies):
    directors = []
    for movie in movies:
        if "Tom Hanks" in movie.actors:
            directors.append(movie.director)
    return directors
```

## Other

### find_string_starting_with
The given function returns the first string in a list that starts with the letter 'a'. Generalize it to the function
`find_string_starting_with(strings, letter)` so that it can find the first string starting with any given letter:
```python
def find_string_starting_with_a(strings):
    for string in strings:
        if len(string) != 0 and string[0].lower() == "a":
            return string
    return None
```

### find_number_greater_than
The given function returns the first number in a list that is greater than 100. Generalize it to the function
`find_number_greater_than(numbers, threshold)` so that it can find the first number that is greater than any given
number:
```python
def find_number_greater_than_100(numbers):
    for number in numbers:
        if number > 100:
            return number
    return None
```
