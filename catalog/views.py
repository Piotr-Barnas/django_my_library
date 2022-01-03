from django.shortcuts import render
from .models import Author, Book, BookInstance, Genre

def index(request):
    """View function used for home page"""

    # counts of main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    num_genres = Genre.objects.all().count()
    num_the = Book.objects.filter(title__icontains='the').count()
    #num_novel = BookInstance.objects.filter(book__in=Book.objects.all().filter(genre__name='Novel')).count()
    num_novel = BookInstance.objects.filter(book__genre__name='Novel').count()
    num_novels_av = BookInstance.objects.filter(
            book__genre__name='Novel',
            status__exact='a'
            ).count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_available': num_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_the': num_the,
        'num_novel': num_novel,
        'num_novels_available': num_novels_av,
    }

    """
    The render() function accepts the following parameters:

    - the original request object, which is an HttpRequest.
    - an HTML template with placeholders for the data.
    - a context variable, which is a Python dictionary, containing the data to insert into the placeholders.
    """

    return render(request, 'index.html', context=context)