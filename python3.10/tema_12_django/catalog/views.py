from django.shortcuts import render

from .models import Director, Movie

# Create your views here.
def index(request):
    num_movies = Movie.objects.all().count()
    num_directors = Director.objects.all().count()

    return render(
        request,
        'index.html',
        context={
            'num_movies': num_movies,
            'num_directors': num_directors
        }
    )

def movies(request):
    movies = Movie.objects.all()

    return render(
        request,
        'movies.html',
        context={
            'movies': movies
        }
    )

def directors(request):
    directors = Director.objects.all()

    return render(
        request,
        'directors.html',
        context={
            'directors': directors
        }
    )