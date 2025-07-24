from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    list_books,
    LibraryDetailView,
    RegisterView,
    CustomLoginView
)

urlpatterns = [
    # Book-related URLs
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Authentication URLs
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),

    # Updated Logout URL
    path('logout/', LogoutView.as_view(
        template_name='relationship_app/logout.html',
        next_page='login'
    ), name='logout'),
]
