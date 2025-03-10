# Itertools

The [`itertools`](https://docs.python.org/3/library/itertools.html) module contains many iterator-centric functionality.
One of the functions in this module is [`pairwise`](https://docs.python.org/3/library/itertools.html#itertools.pairwise).

```python
>>> from itertools import pairwise
>>> list(pairwise(range(5)))
[(0, 1), (1, 2), (2, 3), (3, 4)]
```
Rely on it to solve the first assignment. For all other assignments, try to find the relevant functions in the
`itertools` module.
