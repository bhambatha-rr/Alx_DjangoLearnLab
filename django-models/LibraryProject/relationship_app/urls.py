from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from . import views  # Must use this exact import format
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    # Book-related URLs
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Authentication URLs (must match these exact patterns)
    path('register/', views.register, name='register'),  # Must use "views.register"
    path('login/', LoginView.as_view(template_name="relationship_app/login.html"), name='login'),
    path('logout/', LogoutView.as_view(template_name="relationship_app/logout.html"), name='logout'),

     # New role-based URLs
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
]
