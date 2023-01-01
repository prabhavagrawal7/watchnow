
# Generated by Django 4.0.4 on 2022-05-23 12:52
# model dependencies
from joblib import load
import numpy as np
import pandas as pd
from django.db import migrations
popular_movie_list = load('./dataapi/movie_dataset/popular_movies_list.joblib')
links = pd.read_csv('./dataapi/movie_dataset/links.csv')
movies_info = pd.read_csv(
    './dataapi/movie_dataset/movie_info.csv', index_col='movieId')
Movies = None


def fetch_movie(movie_id):
    global Movies
    movie_info = movies_info.loc[movie_id]
    movie_title = movie_info['original_title']
    movie_img = movie_info['backdrop_path']
    movie_desc = movie_info['overview']
    movie_genres = movie_info['genres']
    movie_rating_count = int(movie_info['vote_count'])
    movie_rating_sum = round(movie_rating_count*movie_info['vote_average'])
    movie_trailer_links = [result['key'] for result in eval(movie_info['videos'])['results'] if result['type'] == 'Trailer']
    if len(movie_trailer_links) == 0:
        try: 
            movie_trailer_links.append(eval(movie_info['videos'])['results'][0]['key'])
        except: 
            movie_trailer_links = [""]
    movie_trailer_link = movie_trailer_links[0]

    # creating movie object and saving in database
    movie = Movies(
        movie_id=movie_id,
        movie_title=movie_title,
        movie_img=movie_img,
        movie_desc=movie_desc,
        movie_genres=movie_genres,
        movie_rating_sum=movie_rating_sum,
        movie_rating_count=movie_rating_count,
        movie_trailer_link=movie_trailer_link
    )
    movie.save()


def fetch_movies(movie_id_list):
    [fetch_movie(movie_id) for movie_id in movie_id_list]


def populate_database(apps, schema_editor):
    global Movies
    Movies = apps.get_model('interface', 'Movies')
    fetch_movies(links['movieId'].tolist())


def unpopulate_database(apps, schema_editor):
    global Movies
    Movies = apps.get_model('interface', 'Movies')
    Movies.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0006_movies_movie_trailer_link'),
    ]

    operations = [
        migrations.RunPython(populate_database, unpopulate_database),
    ]


if __name__ == "__main__":
    fetch_movies(popular_movie_list)
