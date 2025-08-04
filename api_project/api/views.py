from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    """
    A view that returns a list of books in JSON format.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing, creating, updating, and deleting books.
    This single class provides the following actions:
    .list() -- GET /api/books_all/
    .create() -- POST /api/books_all/
    .retrieve() -- GET /api/books_all/<id>/
    .update() -- PUT /api/books_all/<id>/
    .partial_update() -- PATCH /api/books_all/<id>/
    .destroy() -- DELETE /api/books_all/<id>/
    """

    permission_classes = [IsAuthenticated]

    queryset = Book.objects.all()
    serializer_class = BookSerializer
