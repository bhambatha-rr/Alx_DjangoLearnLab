from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book, Author
from .serializers import BookSerializer

# This single view handles both GET (list) and POST (create) requests.
class BookListCreateAPIView(generics.ListCreateAPIView):
    """
    A generic view for listing and creating books.
    - GET: Returns a list of all books.
    - POST: Creates a new book.

    Permissions:
    - Read (GET) access is allowed for any user (authenticated or not).
    - Write (POST) access is restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # This is the key permission setting

# This single view handles GET (retrieve), PUT/PATCH (update), and DELETE (destroy).
class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    A generic view for retrieving, updating, and deleting a single book instance.
    - GET: Returns a single book by its ID.
    - PUT/PATCH: Updates a book.
    - DELETE: Deletes a book.

    Permissions:
    - Read (GET) access is allowed for any user.
    - Write (PUT, PATCH, DELETE) access is restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
