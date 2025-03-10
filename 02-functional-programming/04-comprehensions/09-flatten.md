# Flatten

## Nested for-loops
As we saw before we can replace a single for-loop with a list comprehension, for example:
```python
first_10_numbers = []
for x in range(10):
    result_list.append(x)
```
by the list comprehension
```python
first_10_numbers = [x for x in range(10)]
```

However, sometimes you will encounter nested for-loops, for example:
```python
all_sums = []
first_list = [1, 4, 20, 30]
second_list = [2, 7, 31]
for x in first_list:
    for y in second_list:
        all_sums.append(x + y)
```
(which collects all the possible sums of the numbers in those two lists)

An expression with a nested loop like this can also be converted to a list-comprehension. The code above can be
rewritten as:
```python
first_list = [1, 4, 20, 30]
second_list = [2, 7, 31]

all_sums = [x + y for x in first_list for y in second_list]
```
which results in the list
```python
[3, 8, 32, 6, 11, 35, 22, 27, 51, 32, 37, 61]
```

Notice the difference between the above expression, and the following one:
```python
all_sums = [[x + y for x in first_list] for y in second_list]
```
The difference lies in the double brackets **[]**, which results in the following list:
```python
[[3, 6, 22, 32], [8, 11, 27, 37], [32, 35, 51, 61]]
```

See how the first list is just a list of numbers, and the second one a list of lists? Make sure you understand why
this is the case.

In general, the pattern
```python
result_list = []
for x in first_input_list:
    for y in second_input_list:
        result_list.append(function(x,y))
```
can be rewritten as:
```python
result_list = [function(x, y) for x in first_input_list for y in second_input_list]
```

## Flatten
This is often used to `flatten` a list. Flattening is the process of converting nested lists (or collections in general)
into a single list/collection.

Let's say for example that you receive the list above:
```python
[[3, 6, 22, 32], [8, 11, 27, 37], [32, 35, 51, 61]]
```
but instead of having this list of lists you want a single list containing all the numbers. You can achieve this with a
traditional for-loop:

```python
argument = [[3, 6, 22, 32], [8, 11, 27, 37], [32, 35, 51, 61]]
result = []
for lst in argument:
    for element in lst:
        result.append(element)
```
which gets you the list
```python
[3, 6, 22, 32, 8, 11, 27, 37, 32, 35, 51, 61]
```

Alternatively, you can use the two for-statements in de list comprehension, as we just saw:
```python
argument = [[3, 6, 22, 32], [8, 11, 27, 37], [32, 35, 51, 61]]
result = [element for lst in argument for element in lst]
```

## Combining map, filter and flatten
You can combine as many for- and if-statements as you like, though they may get hard to understand. When unsure, try
to convert the list comprehension to the equivalent for-loop.

```python
argument = [[1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14]]
result = [element for lst in argument if len(lst) > 3 for element in lst if element > 6 if element < 10]
>>> result
[7, 8, 9]
```
To understand this comprehension you can start by writing it on multiple lines:
```python
argument = [[1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14]]
result = [
    element
    for lst in argument if len(lst) > 3
    for element in lst if element > 6 if element < 10
]
```
But also consider the equivalent nested for loop:
```python
argument = [[1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14]]
result = []
for lst in argument:
    if len(lst) > 3:
        for element in lst:
            if element > 6:
                if element < 10:
                    result.append(result)
```

Of course this example is a little bit ridiculous, it's just to show what comprehensions can do.

