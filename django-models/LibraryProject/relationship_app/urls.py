from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from .views import list_books, LibraryDetailView, register

app_name = 'relationship_app'

urlpatterns = [
    # Previous URLs
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Authentication URLs
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),

    # CORRECTED LOGOUT URL: Use the full namespaced name for next_page
    path('logout/', auth_views.LogoutView.as_view(next_page='relationship_app:logged_out_page'), name='logout'),

    # The page that the logout view redirects to
    path('logged-out/', TemplateView.as_view(template_name='relationship_app/logout.html'), name='logged_out_page'),
]
