from django.urls import path
from .views import (
    list_books,
    add_book,
    edit_book,
    delete_book,
    register,
    CustomLoginView,
    CustomLogoutView,
    admin_view,
    librarian_view,
    member_view
)

urlpatterns = [
    # Book-related URLs
    path('books/', list_books, name='list_books'),
    path('books/add/', add_book, name='add_book'),          # Required path
    path('books/<int:pk>/edit/', edit_book, name='edit_book'),  # Required path
    path('books/<int:pk>/delete/', delete_book, name='delete_book'),

    # Authentication URLs
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),

    # Role-based URLs
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
]
