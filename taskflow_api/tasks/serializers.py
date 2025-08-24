from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        # We only want to handle these fields for registration
        fields = ['id', 'username', 'email', 'password']
        # Make the password write-only for security
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # This method handles creating the user with a hashed password
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
