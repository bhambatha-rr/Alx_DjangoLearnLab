from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    # URL for listing all books
    path('books/', views.BookListView.as_view(), name='book-list'),

    # URL for creating a new book
    path('books/create/', views.BookCreateView.as_view(), name='book-create'),

    # URL for retrieving a single book by its primary key (pk)
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),

    # CORRECTED URL for updating a single book
    path('books/update/<int:pk>/', views.BookUpdateView.as_view(), name='book-update'),

    # CORRECTED URL for deleting a single book
    path('books/delete/<int:pk>/', views.BookDeleteView.as_view(), name='book-delete'),

    # URL for obtaining an authentication token
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
