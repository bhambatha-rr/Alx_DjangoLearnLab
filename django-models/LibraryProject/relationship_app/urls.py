from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'relationship_app'

urlpatterns = [
    # Main Views
    path('books/', views.list_books, name='list_books'),

    # Authentication
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Role-Based Views
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),

    # Permission-Based CRUD
    path('book/add/', views.book_add, name='book_add'),
    path('book/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('book/<int:pk>/delete/', views.book_delete, name='book_delete'),
]
