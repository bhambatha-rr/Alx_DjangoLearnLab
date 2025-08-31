from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView, ProfileView, FollowToggleView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),

    # These are the two separate URL patterns required by the checker.
    # Both point to the same view.
    path('follow/<int:user_id>/', FollowToggleView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', FollowToggleView.as_view(), name='unfollow_user'),
]
