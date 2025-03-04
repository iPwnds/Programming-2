# Functions as variables
Just like we can assign numbers, strings and objects to variables, we can assign functions to variables. For example we
can do the following:
```python
def greet_casually(name):
    print(f"Hi {name}!")

>>> greet_function = greet_casually
>>> greet_function("Mary")
Hi Mary!
```
Of course this wasn't very useful. Let's see when and why this could actually be used in useful way.

## Example: testing performance
Let's say we just implemented a simple sorting algorithm. The algorithm in question is
[Bubblesort](https://simple.wikipedia.org/wiki/Bubble_sort). (this was an exercise in Programming 1) It's not important
to know how this algorithm works, the most important thing to know is that it can be used as follows:
```
>>> some_unsorted_list = [1, 4, 2, 6, 4, 67, 1, 2]
>>> bubble_sort(some_unsorted_list)
[1, 1, 2, 2, 4, 4, 6, 67]
```

For reference (it's not relevant to the rest of this explanation), the implementation could look like this:
(this code can also be found in [timing.py](timing.py))
```python
def bubble_sort(unsorted_list):
    """Sorts a list using the bubble sort algorithm."""
    # Create a copy of the argument list
    result_list = list(unsorted_list)
    swapped = True
    while(swapped):
        swapped = False
        for index in range(len(result_list) - 1):
            if result_list[index] > result_list[index + 1]:
                result_list[index], result_list[index + 1] = result_list[index + 1], result_list[index]
                swapped = True
    return result_list
```

To see if this implementation is performant, we wrote a function that tests the performance of our `bubble_sort` code:
```python
import time
import random

def test_bubble_sort():
    for size in [1000, 10000]:
        random_list = random.choices(range(0, 1000), k=size)

        print(f"Testing performance for list size: {size}")
        start_time = time.time()
        bubble_sort(random_list)
        end_time = time.time()
        print(f"Sorting completed in {end_time - start_time} seconds.")
        print()
```
For the rest of our explanation you also don't really need to know what all this code is doing, but we'll explain it
really quickly:
- Firstly, we want to test how fast our sorting algorithm can sort lists of various sizes. So as a first step our
function loops over all the list sizes we want to test. For now we're interested in the performance for lists with
1000 and 10 000 elements
- For each of these list sizes:
    - We first create a list of that size, filled with random numbers between 0 and 999
    - We log a statement stating which list size we're going to test
    - We record the current time using the [time.time()](https://www.geeksforgeeks.org/python-time-time-method/) method.
      This method returns the current timestamp in seconds. The current timestamp is how many seconds have passed since
      a fixed initial date (in this case jan 1st 1970) Why that is useful will become clear later.
    - Then we sort the generated random list with our `bubble_sort` function
    - Finally we record the timestamp again. By subtracting the start timestamp from the end timestamp, we know exactly
      how many seconds have passed while sorting our list. This is what we print out as well

If you didn't completely get all of that don't worry, the most important thing to remember is that this function can
test how fast our `bubble_sort` algorithm can sort various sized lists. As output we get:
```python
>>> test_bubble_sort()
Testing performance for list size: 1000
Sorting completed in 0.06225299835205078 seconds.

Testing performance for list size: 10000
Sorting completed in 6.606142997741699 seconds.
```
(The exact timings depend on the speed of your computer)

Of course, it's hard to say whether this is an efficient implementation, since we haven't compared it to anything. Let's
say we want to compare this performance to the standard Python sort implementation. We can use that implementation by
calling the function `sorted`, like so:
```python
>>> some_list = [1, 4, 2, 6, 4, 67, 1, 2]
>>> sorted(some_list)
[1, 1, 2, 2, 4, 4, 6, 67]
```

As we want to keep our previous testing method around for testing `bubble_sort` later (since we might make changes to
optimize our code), we have to create a new method `test_python_sort`, which looks largely the same as our current
`test_bubble_sort`, except instead of calling `bubble_sort` in the middle of it, we simply call `sorted`:
```python
import time
import random

def test_python_sort():
    for size in [1000, 10000]:
        random_list = random.choices(range(0, 1000), k=size)

        print(f"Testing performance for list size: {size}")
        start_time = time.time()
        sorted(random_list)  # <---- this is the only line that is different
        end_time = time.time()
        print(f"Sorting completed in {end_time - start_time} seconds.")
        print()
```
which we can now also run:
```python
>>> test_python_sort()
Testing performance for list size: 1000
Sorting completed in 6.890296936035156e-05 seconds.

Testing performance for list size: 10000
Sorting completed in 0.0007569789886474609 seconds.
```
Oops, that's embarrassing... The built-in Python implemention is about **10 000** times faster!

However more importantly, we duplicated a lot of code again. Making any change (for example printing some extra
information) means that I now have to make that change in two different methods `test_python_sort` and `test_bubble_sort`.
And if we want to test even more sorting algorithms, we have to create even more methods, duplicating even more code!

Is there a better way? Yes, there is.

## Revisiting counting movies
Let's revisit the our `count_movies_by_spielberg` example. Remember how we generalized that method into a more general
`count_movies_by_director` function by going through the following steps:
```python
# First we hardcoded 'Steven Spielberg' into a non-general count_movies_by_spielberg(movies)
def count_movies_by_spielberg(movies):
    no_movies_by_spielberg = 0
    for movie in movies:
        if movie.director == "Steven Spielberg":
            no_movies_by_spielberg += 1
    return no_movies_by_spielberg

# Then we extracted the director name into a variable
def count_movies_by_spielberg(movies):
    no_movies_by_spielberg = 0
    director = "Steven Spielberg"
    for movie in movies:
        if movie.director == director:
            no_movies_by_spielberg += 1
    return no_movies_by_spielberg

# And turning this variable into a function argument made our function more general
def count_movies_by_director(movies, director):
    no_movies_by_director = 0
    for movie in movies:
        if movie.director == director:
            no_movies_by_director += 1
    return no_movies_by_director
```

Can we do the same for our performance testing method? Focussing on the relevant parts of our test_bubble_sort, it
currently looks like this:
```python
def test_bubble_sort():
    for size in [1000, 10000]:
        # some code
        bubble_sort(random_list)
        # some more code
```
As you can see, the sorting function we are testing is currently hardcoded into the body of the function, just like the
string `"Steven Spielberg"` was hardcoded into the body of the `count_movies_by_spielberg` function.

But as we saw at the very beginning of this section, just like we can assign `"Steven Spielberg"` to a variable, we can
assign any function (and therefore our `bubble_sort` function) to a variable as well:
```python
def test_bubble_sort():
    sorting_function = bubble_sort
    for size in [1000, 10000]:
        # some code
        sorting_function(random_list)
        # some more code
```
And if we can assign this function to a variable, we can turn it into a function argument too:
```python
def test_bubble_sort(sorting_function):
    for size in [1000, 10000]:
        # some code
        sorting_function(random_list)
        # some more code
```
And voila! Just like this we wrote a performance testing function that can test the performance of any sorting function!
This deserves a renaming! Instead of naming it `test_bubble_sort`, we'll call it `test_sort`:
```python
def test_sort(sorting_function):
    for size in [1000, 10000]:
        # some code
        sorting_function(random_list)
        # some more code
```
and we can test any sorting function like so:
```python
>>> test_sort(bubble_sort)
Testing performance for list size: 1000
Sorting completed in 0.06225299835205078 seconds.

Testing performance for list size: 10000
Sorting completed in 6.606142997741699 seconds.

>>> test_sort(sorted)
Testing performance for list size: 1000
Sorting completed in 6.890296936035156e-05 seconds.

Testing performance for list size: 10000
Sorting completed in 0.0007569789886474609 seconds.
```
If we implement another function `insertion_sort` (that uses the
[insertion sort algorithm](https://en.wikipedia.org/wiki/Insertion_sort)), we could test that function, without writing
any extra code, just like this:
```python
>>> test_sort(insertion_sort)
# its output
```

## Conclusion: higher order functions
This example showed the usefulness of being able to pass functions to other functions as arguments. Functions like
`test_sort`, that take other functions as arguments, are called **higher order functions**

