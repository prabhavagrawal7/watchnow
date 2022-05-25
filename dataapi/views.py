# from django.shortcuts import render
from joblib import load
import numpy as np
import pandas as pd
from interface.models import Movies
# Create your views here.
"""
Saving features using joblib
1. model
5. transformed_data
6. movie_index
"""
model, transformed_data, movie_indexes = load('./dataapi/movie_dataset/required_contents.joblib')
hash_loc = None
popular_movie_list = load('./dataapi/movie_dataset/popular_movies_list.joblib')
all_genres = load('./dataapi/movie_dataset/all_genres.joblib')
# all_genres = pd.read_csv('./dataapi/movie_dataset/all_genres.csv')
genres_dict = {}

def createHash():
    global hash_loc
    hash_loc = dict()
    for i, movie_index in enumerate(movie_indexes):
        hash_loc[str(movie_index)] = i


def fetch_movies(movie_id_list):
    return [Movies.objects.get(movie_id=movie_id) for movie_id in movie_id_list]


def fetch_movies_on_genre(genre):
    global genres_dict
    if genres_dict.get(genre) is not None: 
        return genres_dict[genre]
    # fetching by genres, sorting by popularity
    movies = Movies.objects.filter(movie_genres__icontains=genre).order_by('-movie_rating_sum')
    nmovies = []
    for i in movies:
        nmovies.append(i)
    genres_dict[genre] = nmovies[:16]
    return genres_dict[genre]

"""
The whole logical content of the index page or the front page. 
Structure of Index Page -> 
___________________________________________________________
Popular movie list -> extracted from popularMovies
Genres movie list -> extracted from user genres if user logged in
"""


def fetchMovieOnMovie(movie):
    # getting transformed_data and using the data to extract the list of movies
    global transformed_data, hash_loc, movie_indexes
    if hash_loc is None:
        createHash()
    trans_loc = hash_loc[movie.movie_id]
    movie_data = transformed_data[trans_loc]
    # using knn model to extract 20 movies
    movie_locs = model.kneighbors([movie_data])[1][0][1:21]
    movie_id_list = [movie_indexes[locs] for locs in movie_locs]
    return fetch_movies(movie_id_list)


def profile_movies(profile, movie_count=4):
    # returns movie_count (3) number of movie carousels
    ratings_to_movies = profile.user_ratings['ratings_to_movies']
    movie_id_list = []
    for rating in range(5, 2, -1):
        rating = str(rating)
        if len(movie_id_list) < movie_count and ratings_to_movies.get(rating) is not None:
            movie_id_list += ratings_to_movies.get(rating)[::-1]
    movie_id_list = movie_id_list[:movie_count]
    movie_list = fetch_movies(movie_id_list)
    list_from_profile = []
    for movie in movie_list:
        list_from_profile.append((movie, fetchMovieOnMovie(movie)))
    return list_from_profile


def indexContent(profile=None) -> list():
    """
    Returns front page content for a given profile if user is logged in
    Otherwise returns list of default movie content.
    """
    contents = []
    # show popular movies

    contents.append(('Top movies', popularMovies(16)))
    global all_genres
    if profile is not None:
        movies_based_on_profile = profile_movies(profile)
        for movie_lists in movies_based_on_profile:
            # movie_lists type will contain typle(movie, [movie_list])
            contents.append(
                (f"Because you liked {movie_lists[0].movie_title}", movie_lists[1]))

    for genres in sorted(all_genres):
        contents.append((f"Popular {genres} movies",
                        fetch_movies_on_genre(genres)))
    return contents


def popularMovies(listing=100):
    movie_list = []
    for movie_id in popular_movie_list[:listing]:
        movie_list.append(movie_id)
    return fetch_movies(movie_list)
