from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import CustomUser
from .serializers import UserRegistrationSerializer, UserProfileSerializer

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
