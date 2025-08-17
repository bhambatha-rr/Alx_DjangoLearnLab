from rest_framework import generics
from rest_framework import permissions
from .models import Book
from .serializers import BookSerializer

# 1. A view for listing all books (GET)
class BookListView(generics.ListAPIView):
    """
    Provides a read-only list of all books.
    Permissions: Allows any user (authenticated or not) to view the list.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# 2. A view for retrieving a single book (GET)
class BookDetailView(generics.RetrieveAPIView):
    """
    Provides a read-only view of a single book by its ID.
    Permissions: Allows any user to view details.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# 3. A view for creating a new book (POST)
class BookCreateView(generics.CreateAPIView):
    """
    Provides an endpoint to create a new book.
    Permissions: Restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# 4. A view for updating an existing book (PUT/PATCH)
class BookUpdateView(generics.UpdateAPIView):
    """
    Provides an endpoint to update an existing book.
    Permissions: Restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# 5. A view for deleting an existing book (DELETE)
class BookDeleteView(generics.DestroyAPIView):
    """
    Provides an endpoint to delete an existing book.
    Permissions: Restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
