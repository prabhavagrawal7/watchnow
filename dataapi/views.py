from django.shortcuts import render
from joblib import load
import numpy as np
import pandas as pd
from interface.models import Movies
import requests
from concurrent.futures import ThreadPoolExecutor
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
hash_loc = None
popular_movie_list = load('./dataapi/data/popular_movies.joblib')
all_genres = pd.read_csv('./dataapi/data/all_genres.csv')['genres']
genres_dict = load('./dataapi/data/genres_dict.joblib')
API_KEY = "62c56bbac67642762ecb788540b5888e"


def createHash():
    global hash_loc
    hash_loc = dict()
    for i, movie_index in enumerate(movie_indexes):
        hash_loc[str(movie_index)] = i


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


def fetch_movie(movie_id):
    tmdb_id = links.loc[movie_id]['tmdbId']
    url = f"https://api.themoviedb.org/3/movie/{tmdb_id}?api_key={API_KEY}"
    r = requests.get(url).json()
    movie_title = r['original_title']
    movie_img = fetch_images(r)
    movie_desc = r['overview']
    movie_genres = [genre['name'] for genre in r['genres']]
    movie_rating_count = int(r['vote_count'])
    movie_rating_sum = (float(r['vote_average'])*movie_rating_count)
    # creating movie object and saving in database
    movie = Movies(
        movie_id=movie_id,
        movie_title=movie_title,
        movie_img=movie_img,
        movie_desc=movie_desc,
        movie_genres=movie_genres,
        movie_rating_sum=movie_rating_sum,
        movie_rating_count=movie_rating_count,
    )
    movie.save()
    movie_obj = Movies.objects.get(movie_id=movie_id)
    movie_obj.save()


def fetch_movies(movie_id_list):
    movie_id_not_found = [movie_id for movie_id in movie_id_list if not Movies.objects.filter(
        movie_id=movie_id).exists()]
    with ThreadPoolExecutor(max_workers=len(movie_id_list)+1) as executor:
        with requests.Session() as session:
            executor.map(fetch_movie, movie_id_not_found)
            executor.shutdown(wait=True)
    return [Movies.objects.get(movie_id=movie_id) for movie_id in movie_id_list]


def fetch_movies_on_genre(genre):
    # fetching by genres, sorting by popularity
    global genres_dict
    movie_id_list = genres_dict[genre][:16]
    return fetch_movies(movie_id_list)


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


def profile_movies(profile, movie_count=3):
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
