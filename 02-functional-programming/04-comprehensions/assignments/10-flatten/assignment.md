

## Tasks

* Write a function `genres(movies)` that collects all movie genres in a set.
* Write a function `actors(movies)` that collects all movie actors in a set.
* Write a function `repeat_consecutive(xs, n)` that creates a new list where every element from `xs` is repeated `n` times in the following manner:
  `repeat_consecutive([1, 2, 3], 4)` should return `[1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3]`.
* Write a function `repeat_alternating(xs, n)` that creates a new list where every element from `xs` is repeated `n` times in the following manner:
  `repeat_alternating([1, 2, 3], 4)` should return `[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]`.
* Write a function `cards(values, suits)` that returns a set of all cards that can be made using `values` and `suits`.
  For example, `cards([2, 5, 10], ['hearts', 'diamonds'])` should return `{Card(2, 'hearts'), Card(5, 'hearts'), Card(10, 'hearts'), Card(2, 'diamonds'), Card(5, 'diamonds'), Card(10, 'diamonds')}`.
  You should import the `Card` class from `util`.
