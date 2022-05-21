from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Movies(models.Model):
    movie_id = models.CharField(max_length=100, primary_key=True)
    movie_title = models.CharField(max_length=100, null=True)
    movie_img = models.ImageField(upload_to='static/img', null=True)
    movie_desc = models.CharField(max_length=25000, null=True)
    movie_genres = models.JSONField()
    movie_rating_count = models.IntegerField(default=0)
    movie_rating_sum = models.IntegerField(default=0)
    def __str__(self):
        return self.movie_title

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_ratings = models.JSONField()

    def __str__(self):
        return self.user.username