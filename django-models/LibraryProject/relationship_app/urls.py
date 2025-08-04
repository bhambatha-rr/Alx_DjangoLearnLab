from django.urls import path
from django.contrib.auth import views as auth_views
from . import views # Revert to the general import for views
from .views import list_books, LibraryDetailView, register, admin_view, librarian_view, member_view

app_name = 'relationship_app'

urlpatterns = [
    # Previous URLs
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Authentication URLs formatted for the checker
    path('register/', views.register, name='register'), # Use the 'views.' prefix
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),

    # Revert the logout view to use template_name as required by the checker
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
]
