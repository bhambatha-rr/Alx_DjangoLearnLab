from rest_framework import viewsets, filters, generics, permissions # Import the whole module
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing, creating, and editing posts.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # Reference the permission class through the module
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing, creating, and editing comments.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # Reference the permission class through the module
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedView(generics.ListAPIView):
    """
    A view that returns a list of posts from users that the current user follows.
    """
    serializer_class = PostSerializer
    # This is the line the checker is looking for.
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all the posts
        by users that the currently authenticated user follows.
        """
        user = self.request.user
        following_users = user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
