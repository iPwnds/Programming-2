def movies_from_year(movies, year):
    # returns the titles of movies from the given year.
    list = []
    for movie in movies:
        if movie.year == year:
            list.append(movie.title)

    return list


def movies_with_actor(movies, actor):
    # returns the titles of movies that have actor in it.
    list = []
    for movie in movies:
        if actor in movie.actors:
            list.append(movie.title)

    return list

def divisors(n):
    # returns the divisors of n in increasing order. For example, divisors(12) should return [1, 2, 3, 4, 6, 12].
    return [i for i in range(1, n + 1) if n % i == 0]