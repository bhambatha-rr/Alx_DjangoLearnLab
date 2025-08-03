from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# 1. Implement Function-based View
def list_books(request):
    """
    A function-based view that retrieves all books from the database
    and renders them using a template.
    """
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'relationship_app/list_books.html', context)


# 2. Implement Class-based View
class LibraryDetailView(DetailView):
    """
    A class-based view that displays details for a specific library.
    Django's DetailView automatically handles fetching the object
    based on the primary key (pk) from the URL.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library' # Use 'library' in the template instead of the default 'object'
