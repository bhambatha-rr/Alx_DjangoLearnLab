from django.urls import path
from . import views

app_name = 'relationship_app' # Good practice for namespacing

urlpatterns = [
    # URL for the function-based view to list all books
    path('books/', views.list_books, name='list_books'),

    # URL for the class-based view to show a specific library's details
    # <int:pk> captures the library's ID from the URL and passes it to the view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
