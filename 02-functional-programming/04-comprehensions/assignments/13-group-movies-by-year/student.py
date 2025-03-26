def group_movies_by_year(movies):
    # that creates a dictionary whose keys are years and whose values are lists of movie titles from that year.
    movie_dict = {}

    for movie in movies:
        if movie.year not in movie_dict:
            movie_dict[movie.year] = []
        movie_dict[movie.year].append(movie.title)

    return movie_dict