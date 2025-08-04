from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookList, BookViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    # Route for the original BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),

    # Include the router URLs for the BookViewSet (all CRUD operations)
    path('', include(router.urls)),

    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
