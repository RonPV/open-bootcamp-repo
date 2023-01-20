from django.db import models
from django.urls import reverse

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=64, help_text='Nombre de la pelicula')
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=100, help_text='Pon aqui de que va el libro')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie_detail", args=[str(self.id)])
    

class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        return reverse("director_detail", args=[str(self.id)])

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
