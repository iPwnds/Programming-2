# Iterable

So far you've encountered multiple collections:

* Lists
* Tuples
* Strings
* Sets
* Dictionaries

While all of these collections are different in several ways, for example
- lists allow indexed access (`l[i]`) while sets do not
- tuples are immutable, while most other collections can be modified
- dictionaries are key-value pairs, while the other collections simply contain single values
- etc
there is one property they all share: they can all be iterated on. For example in the following code it doesn't matter
whether `coll` is defined a list/tuple/dict/etc, the for-loop will always work:

```python
coll = [1, 2, 3, 4]
# or
coll = {
    'key_1': 1,
    'key_2': 2,
}
# or
coll = "A string is also a collection (of characters)"
# or
coll = (1, 2, ,3)

# The for-loop will work with all of these:
for element in coll:
    print(element)
```

When objects can be iterated on like this, we call them **iterables**.

There are several functions that take iterables as arguments. These functions don't care which collection it is exactly
that they are receiving as arguments. They only care that the argument is iterable.

```python
min(collection)

max(collection)

sum(collection)

all(collection)

any(collection)

[expr for x in collection]

" ".join(collection)
```
