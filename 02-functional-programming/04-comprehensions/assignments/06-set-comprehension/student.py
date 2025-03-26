def directors(movies):
    # collects all directors in a set.
    list = set()
    for movie in movies:
        list.add(movie.director)
    return list

def common_elements(xs, ys):
    # should return the set of values that occur both in xs and ys.
    return set(xs) & set(ys)