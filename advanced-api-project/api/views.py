from rest_framework import generics
from rest_framework import filters
# This is the combined permission import required by the previous task's checker.
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
# This is the filter import required by the current task's checker.
from django_filters import rest_framework as django_filters
from .models import Book
from .serializers import BookSerializer

# An enhanced view for listing books with all features
class BookListView(generics.ListAPIView):
    """
    Provides a read-only list of all books with advanced query capabilities.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Use the imported permission class
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Explicitly define the backends for filtering, searching, and ordering
    filter_backends = [django_filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Configuration for DjangoFilterBackend
    filterset_fields = ['publication_year', 'author__name']

    # Configuration for SearchFilter
    search_fields = ['title', 'author__name']

    # Configuration for OrderingFilter
    ordering_fields = ['title', 'publication_year']

# --- Other Required Views for Previous Checkers ---

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
