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
model, transformed_data, movie_indexes = load(
    './dataapi/movie_dataset/required_contents.joblib')
hash_loc = None
popular_movie_list = load('./dataapi/movie_dataset/popular_movies_list.joblib')
all_genres = load('./dataapi/movie_dataset/all_genres.joblib')
genres_dict = {}

def create_hash():
    """
    Creates hashing of movies with the location of indexes
    Stores the hashes in hash_loc
    """
    global hash_loc
    hash_loc = dict()
    for i, movie_index in enumerate(movie_indexes):
        hash_loc[str(movie_index)] = i


def fetch_movies(movie_id_list):
    return [Movies.objects.get(movie_id=movie_id) for movie_id in movie_id_list]


def fetch_movies_on_genre(genre) -> list:
    """
    Returns a list of movies which have same genre, 
    sorted by sum of movie ratings of users 
    """
    global genres_dict
    if genres_dict.get(genre) is not None:
        return genres_dict[genre]
    # fetching by genres, sorting by popularity
    movies = Movies.objects.filter(
        movie_genres__icontains=genre).order_by('-movie_rating_sum')
    nmovies = []
    for i in movies:
        nmovies.append(i)
    genres_dict[genre] = nmovies[:16]
    return genres_dict[genre]


def fetch_movie_on_movie(movie) -> list:
    """ 
    Returns list of movies which are similar to the (movie) variable. 
    transformed_data is list of list where data(values=ratings, index=movie_id, columns=values) is 
    reduced by StandardScalar and applied PCA on the columns to reduce variable overhead.

    Model used to find is K Nearest Neighbours
    Model = NearestNeighbors(algorithm='brute', metric='cosine', n_jobs=-1, n_neighbors=21)
    Model returns list of [neighbour distance], [movies with distances]
    """
    # getting transformed_data and using the data to extract the list of movies
    global transformed_data, hash_loc, movie_indexes
    if hash_loc is None:
        create_hash()
    trans_loc = hash_loc[movie.movie_id]
    movie_data = transformed_data[trans_loc]
    # using knn model to extract 20 movies
    movie_locs = model.kneighbors([movie_data])[1][0][1:21]
    movie_id_list = [movie_indexes[locs] for locs in movie_locs]
    return fetch_movies(movie_id_list)


def profile_movies(profile, movie_count=4) -> list:
    """
    Return a list of movies based on what movies user liked in past.
    Takes at. max past 4 best and fresh ratings and fetch movies similar to those. 
    Uses fetch_movie_on_movie function to extract the list of movies 
    """
    # returns movie_count (3) number of movie carousels
    ratings_to_movies = profile.user_ratings['ratings_to_movies']
    movie_id_list = []
    # Retrieves a rating of 5⭐️, 4⭐️, 3⭐️
    for rating in range(5, 2, -1):
        rating = str(rating)
        if len(movie_id_list) < movie_count and ratings_to_movies.get(rating) is not None:
            movie_id_list += ratings_to_movies.get(rating)[::-1]
    movie_id_list = movie_id_list[:movie_count]
    movie_list = fetch_movies(movie_id_list)
    list_from_profile = []
    for movie in movie_list:
        list_from_profile.append((movie, fetch_movie_on_movie(movie)))
    return list_from_profile


def index_content(profile=None) -> list:
    """
    The whole logical content of the index page or the front page. 
    Structure of Index Page 
    ___________________________________________________________
    Popular movie list -> extracted from popular_movies
    Profile based movie list -> extracted from user genres if user logged in
    Genres based movie list -> extracted from fetch_movies_on_genre

    Returns front page content for a given profile if user is logged in
    Otherwise returns list of default movie content.
    Returns a list of tuple(Category text, Movie list for that category)
    """

    contents = []
    # Retrieves popular movies from the function
    contents.append(('Top movies', popular_movies(16)))

    # Retrives movies based on Profile
    global all_genres
    if profile is not None:
        movies_based_on_profile = profile_movies(profile)
        for movie_lists in movies_based_on_profile:
            # movie_lists type will contain typle(movie, movie_list)
            contents.append(
                (f"Because you liked {movie_lists[0].movie_title}", movie_lists[1]))

    # Retrives movies based on Genres
    for genres in sorted(all_genres):
        contents.append((f"Popular {genres} movies",
                        fetch_movies_on_genre(genres)))
    return contents


def popular_movies(listing=100) -> list:
    """
    Returns a list of popular movies from the list of movies sorted 
    in order by sum of ratings. 
    The default list length is 100. 
    """
    movie_list = []
    for movie_id in popular_movie_list[:listing]:
        movie_list.append(movie_id)
    return fetch_movies(movie_list)
