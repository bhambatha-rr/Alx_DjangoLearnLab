from django.urls import path
from .views import (
    list_books,
    add_book,
    edit_book,
    delete_book,
    register,
    admin_view,
    librarian_view,
    member_view,
    CustomLoginView,
    CustomLogoutView
)

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('books/add/', add_book, name='add_book'),
    path('books/<int:pk>/edit/', edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', delete_book, name='delete_book'),
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
]
