# Generated by Django 4.0.4 on 2022-05-17 06:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('movie_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('movie_title', models.CharField(max_length=100)),
                ('movie_tags', models.CharField(max_length=100000)),
                ('movie_img', models.ImageField(upload_to='static/img')),
                ('movie_desc', models.CharField(max_length=25000)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_tags', models.CharField(default='', max_length=1000000)),
                ('liked_movies', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='interface.movies')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
