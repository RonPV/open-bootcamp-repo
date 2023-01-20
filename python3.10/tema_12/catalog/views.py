from django.shortcuts import render

from .models import Book, BookInstance, Genre, Author

# Create your views here.
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_authors = Author.objects.all().count()

    disponibles = BookInstance.objects.filter(status__exact= 'a').count()

    return render(
        request,
        'index.html',
        context={
            'num_books': num_books,
            'num_authors': num_authors,
            'disponibles': disponibles,
            'num_instances': num_instances  
        }
    )