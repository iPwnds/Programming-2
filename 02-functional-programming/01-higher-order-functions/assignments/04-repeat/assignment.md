
## Task

Let's have you write some higher order functions.
We start off simple:

```python
def say_hello():
    print("Hello!")

>>> repeat(say_hello, 5)
Hello!
Hello!
Hello!
Hello!
Hello!
```

Write a function `repeat(function, n)` that simply calls `function` `n` times.
You can assume `function` takes no arguments and returns nothing useful.
