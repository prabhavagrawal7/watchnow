# Create your views here.
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile, Movies
import dataapi.views as datafetch


def index(request):
    # get the count vectorizer instance
    if request.user.is_authenticated:
        user_movies = datafetch.index_content(
            Profile.objects.get(user=request.user))
    else:
        user_movies = datafetch.index_content()
    return render(request, 'interface/index.html', {'user_movies': user_movies})

# Under development
def search(request): 
    """
    Search for movies in the database
    If movies are not found, instead of returning empty list, redirected to the
    home page.
    """
    if request.method == 'POST':
        query = request.POST.get('query')
        if len(query) < 2: 
            messages.error(request, "Search query must be at least 2 characters")
            return redirect('index')
        query = query.strip().split()
        movies = Movies.objects.all()
        for small_query in query: 
            movies = movies.filter(movie_title__icontains=small_query)
        return render(request, 'interface/search.html', {'movies': movies})


def userLogout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logged out successfully !")
        return redirect('index')


def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, "Incorrect username or password")
        else:
            messages.success(request, "Login successful")
            login(request, user)
    else:
        messages.error(request, "Login failed")
    return redirect('index')


def userSignup(request):
    if(request.method == 'POST'):
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        if password1 != password2:
            messages.error(request, "Passwords do not match !")
        elif not User.objects.filter(username=username).exists():
            user = User.objects.create(
                username=username,
                first_name=firstname,
                last_name=lastname,
                email=email)
            user.set_password(password1)
            user.save()
            profile = Profile(
                user=user,
                user_ratings={'movies_to_ratings': {}, 'ratings_to_movies': {}})
            profile.save()
            messages.success(
                request, "User is registered successfully, please login again")
        else:
            messages.error(request, "This username is already registered")
    else:
        messages.error(request, "Some error occurred, please try again")
    return redirect('index')


def moviePage(request, movie_id):
    user_rated = None
    try:
        moviefound = True
        movie = Movies.objects.get(movie_id=movie_id)
        similar_movies = datafetch.fetch_movie_on_movie(movie)
        if request.user.is_authenticated:
            user = Profile.objects.get(user=request.user)
            user_rated = user.user_ratings['movies_to_ratings'].get(movie_id)
    except Movies.DoesNotExist:
        moviefound = False
    return render(request, 'interface/moviepage.html',
                  {
                      'moviefound': moviefound,
                      'movie': movie,
                      'similar_movies': similar_movies,
                      'user_rated': user_rated,
                      'movie_rating': round(movie.movie_rating_sum/movie.movie_rating_count, 2),
                  })

# Under development
def userRating(request, movie_id):
    if request.method == 'POST':
        movie_rating = request.POST.get('rating')
        movie = Movies.objects.get(movie_id=movie_id)
        movie.movie_rating_count += 1
        movie.movie_rating_sum += int(movie_rating)
        profile = Profile.objects.get(user=request.user)
        # some aliasings
        movie_to_ratings = profile.user_ratings['movies_to_ratings']
        ratings_to_movie = profile.user_ratings['ratings_to_movies']
        # If user is already rated before, then removing the older ratings
        if movie_to_ratings.get(movie_id) is not None:
            ratings_to_movie[movie_to_ratings[movie_id]].remove(movie_id)

        movie_to_ratings[movie_id] = movie_rating
        if ratings_to_movie.get(movie_rating) is not None:
            ratings_to_movie[movie_rating].append(movie_id)
        else:
            ratings_to_movie[movie_rating] = [movie_id]
        profile.save()
        return redirect(f'/movie/{movie_id}')

# Under development
def contact(request): 
    return render(request, 'contact.html')