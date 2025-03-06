## Tasks

Write the following functions and rely on comprehensions and the functions above.

* `movie_count(movies, director)` returns the number of movies made by `director`.
* `longest_movie_runtime_with_actor(movies, actor)` returns the runtime duration of the longest movie in which `actor` appears.
* `has_director_made_genre(movies, director, genre)` returns `True` is `director` made a movie of the given `genre`.
* `is_prime(n)` checks whether `n` is a prime number, i.e., that it is only divisible by 1 and itself.
* `is_increasing(ns)` checks whether the values in `ns` appear in nondecreasing order.
  For example, `is_increasing([1, 1, 2, 3, 4, 6])` should return `True`, whereas `is_increasing([3, 2, 1])` should yield `False`.
* `count_matching(xs, ys)` counts how many of the corresponding elements are equal.
  For example, `count_matching([1, 2, 3], [3, 2, 1])` should return `1`, because only equal values on equal positions are counted.
* `weighted_sum(ns, weights)` should multiply each value in `ns` with its corresponding weight in `weights` and return the sum of these products.
  For example, `weighted_sum([a, b, c], [x, y, z])` should return `a * x + b * y + c * z`.
* `alternating_caps(string)` should change the case of each character such that they alternate between upper and lower case.
  For example, `alternating_caps("abcdef")` should return `AbCdEf`.
* `find_repeated_words(sentence)` first collects all words in the given string `sentence`.
  A word is defined as a series of letters (can be both upper and lowercase).
  Next, the function has to look for repeated consecutive words and collect them in a set.
  The case of letters should be ignored: `"dog"` and `"Dog"` are to be considered the same word.
  For example, `find_repeated_words("This sentence has has repeated words.   Words.")` should return the set `{'has', 'words'}`.
  The returned set should contain all of its words in lower case.
  Note also that interpunction, spaces, etc. should also have no impact on deciding whether a word is repeated or not.
