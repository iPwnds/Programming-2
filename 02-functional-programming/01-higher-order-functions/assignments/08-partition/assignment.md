Consider the following function:

```python
def children_and_adults(people):
    children = []
    adults = []
    for person in people:
        if person.age < 18:
            children.append(person)
        else:
            adults.append(person)

    return (children, adults)
```

As you can see it takes a list of `Person` objects and splits it up in two lists, one of children and one of adults.

Generalize this function into a function `partition(lst, condition)` such that it can take a list of any kind of object, together with a function that for each object determines whether it should be in the first or second list.

Rewrite `children_and_adults` such that it uses this new `partition` function.
