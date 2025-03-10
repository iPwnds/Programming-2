# Generalizing functions

## Example: Counting movies
The file movie.py defines the class Movie. In this file you'll also find a list with a bunch of those `Movie` objects.

Say we're analyzing this `Movie` database and we want to determine how many movies a certain director has made.
We can then write the following code:
```python
no_movies_by_spielberg = 0
for movie in movies:
    if movie.director == "Steven Spielberg":
        no_movies_by_spielberg += 1
```
For some reason, we need this in multiple places.
We build a function around it so we don't need to repeat this code:

```python
def count_movies_by_spielberg(movies):
    no_movies_by_spielberg = 0
    for movie in movies:
        if movie.director == "Steven Spielberg":
            no_movies_by_spielberg += 1
    return no_movies_by_spielberg
```

Next, we also need to determine how many of our movies were made by the Coen brothers. We can write a similar function:
```python
def count_movies_by_coen_brothers(movies):
    no_movies_by_coen_brothers = 0
    for movie in movies:
        if movie.director == "Coen Brothers":
            no_movies_by_coen_brothers += 1
    return no_movies_by_coen_brothers
```
As you can see, this is basically the same code as the code we had to write for Spielberg, so ideally we'd like to
reuse the previous function we wrote somehow, to also be able to count movies made by the Coen brothers. Unfortunately,
the name `'Steven Spielberg'` is hard coded into this function, so we're out of luck. Or are we?

Let's see if we can change (or refactor) this function slightly, so that is more generally usable:

First, instead of having the director name directly in our if-statement, we could extract it into a separate
variable:
```python
def count_movies_by_spielberg(movies):
    no_movies_by_spielberg = 0
    director = "Steven Spielberg"
    for movie in movies:
        if movie.director == director:
            no_movies_by_spielberg += 1
    return no_movies_by_spielberg
```

Then, instead of having this `director` variable always be `'Steven Spielberg'`, we could simply turn it into one of our
function arguments, to make this very specific function that can only count Spielberg movies into a more general one
that can count movies made by any director (so let's also rename it):

```python
def count_movies_by_director(movies, director):
    no_movies_by_director = 0
    for movie in movies:
        if movie.director == director:
            no_movies_by_director += 1
    return no_movies_by_director
```
Now we can count both movies made by Spielberg as well as movies made by any other director by calling this function:
```python
no_movies_by_spielberg = count_movies_by_director(movies, 'Steven Spielberg')
no_movies_by_coen_brothers = count_movies_by_director(movies, 'Coen Brothers')
```
Much better.

## Generalizing
What we just did is called 'generalizing' our function. By replacing a hard-coded value with a function argument, this
function is now usable more flexibly in many different situations.
