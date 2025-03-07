# Mapping

Consider the following algorithm:

```python
def squares(ns):
    result = []
    for n in ns:
        result.append(n**2)
    return result


>>> squares([0, 1, 2, 3, 4])
[0, 1, 4, 9, 16]
```

While it may not be the most useful code, it follows a certain pattern: given a list of values, it applies an operation on each of them and collects the results in a new list.
Here, the operation is squaring.

Another example could be:
```python
def calc_price(groceries):
    prices = []
    for grocery in groceries:
        prices.append(grocery[1])
    return sum(prices)

>>> calc_prices([('carrots', 4.5), ('lettuce', 2.1), ('chips', 4)])
10.6
```

This pattern occurs quite often, typically as part of a bigger whole:

* Given a list of items, get the price of each item (and take the sum to get the total cost).
* Given a list of enemies, check if any one of them touches the player (and if so, the player is dead).
* Given a list of exam questions, grade each of them (and compute the final grade).

This pattern is called _mapping_: it _maps_ each value from an input list to corresponding value which is stored in an
output list.
* In the list of items, we map each item to its price
* In the list of enemies, we map each enemy to the True/False value of whether it touches the player
* In the list of exam question, we map each question to its grade.
Python provides a special syntax for this mapping operation.

We can rewrite the `squares` function above as

```python
def squares(ns):
    return [n**2 for n in ns]
```

In general the pattern
```python
new_list = []
for element in input_list:
    new_list.append(map(element))
```
Can be written as
```python
new_list = [map(element) for element in input_list]
```

This is called a _list comprehension_ and is a more concise (and readable) way to perform mappings.
They also have performance benefits.
Running the provided script `benchmark.py` shows this:

```bash
$ py benchmark.py
squares_loop used 0.764 seconds
squares_loop2 used 0.867 seconds
squares_comprehension used 0.642 seconds
```
