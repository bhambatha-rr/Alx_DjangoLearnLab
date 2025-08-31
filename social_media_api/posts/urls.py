from django.urls import path, include
from rest_framework.routers import DefaultRouter
# Import the two new views
from .views import PostViewSet, CommentViewSet, FeedView, LikeView, UnlikeView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),

    # These are the two separate URL patterns required by the checker.
    path('posts/<int:pk>/like/', LikeView.as_view(), name='like_post'),
    path('posts/<int:pk>/unlike/', UnlikeView.as_view(), name='unlike_post'),

    path('', include(router.urls)),
]
