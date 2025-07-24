from django.shortcuts import render
from django.views.generic.detail import DetailView  # This exact import
from .models import Library, Book

# Function-based view (for listing books)
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view (for library details)
class LibraryDetailView(DetailView):
    model = Library  # This requires the Library import
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
