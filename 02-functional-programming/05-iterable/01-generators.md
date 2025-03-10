# Generator functions
Generator functions are functions that behave like iterables. For example, we could iterate over the following list and
print its results
```python
languages = ["Python", "Java", "Haskell"]
for language in languages:
    print(language)

Python
Java
Haskell
```
A generator function is a function that generates values which that can also be iterated over. For example, the previous
list can be written as the generator function:
```python
def languages():
    yield "Python"
    yield "Java"
    yield "Haskell"

for language in languages():
    print(language)

Python
Java
Haskell
```

What is going on here? Well the keyword `yield` behaves a little like `return`. Like return, yield returns the value
from the function to the code that called it. However unlike return, the function resumes when the next value is needed
until it encounters the next yield-statement, at which point it returns the value and pauses again.

You can think of it as if the above `languages()` function actually returns a collection with all of the values it
'yields', so they can be iterated over. However - and this is an important distinction - it doesn't actually return all
of these values in a collection at once. Instead, the generator function only resumes execution when the next value is
needed.

We can demonstrate this by adding print statements to our generator function:
```python
def languages():
    print("Yielding Python")
    yield "Python"
    print("Yielding Java")
    yield "Java"
    print("Yielding Haskell")
    yield "Haskell"
```
If we execute this function as before, we get what we expect:
```python
for language in languages():
    print(language)

Yielding Python
Python
Yielding Java
Java
Yielding Haskell
Haskell
```
However, if we would break this loop early, we see that the `languages` function didn't actually fully execute at once
and collected its 'yield' values into some collection which it then returned (in which case we would expect all the
print statement to have executed):
```python
for language in languages():
    print(language)
    if language == "Python":
        break

Yielding Python
Python
```
Instead, because the iteration was broken off after the value `"Python"` was yielded, the function never resumed, and
therefore never printed out any of the other log-statements ("Yielding Java" and "Yielding Haskell").

Finally, what do you think would happen if we simply called our generator function without looping over its result, like
so:
```python
languages()
# No output
```
Nothing is printed! The function only starts its execution when we ask for the first value by looping over it.

## Another example
The above example simply served to introduce the generator function syntax and how these functions can be used as
iterables. Let's look at another example of a generator function that is a bit more useful:
```python
def integers(n):
    current = 0
    while current < n:
        yield current
        current += 1

for i in integers(5):
    print(i)
0
1
2
3
4
```
This generator function generates all integers starting at 0 up until (but not including `n`). This function might seem
familiar to you, as it basically does what the built-in `range` does. (Though the behaviour is largely the same, `range`
is actually not a generator function, but we'll see why that is later).

## The purpose of generator functions
The advantage of generator functions is that you can iterate over a large set of values, without having to store all of
them in some datastructure, which saves time and is more memory efficient. For example if we look at how much memory a
list of 10 000 integers takes in Python:
```
>>> sys.getsizeof(list(range(10000)))
80056
```
we see that takes up roughly 80KB, while if we would generate those same numbers with our generator function defined
above
```
>>> sys.getsizeof(integers(10000))
112
```
we see it only takes 112 bytes. This makes sense, because we're not actually storing any of these values, we are simply
computing them on the fly.

Also because we don't first have to create this entire datastructure that stores all of these values, we save a lot
of time. (You can try to test how long it takes to create a list of let's say 100 thousand integers vs how long it takes
to initialize this generator function)

## the `next` function
Apart from iterating over all the values of a generator function in a for-loop, you can also get its values one by one,
by using the built-in `next` function:
```python
ints = integers(5)
>>> next(ints)
0
>>> next(ints)
1
...
```

## Infinite generators
Another application of generator functions is you can define them to go on for ever. For example, the function
```python
def integers():
    current = 0
    while True:
        yield current
        current += 1
```
will generate integers indefinitely. This is something you could have not achieved with any datastructure. Of course
beware that iterating over such a generator function will create an infinite loop, but there are cases where this is
exactly what you want. And of course you can simply use the `next`-function to simply get the values one at a time:
```python
ints = integers()
>>> next(ints)
0
>>> next(ints)
1
...
```

## Generators vs iterables
At this point you might think that generators are a type of iterable, but there is actually one subtle difference:
when you call a generator function, you can only iterate over it once, while you can iterate over iterables many times.
If you want to iterate over the generator function more than once, you have to call it again. Let's illustrate with an
example:
```python
l = [1, 2, 3]
for el in l:
    print(el)
1
2
3

for el in l:
    print(el)
1
2
3
```
As you can see, we were able to iterate of the specific list `l` twice, and printed out all of its values correctly both
times. You could do the same with `range`:
```python
r = range(3)
for el in r:
    print(el)
0
1
2

for el in r:
    print(el)
0
1
2
```
However, if you would try this for our generator function `integers(n)`, you would actually get:
```python
g = integers(3)
for el in g:
    print(el)
0
1
2

for el in g:
    print(el)
# Nothing is printed,
# the generator
# is already 'spent'
```
Of course you could easily fix this by simply calling the generator function multiple times like so:
```python
for el in integers(3):
    print(el)
0
1
2

for el in integers(3):
    print(el)
0
1
2
```

## What is `range`?
At this point you might be wondering what `range` is, if it's not a generator function. Range is actually a class that
implements the `iterable` protocol (as List and other collections do). If you're interested in how to turn classes into
iterables, we definitely encourage you to look that up. It's not especially complicated, but we're not going to cover
that in this class.

## Conclusions
- Generator functions can be used when we can define the values we want to iterate over programmatically.
- They are more space and time efficient than to first trying to allocate a datastructure to contain all of these values.
- The only difference between generator and regular functions syntax-wise is that generator functions use `yield` instead
  of `return`
