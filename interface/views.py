# Create your views here.
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile, Movies
import dataapi.views as datafetch
import json
def index(request):
    # get the count vectorizer instance
    if request.user.is_authenticated:
        user_movies = datafetch.indexContent(Profile.objects.get(user=request.user))
    else:
        user_movies = datafetch.indexContent()
    return render(request, 'interface/index.html', {'user_movies': user_movies})
    
def userLogout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('index')

def userLogin(request): 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
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
                username = username, 
                first_name = firstname,
                last_name = lastname, 
                email = email)
            user.set_password(password1)
            user.save()
            Profile(user=user, user_reviews={})
            Profile.save()
            messages.success(request, "User is registered successfully, please login again")
        else: 
            messages.error(request, "This username is already registered")
    else:
        messages.error(request, "Some error occurred, please try again")
    return render(request, 'interface/index.html')

def moviePage(request, movie_id):
    try: 
        moviefound = True
        movie = Movies.objects.get(movie_id = movie_id)
        similar_movies = datafetch.fetchMovieOnMovie(movie)
    except Movies.DoesNotExist:
        moviefound = False
    return render(request, 'interface/moviepage.html', {'moviefound': moviefound, 'movie': movie, 'similar_movies': similar_movies})

def userrated(request): 
    if request.method == 'POST':
        print("hello")
        return HttpResponse("""{"status" : "error"}""")
    return HttpResponse("""{"status" : "error"}""")