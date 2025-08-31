from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import CustomUser
from .serializers import UserRegistrationSerializer, UserProfileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

class RegisterView(generics.GenericAPIView):
    """
    A view for user registration.
    On successful registration, it returns the user's data and an auth token.
    """
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # The .create() method of our serializer now returns a dictionary
        user_data = serializer.save()
        return Response({
            "user": {
                "username": user_data['username'],
                "email": user_data['email']
            },
            "token": user_data['token']
        }, status=status.HTTP_201_CREATED)

# Keep your ProfileView as it was
class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user

class FollowToggleView(APIView):
    """
    A view for a user to follow or unfollow another user.
    """
    permission_classes = [IsAuthenticated]

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
