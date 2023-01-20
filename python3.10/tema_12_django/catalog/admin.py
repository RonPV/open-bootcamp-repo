from django.contrib import admin

# Register your models here.
from .models import Movie, Director

admin.site.register(Director)
admin.site.register(Movie)