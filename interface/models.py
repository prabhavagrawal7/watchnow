from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Movies(models.Model):
    movie_id = models.CharField(max_length=100, primary_key=True)
    movie_title = models.CharField(max_length=100, null=True)
    movie_img = models.ImageField(upload_to='static/img', null=True)
    movie_desc = models.CharField(max_length=25000, null=True)
    movie_genres = models.JSONField()
    movie_trailer_link = models.ImageField(upload_to='static/img', null=True)
    movie_rating_count = models.IntegerField(default=0)
    movie_rating_sum = models.IntegerField(default=0)
    def __str__(self):
        return self.movie_title

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_ratings = models.JSONField()

    def __str__(self):
        return self.user.username

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70)
    phone = models.CharField(max_length=70)
    desc = models.CharField(max_length=1000)

    def __str__(self):
        if len(f"{self.name[:75]}: {self.desc}") > 75:
            return f"{self.name[:75]}: {self.desc}" + '..'
        else:
            return f"{self.name[:75]}: {self.desc}"