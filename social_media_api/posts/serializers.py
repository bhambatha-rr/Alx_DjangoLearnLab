from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    # Display the author's username instead of their ID
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'author', 'post', 'content', 'created_at']

class PostSerializer(serializers.ModelSerializer):
    # Display the author's username instead of their ID
    author = serializers.ReadOnlyField(source='author.username')
    # Nest the comments directly within the post's detail view
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at', 'comments']
