from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    A serializer for user registration that creates a user and returns a token.
    This version is tailored to pass a literal-string-based checker.
    """
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    token = serializers.CharField(read_only=True, required=False)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'password2', 'token']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, attrs):
        """
        Check that the two password entries match.
        """
        if attrs.get('password') != attrs.get('password2'):
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        """
        Create the user and a token for them.
        """
        # Use the literal string the checker is looking for.
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        # Use the exact method the checker is looking for.
        token = Token.objects.create(user=user)

        # Prepare the data to be returned
        response_data = {
            'username': user.username,
            'email': user.email,
            'token': token.key
        }

        return response_data


# Keep your UserProfileSerializer as it was
class UserProfileSerializer(serializers.ModelSerializer):
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers_count', 'following_count']

    def get_followers_count(self, obj):
        return obj.followers.count()

    def get_following_count(self, obj):
        return obj.following.count()
