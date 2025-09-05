from django.db import models
from django.conf import settings

class Post(models.Model):
    """
    Represents a blog post entry.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    # Links each post to a user. If a user is deleted, all their posts are also deleted.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        # This provides a human-readable representation in the admin panel.
        return self.title
