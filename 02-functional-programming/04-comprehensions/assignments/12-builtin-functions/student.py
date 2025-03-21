import re

def movie_count(movies, director):
    # returns the number of movies made by director.
    return sum(1 for movie in movies if movie.director == director)

def longest_movie_runtime_with_actor(movies, actor):
    # returns the runtime duration of the longest movie in which actor appears.
    longest_runtime = 0

    for movie in movies:
        if actor in movie.actors:
            longest_runtime = max(longest_runtime, movie.runtime)

    return longest_runtime

def has_director_made_genre(movies, director, genre):
    # returns True is director made a movie of the given genre.
    return any(genre in movie.genres and movie.director == director for movie in movies)

def is_prime(n):
    # checks whether n is a prime number, i.e., that it is only divisible by 1 and itself.
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

def is_increasing(ns):
    # checks whether the values in ns appear in nondecreasing order. For example, is_increasing([1, 1, 2, 3, 4, 6]) should return True, whereas is_increasing([3, 2, 1]) should yield False.
    return all(x <= y for x, y in zip(ns, ns[1:]))

def count_matching(xs, ys):
    # counts how many of the corresponding elements are equal. For example, count_matching([1, 2, 3], [3, 2, 1]) should return 1, because only equal values on equal positions are counted.
    return sum(1 for x, y in zip(xs, ys) if x == y)

def weighted_sum(ns, weights):
    # should multiply each value in ns with its corresponding weight in weights and return the sum of these products. For example, weighted_sum([a, b, c], [x, y, z]) should return a * x + b * y + c * z.
    return sum(n * w for n, w in zip(ns, weights))

def alternating_caps(string):
    # should change the case of each character such that they alternate between upper and lower case. For example, alternating_caps("abcdef") should return AbCdEf.
    return ''.join(
        char.upper() if i % 2 == 0 else char.lower()
        for i, char in enumerate(string)
    )

def find_repeated_words(sentence):
    # first collects all words in the given string sentence. A word is defined as a series of letters (can be both upper and lowercase). Next, the function has to look for repeated consecutive words and collect them in a set. The case of letters should be ignored: "dog" and "Dog" are to be considered the same word. For example, find_repeated_words("This sentence has has repeated words. Words.") should return the set {'has', 'words'}. The returned set should contain all of its words in lower case. Note also that interpunction, spaces, etc. should also have no impact on deciding whether a word is repeated or not.
    words = re.findall(r'[a-zA-Z]+', sentence.lower())

    return {word1 for word1, word2 in zip(words, words[1:]) if word1 == word2}