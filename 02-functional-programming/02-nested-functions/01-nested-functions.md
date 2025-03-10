# Nested Functions

Previously, we saw how we generalized the specific function `count_movies_by_spielberg()` into the more general function
`count_movie_by_director(director)`.

```python
def count_movies_by_director(movies, director):
    no_movies_by_director = 0
    for movie in movies:
        if movie.director == director:
            no_movies_by_director += 1
    return no_movies_by_director
```
However, a little later we created an even more general `count` function that could count elements in any collection
based on a `condition`-function, which we could for example use together with the helper-function `is_even` to count
the even numbers in a list:
```python
def count(collection, condition):
    count = 0
    for element in collection:
        if condition(element):
            count += 1
    return count

def is_even(number):
    return number % 2 == 0

>>> count([1, 2, 3, 4], is_even)
2
```
Can we make our function `count_movies_by_director` even more simple by using `count` in its implementation? Let's give
it a try.

The first step is to turn the `if`-condition `movie.director == director` into a `condition`-function that we can
then pass to `count`. This function needs to be such that we can use `count` as follows:
```python
count(movies, is_by_director)
```
Inside the body of the `count` function, we see that this function will be used like this:
```python
def count(collection, condition): # collection = movies, condition = is_by_director
    # rest of code
    for element in collection: # for movie in movies
        if condition(element): # if is_by_director(movie)
    # more code
```
As `collection` will be the list of movies we pass to count, we see that our `condition`-function `is_by_director` will
take a single argument, namely a movie from our list of movies.

So `is_by_director` would need to look something like this:
```python
def is_by_director(movie):
    return movie.director == director
```
However, this will clearly not work, as the `director` variable is not defined in the scope of this function. However,
`director` **is** defined in the scope of our original `count_movies_by_director` function, so if we could define
`is_by_director` within that scope, it would have access to `director` and therefore this would make it all work.
And we can do exactly that:

```python
def count_movies_by_director(movies, director):
    def is_by_director(movie):
        return movie.director == director
    return count(movies, is_by_director)
```
A function like `is_by_director`, that is defined within the scope of another function, is called a **nested function**.

Defining the function within the scope of another function like this, effectively means `is_by_director` is redefined
with a different director every time `count_movies_by_director` is called.

## When to use nested functions?

Take a look at the two fucnction definitions of `count_movies_by_director` and `count_even_numbers`:
```python
def count_movies_by_director(movies, director):
    def is_by_director(movie):
        return movie.director == director
    return count(movies, is_by_director)
```
```python
def is_even(number):
    return number % 2

def count_even_numbers(numbers):
    return count(numbers, is_even)
```
Apart from the helper-function `is_even` being defined outside of `count_even_numbers`, what is the difference between
these two functions? What made it necessary to turn `is_by_director` into a nested function, while we did not need to do
this for `is_even`?

The answer is that aside from the collections they are counting the elements of (`movies` and `numbers` respectively),
`count_movies_by_director` takes an additional parameter `director`, that defines what the condition is.

And because `count` only accepts condition-functions that have a single argument (the object we are either counting), we
__need a way to pass this argument `director` into the body of our helper-function, without adding it to its argument list__.
We can only do this by defining the helper-function in the scope in which this argument is defined, in other words, by
defining it as a **nested function**.
