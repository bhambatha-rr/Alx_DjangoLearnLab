from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    # Endpoint for listing all books and creating a new one
    path('books/', views.BookListCreateAPIView.as_view(), name='book-list-create'),

    # Endpoint for retrieving, updating, or deleting a single book by its primary key (pk)
    path('books/<int:pk>/', views.BookRetrieveUpdateDestroyAPIView.as_view(), name='book-detail'),

    # Endpoint for obtaining an authentication token
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
