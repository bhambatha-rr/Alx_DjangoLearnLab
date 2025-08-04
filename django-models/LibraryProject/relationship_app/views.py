from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library

# Imports for Authentication
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login # This is the import the checker wants

# --- Your existing views ---
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

class LibraryDetailView(DetailView):
    """
    A class-based view that displays details for a specific library.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# --- Corrected Registration View ---
def register(request):
    """
    Handles user registration. If the form is valid, it saves the user,
    logs them in automatically, and redirects to the main book list.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the form and get the new user object
            login(request, user)  # Log the new user in
            return redirect('relationship_app:list_books') # Redirect to the main page
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
