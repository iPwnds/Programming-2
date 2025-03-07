# Built-in Functions

Python comes with a number of built-in functions, most of which you probably already know.
Some of these  functions are often used in conjunction with comprehensions, so let's make a few exercises on them.

> Note that these functions are not aware how their arguments are constructed.
> You can use them on any list/set/dictionary: the only thing that matters is that it is _iterable_.

We give a short overview of these functions.
Use it as a hint to solve the exercises.

## `len`

`len` returns the number of items in the collection.

## `min` and `max`

These functions, as their names imply, look for the smallest and greatest element of a collection (a list, a set, anything iterable).
Make sure though not to pass an empty collection.

## `sum`

`sum` takes the sum of all the elements.

## `all` and `any`

`all` checks if all elements in the given collection are truthy.
If so, the function returns `True`, otherwise `False`.

`any` is easier to please: it will return `True` is at least one of the values in the given collection is truthy.

## `zip`

`zip` takes two collections and pairs up their first elements, then second elements, etc.
An example will make this clearer:

```python
>>> xs = ['a', 'b', 'c']
>>> ys = [1, 2, 3]
>>> list(zip(xs, ys))
[('a', 1), ('b', 2), ('c', 3)]
```

## `enumerate`

Enumerate pairs up elements with their index.

```python
>>> xs = ['a', 'b', 'c']
>>> list(enumerate(xs))
[(0, 'a'), (1, 'b'), (2, 'c')]
```

