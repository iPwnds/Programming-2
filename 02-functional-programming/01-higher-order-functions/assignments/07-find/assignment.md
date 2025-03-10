## Task

Consider the following fucntion `find_string_with_consecutive_characters`. It returns the first string in a given list
that contains two consecutive characters that are the same.

```python
def find_string_with_consecutive_characters(strings):
    for string in strings:
        for index in range(len(string) - 1):
            if string[index] == string[index + 1]:
                return string
    return None

>>> find_string_with_consecutive_characters(["monkey", "banana", "computer", "yellow", "oddish"])
"yellow"
```

Generalize it into a more general `find` function that takes a list of any kind of object, together with condition
function such that it returns the first object in the list that satisfies the condition. Reimplement
`find_string_with_consecutive_characters` such that it uses this new `find` function.

```python
>>> find(["monkey", "banana", "computer", "yellow", "oddish"], has_consecutive_characters)
"yellow"
```
