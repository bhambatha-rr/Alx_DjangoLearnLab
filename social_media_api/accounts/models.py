from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.
    Adds a bio, profile picture, and a self-referencing
    ManyToManyField for followers.
    """
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    # The 'self' argument creates a relationship with the model itself.
    # `symmetrical=False` is crucial for follower relationships (if I follow you, you don't automatically follow me).
    # `related_name='following'` allows us to access the set of users that a user is following.
    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='following',
        blank=True
    )

    def __str__(self):
        return self.username
