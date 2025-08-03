from django.urls import path
# Import each view explicitly as required by the checker
from .views import list_books
from .views import LibraryDetailView

app_name = 'relationship_app'

urlpatterns = [
    # URL for the function-based view to list all books
    path('books/', list_books, name='list_books'),

    # URL for the class-based view to show a specific library's details
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
