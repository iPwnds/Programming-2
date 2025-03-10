# Indices Of
Consider the following function `get_palindrome_indices(strings)`
which return the indices of the strings in the last that are palindromes (words that are the same backwards)
```python
def get_palindrome_indices(strings):
    indices = []
    for index, string in enumerate(strings):
        if string == string[::-1]:
            indices.append(index)
    return indices

>>> get_palindrome_indices(["kayak", "never", "rotator", "palindrome"])
[0, 2]
```

Generalize this function into `indices_of(xs, condition)` that returns the indices of all the elements in any kind of
list for which `condition` returns a truthy value. You'll also need to define a function `is_palindrom` that determines
whether a given string is a palindrome

```python
>>> indices_of(["kayak", "never", "rotator", "palindrome"], is_palindrome)
[0, 2]
```
