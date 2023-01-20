from django.urls import re_path as url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'movies', views.movies, name='movies'),
    url(r'directors', views.directors, name='directors'),
]