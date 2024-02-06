def movie_organizer(*args):
    dictionary_of_movies = {}
    result = ''
    for arg in args:
        movie,genre = arg
        if genre not in dictionary_of_movies:
            dictionary_of_movies[genre] = [movie]
        else:
            dictionary_of_movies[genre].append(movie)

    sorted_movies = sorted(
        dictionary_of_movies.items(),
        key = lambda kvp: (-len(kvp[1]),kvp[0])
    )

    for genre,movie_names in sorted_movies:
        result += genre + f" - {len(movie_names)}" '\n'
        for movie in sorted(movie_names):
            result += f'* {movie}\n'
    return result

print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("21 Jump Street", "Comedy")))

