def titles(movies):
    # returns the movie titles.
    list = []
    for movie in movies:
        list.append(movie.title)
    return list

def titles_and_years(movies):
    # returns the movie titles and their year, grouped in pairs: [(title1, year1), (title2, year2), ...].
    list = []
    for movie in movies:
        list.append((movie.title, movie.year))
    return list

def titles_and_actor_counts(movies):
    # returns the movie titles paired up with the number of actors.
    list = []
    for movie in movies:
        list.append((movie.title, len(movie.actors)))
    return list

def reverse_words(sentence):
    # must reverse each word in the given string sentence. Words are separated by one space.
    return ' '.join(word[::-1] for word in sentence.split())