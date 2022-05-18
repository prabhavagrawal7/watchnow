from django.shortcuts import render
from joblib import load
import numpy as np
import pandas as pd
from interface.models import Movies
import requests

# Create your views here.
"""
Saving features using joblib
1. model
5. transformed_data
6. movie_index
"""
model, transformed_data, movie_indexes = load(
    './dataapi/data/required_contents.joblib')
links = pd.read_csv('./dataapi/data/links.csv', index_col=['movieId'])
movie_genres = pd.read_csv('./dataapi/data/movies.csv', index_col=['movieId'])
hash_loc = None
API_KEY = "62c56bbac67642762ecb788540b5888e"
"""
    movie_id = models.CharField(max_length=100, primary_key=True)
    movie_title = models.CharField(max_length=100, null=True)
    movie_img = models.ImageField(upload_to='static/img', null=True)
    movie_desc = models.CharField(max_length=25000, null=True)
    movie_genres = models.JSONField()
    def __name__(self):
        return self.movie_title
"""
popular_movie_list = load('./dataapi/data/popular_movies.joblib')
all_genres = pd.read_csv('./dataapi/data/all_genres.csv')['genres']
genres_dict = load('./dataapi/data/genres_dict.joblib')


def createHash():
    global hash_loc
    hash_loc = dict()
    for i, movie_index in enumerate(movie_indexes):
        hash_loc[movie_index] = i


def fetch_images(r):
    try:
        movie_img = r['backdrop_path']
        if movie_img is None:
            raise Exception("Movie image not found")
    except:
        try:
            movie_img = r['poster_path']
        except:
            movie_img = None
    if movie_img is None:
        movie_img = "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
    return movie_img


def fetch_genres(movie_id):
    genres_string = movie_genres.loc[movie_id]['genres']
    # return a list of genres sep. by |
    return genres_string.split('|')


def fetch_movie(movie_id):
    try:
        movie_obj = Movies.objects.get(movie_id=movie_id)
    except Movies.DoesNotExist:
        tmdb_id = links.loc[movie_id]['tmdbId']
        url = f"https://api.themoviedb.org/3/movie/{tmdb_id}?api_key={API_KEY}"
        r = requests.get(url).json()
        movie_title = r['original_title']
        movie_img = fetch_images(r)
        movie_desc = r['overview']
        movie_genres = fetch_genres(movie_id)
        # creating movie object and saving in database
        movie = Movies(
            movie_id=movie_id,
            movie_title=movie_title,
            movie_img=movie_img,
            movie_desc=movie_desc,
            movie_genres=movie_genres,
        )
        movie.save()
        movie_obj = Movies.objects.get(movie_id=movie_id)
    return movie_obj


def moviePageAPI(movie):
    if hash_loc is None:
        createHash()
    movie_index = movie.movie_index
    movie_loc = hash_loc[movie_index]
    x_test = transformed_data[movie_loc]
    neighbour_locs = model.kneighbors(x_test)[1][0]
    movie_list = []
    # Directly providing movies from vector location
    for loc in neighbour_locs:
        movie = fetch_movie(hash_loc[loc])
        movie_list.append(movie)
    return movie_list


def fetchMovieOnGenres(genres):
    # fetching by genres, sorting by popularity
    global genres_dict
    movies = []
    for movie_id in genres_dict[genres][:12]:
        movies.append(fetch_movie(movie_id))
    return movies

"""
The whole logical content of the index page or the front page. 
Structure of Index Page -> 
___________________________________________________________
Popular movie list -> extracted from popularMovies
Genres movie list -> extracted from user genres if user logged in
"""


def indexContent(Profile) -> dict():
    contents = {}
    # show popular movies
    contents['Top movies'] = popularMovies(16)
    global all_genres
    if Profile is None or Profile.user_reviews.get('genres_points') is None:

        # show genres popular movies
        for genres in sorted(all_genres)[:6]:
            contents[f"Popular {genres} movies"] = (fetchMovieOnGenres(genres))
    else:
        # genres_points will be in the dictionary format
        genre_list = list(Profile.user_reviews['genres_points'])
        genre_list = sorted(genre_list, key=lambda x: x[1], reverse=True)[:6]
        for genres, genre_liking in genre_list:
            contents[f'Popular {genres} movies'] = fetchMovieOnGenres(genres)
    return contents


def popularMovies(listing=100):
    movie_list = []
    for movie_id in popular_movie_list[:listing]:
        movie_list.append(fetch_movie(movie_id))
    return movie_list
