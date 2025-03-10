# Filtering

Consider the following function:

```python
def select_adults(people):
    result = []
    for person in people:
        if person.age >= 18:
            result.append(person)
    return result
```

This little function selects `Person`s whose age is at least `18`.
Or, more generally, given a list `lst` of values, it returns a new list that contains all items from `lst` that satisfy a certain condition (in this case that they are over 18 years old).
This is called _filtering_.

As with mapping, Python also has a special syntax for it.
Fortunately, it fits in with the already existing syntax for list comprehensions:

```python
def select_adults(people):
    return [person for person in people if person.age >= 18]
```


In general, the pattern
```python
filtered_list = []
for item in input_list:
    if condition(item):
        input_list.append(item)
```
can be rewritten as:
```python
filtered_list = [item for item in input_list if condition(item)]
```

It is of course possible to combine mapping with filtering.
Say you want the names of all adults (in other words you want to map the person objects to their namesm in addition to filtering these person objects on their age):

```python
def select_adult_names(people):
    return [person.name for person in people if person.age >= 18]
```

For the sake of readability, you might want to spread it over multiple lines:

```python
def select_adult_names(people):
    return [
        person.name
        for person in people
        if person.age >= 18
    ]
```

The general pattern:
```python
result = []
for element in input:
    if condition(element):
        result.append(map(element))
```
can be rewritten as

```python
result = [map(element) for element in input if condition(element)]
```
