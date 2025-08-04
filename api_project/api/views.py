from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    """
    A view that returns a list of books in JSON format.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
