# Generalizing revisited

## Example: counting some more stuff
Consider the following code:
```python
def count_children(people):
    children_count = 0
    for person in people:
        if person.age < 18:
            children_count += 1
    return children_count
```
This function counts the number of children in a list of `Person` objects, based on their age.

Now consider the following function:
```python
def count_even_numbers(numbers):
    even_number_count = 0
    for number in numbers:
        if number % 2 == 0:
            even_number_count += 1
    return even_number_count
```

You can tell these functions are very similar. They both take a collection of something as their argument, iterate over
all the elements in it, and count how many elements satisfy a specific condition. We can make this
more clear by giving all the arguments and variables more generic names for example:

```python
def count_even_numbers(collection): # collection instead of numbers
    count = 0                       # count instead of even_number_count
    for element in collection:      # element instead of number
        if element % 2 == 0:
            count += 1
    return count
```
and
```python
def count_children(collection): # collection instead of people
    count = 0                   # count instead of children_count
    for element in collection:  # element instead of person
        if element.age < 18:
            count += 1
    return count
```
Here it's clear the only difference between these two functions is the `if`-condition: `element.age < 28` vs
`element % 2 == 0` These conditions are hardcoded in the function bodies.

We don't like to duplicate code. So is there a way we can turn these two count-functions into one single function that
can be used to count both of these different things?

## Extracting any code as a function
We've seen before that we can extract hardcoded constants like strings and even functions from the code and turn them
into function arguments, which is how we turned `count_movies_by_spielberg()` into `count_movies_by_director(director)`
and how we turned `test_bubble_sort()` into `test_sort(sorting_function)`.

But in this case it's the `if`-condition that is hard-coded. We can't extract a condition into a function argument,
right?

Actually we can.

The key is to realize that any code can be turned into a function. For example the condition `number % 2 == 0` can
be written as the function:
```python
def is_even(number):
    return number % 2 == 0
    # which is the same as
    # if number % 2 == 0:
    #     return True
    # else:
    #     return False
```
Our function `count_even_numbers` can then become:
```python
def count_even_numbers(collection):
    count = 0
    for element in collection:
        if is_even(element):
            count += 1
    return count
```
Likewise, if we write the function `is_child`:
```python
def is_child(person):
    return person.age < 18
```
We can rewrite `count_children` as
```python
def count_children(collection):
    count = 0
    for element in collection:
        if is_child(element):
            count += 1
    return count
```
All of the sudden, the only thing that sets these two `count` functions apart is the function they use (`is_even` vs
`is_child`) to check the condition, and as we've seen, we can extract function into variables and function arguments.
First we put the function into a variable:
```python
def count_even_numbers(collection):
    count = 0
    condition = is_even
    for element in collection:
        if condition(element):
            count += 1
    return count
```
and then into a function argument:
```python
def count_even_numbers(collection, condition):
    count = 0
    for element in collection:
        if condition(element):
            count += 1
    return count
```
which we can then use to count even numbers like so:
```python
>>> count_even_numbers([1, 2, 3, 4], is_even)
2
```
But actually, the function `count_even_numbers` doesn't really count even numbers anymore! It only counts even numbers
if you pass it a list of numbers and the `is_even` function as the `condition` argument. So let's rename it:
```python
def count(collection, condition):
    count = 0
    for element in collection:
        if condition(element):
            count += 1
    return count
```

And if we give it a list of people and the is_child as argument, we can count children in a list of `Person`s:
```python
# people is some list of Person objects
>>> count(people, is_child)
... # however many children are in the list of people
```
And of course we can still use it to count even numbers:
```python
>>> count([1, 2, 3, 4], is_even)
2
```

## Conclusion: Generalization
Now we have a single `count` function that can count any kind of objects based on any condition.
This would not have been possible without using function arguments.

This kind of generalization is very important. When writing code, you should always watch out for arbitrary limitations
and see if introducing parameters can make your functions more generally usable.


