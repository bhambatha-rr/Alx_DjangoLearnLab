from django.contrib import admin
from .models import Book

# This line registers the Book model with the admin site.
admin.site.register(Book)
