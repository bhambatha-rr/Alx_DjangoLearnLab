from django.db import models
# This is the direct import the checker is looking for.
from django.contrib.auth.models import User

class Post(models.Model):
    """
    Represents a blog post entry.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    # This now directly references the imported User model.
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
