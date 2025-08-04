from django.urls import path
from . import views

app_name = 'bookshelf'

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/create/', views.book_create, name='book_create'),
    path('book/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('book/<int:pk>/delete/', views.book_delete, name='book_delete'),
]
