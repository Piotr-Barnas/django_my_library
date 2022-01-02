from django.shortcuts import render
from .models import Author, Book, BookInstance, Genre

def index(request):
    """View function used for home page"""

    # counts of main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_available': num_available,
        'num_authors': num_authors,
    }

    """
    The render() function accepts the following parameters:

    - the original request object, which is an HttpRequest.
    - an HTML template with placeholders for the data.
    - a context variable, which is a Python dictionary, containing the data to insert into the placeholders.
    """

    return render(request, 'index.html', context=context)