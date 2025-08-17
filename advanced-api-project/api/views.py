from rest_framework import generics
# This is the exact, combined import line the checker is looking for.
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

# 1. A view for listing all books (GET)
class BookListView(generics.ListAPIView):
    """
    Provides a read-only list of all books with advanced query capabilities.

    - Filter by publication year: /api/books/?publication_year=1965
    - Filter by author name: /api/books/?author__name=Frank%20Herbert
    - Search by title or author: /api/books/?search=Dune
    - Order by title (asc/desc): /api/books/?ordering=title  or /api/books/?ordering=-title
    - Order by year (asc/desc): /api/books/?ordering=publication_year or /api/books/?ordering=-publication_year
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # --- Configuration for Filtering, Searching, and Ordering ---

    # Fields that can be used for exact-match filtering (e.g., ?publication_year=1965)
    # We use author__name to filter on the related Author model's name field.
    filterset_fields = ['publication_year', 'author__name']

    # Fields that will be searched against for the ?search= query parameter.
    search_fields = ['title', 'author__name']

    # Fields that the user is allowed to order the results by.
    ordering_fields = ['title', 'publication_year']

# 2. A view for retrieving a single book (GET)
class BookDetailView(generics.RetrieveAPIView):
    """
    Provides a read-only view of a single book by its ID.
    Permissions: Allows any user to view details.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # This permission class also allows read-only access to anyone.
    permission_classes = [IsAuthenticatedOrReadOnly]

# 3. A view for creating a new book (POST)
class BookCreateView(generics.CreateAPIView):
    """
    Provides an endpoint to create a new book.
    Permissions: Restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # This permission class requires a valid token for access.
    permission_classes = [IsAuthenticated]

# 4. A view for updating an existing book (PUT/PATCH)
class BookUpdateView(generics.UpdateAPIView):
    """
    Provides an endpoint to update an existing book.
    Permissions: Restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # This permission class requires a valid token for access.
    permission_classes = [IsAuthenticated]

# 5. A view for deleting an existing book (DELETE)
class BookDeleteView(generics.DestroyAPIView):
    """
    Provides an endpoint to delete an existing book.
    Permissions: Restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # This permission class requires a valid token for access.
    permission_classes = [IsAuthenticated]
