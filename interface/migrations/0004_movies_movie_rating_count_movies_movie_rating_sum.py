# Generated by Django 4.0.4 on 2022-05-21 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0003_remove_movies_movie_tags_remove_profile_user_tags_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='movie_rating_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='movies',
            name='movie_rating_sum',
            field=models.IntegerField(default=0),
        ),
    ]