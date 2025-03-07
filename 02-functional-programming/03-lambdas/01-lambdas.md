# Lambdas

In the section on higher order functions, we saw that we could create simple but very generally applicable functions
such as `count`, by giving them a function as an argument. For example we created the function `count` like this:
```python
def count(collection, condition):
    count = 0
    for element in collection:
        if condition(element):
            count += 1
    return count
```
which could then be used together with a helper function such as `is_even`
```python
def is_even(number):
    return number % 2 == 0

>>> no_even_numbers = count([1, 2, 3, 4], is_even)
2
```
or a nested function such as for `count_movies_by_director`:
```python
def count_movies_by_director(movies, director):
    def is_by_director(movie):
        return movie.director == director
    return count(movies, is_by_director)
```

Having to define helper functions like this every time you want to use the count function for something can get a little
bit cumbersome.

Luckily there is a shorter syntax. First let's introduce this syntax. Instead of defining the function:
```python
def is_even(number):
    return number % 2 == 0

no_even_numbers = count([1, 2, 3, 4], is_even)
```

You can write
```python
is_even = lambda number: number % 2 == 0
no_even_numbers = count([1, 2, 3, 4], is_even)
```

## The lambda syntax
Let's dissect this weird new thing.

The name `lambda` comes from [the lambda calculus](https://en.wikipedia.org/wiki/Lambda_calculus), which is a tiny
programming language developed around a century ago. You can simply pretend lambda means "function".

The general syntax of a lambda function is
```python
lambda arguments: expression
```
* `arguments` represents the argument list of this function (which can be empty), just like you can have arguments in a
regular function. **NOTE**: In a lambda function we **don't write parentheses**.
* The `:` separates the arguments from the body of the function. This body is always just a single expression that is
  returned
* Because the expression of the body is always returned, no `return`-statement is necessary, it happens implicitly.
* This means a lambda-function is always a **one-line** function

Let's see some more examples. We'll show the lambda function together with it's equivalent classic function definition:

A function that always just returns the value 5, is written as:
```python
# The lambda syntax
return_5 = lambda: 5

# The regular function definition
def return_5():
    return 5

>>> return_5()
5
```
The lambda function that adds two numbers together can be written as:
```python
# The lambda syntax
add = lambda value_1, value_2: value_1 + value_2

# The regular function definition
def add(value_1, value_2):
    return value_1 + value_2

>>> add(4, 6)
10
```

## Intermezzo: expressions vs statements
You've probably heard the term 'expression' being used before when talking about code. But what is an expression exactly?

An expression is piece of code that evaluates to a value. Examples of this are
- constants: eg `"hello"`, `5`, `True`, ...
- variables: `counter`, `name`, ...
- results of operations: `"hello" + "world"`, `3 * 2`, ...
- function calls: `max(1, 2, 3)`, `"hello".upper()`, ...
- ...

As a general rule, if you can put it as the argument of a `print()`-statement or you can assign it to variable without
it raising any errors, it's an expression.
```python
print("Hello")
print(counter)
print(max(1, 2, 3))
...
```

Then what is not an expression?
- if-statements:
```python
if True:
    print("Hello")
```
- function definitions;
```python
def function():
    print("Hello")
```
- ...
You can verify this by trying to put a function definition or an if-statement in a `print`-call:
```python
 # This will raise an error
print(def function(): print("Hello"))
```
Likewise, for-loops, class definitions etc are also not expressions. Instead we call these things **statements**. (Note
that every expression is also a statement, but not every statement is an expression)

So why this big explanation about expressions?

## Lambdas as expressions
Because lambda functions (as opposed to regular function definitions) **are** expressions.

That means that instead of assigning them to a variable when creating them, like we did before:
```python
is_even = lambda number: number % 2 == 0
no_even_numbers = count([1, 2, 3, 4], is_even)
```

We can simply immediately pass it to the function:
```python
no_even_numbers = count([1, 2, 3, 4], lambda number: number % 2 == 0)
```

When we do this, we don't even have to name the function anymore.

> HINT: if initially, you find it confusing to see lambda functions as part of a function call like this, simply start
by defining it as a regular function, then convert it to the lambda syntax and assign it to variable. After you've done
that (like we did above) you can past the lambda function to where the variable is used.

## Lambda conclusions
A _lambda_ is nothing more than an anonymous, one-line function.
It is used in cases where we need to define a function that we're only going to use this one time.
In essence, it's a throw-away function.
We don't even bother naming it.

Note that lambdas can only be used for very simple functions: the lambda's body is limited to a single expression.
This is a Python-specific limitation: for nontrivial logic, the language wants you to define an actual named function
using `def`.
