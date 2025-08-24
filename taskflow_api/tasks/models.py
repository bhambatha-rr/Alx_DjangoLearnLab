from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # For now, we don't need extra fields, but setting this up
    # makes it easy to add them later (e.g., a profile picture).
    pass
