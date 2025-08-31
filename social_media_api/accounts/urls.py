from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView, ProfileView
from .views import RegisterView, ProfileView, FollowToggleView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('users/<int:pk>/follow/', FollowToggleView.as_view(), name='follow-toggle'),
]
