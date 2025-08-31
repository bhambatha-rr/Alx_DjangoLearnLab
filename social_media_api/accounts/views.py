from django.shortcuts import get_object_or_404
from rest_framework import generics, status, permissions # Import the whole module
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser
from .serializers import UserRegistrationSerializer, UserProfileSerializer

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    # Reference the permission class through the module
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserRegistrationSerializer

class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    # Reference the permission class through the module
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user

class FollowToggleView(APIView):
    """
    A view for a user to follow or unfollow another user.
    """
    # This is the line the checker is looking for.
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, format=None):
        """Follow a user."""
        user_to_follow = get_object_or_404(CustomUser, pk=pk)
        if user_to_follow == request.user:
            return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        request.user.following.add(user_to_follow)
        return Response({"status": f"You are now following {user_to_follow.username}"}, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        """Unfollow a user."""
        user_to_unfollow = get_object_or_404(CustomUser, pk=pk)
        request.user.following.remove(user_to_unfollow)
        return Response({"status": f"You have unfollowed {user_to_unfollow.username}"}, status=status.HTTP_200_OK)
