# Min and Max

We can find the maximum of a series of numbers:

```python
max(numbers)
```

But what if we want to get the `Person` the highest age in a list of `Person` objects (people)? We can't just do

```python
max(people)
```
because Python doesn't know that we consider the 'max' `Person` to be the one with the highest age.

`max`, like `sort`, relies on `__lt__`.
This means we could have `Person`'s `__lt__` method compare ages, but that would be very limiting: In this context we
want the 'max'-person to be the oldest, but what if at some other point we want the tallest person, or the person with
the longest name etc.?

Fortunately, there is a way to tell `max` what we want to maximize.
Like `sort`, it takes a (keyword) parameter `key`.
This should be a function that, given an element of the list, returns the value that should be used for comparisons.

```python
oldest_person = max(people, key=lambda person: person.age)
tallest_person = max(people, key=lambda person: person.height)
person_with_longest_name = max(people, key=lambda person: len(person.name))
```

And of course, the same is true for `min`.
