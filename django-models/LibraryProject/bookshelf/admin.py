from django.contrib import admin
from .models import Book

# Define a custom admin class for the Book model
class BookAdmin(admin.ModelAdmin):
    """
    Customizes the admin interface for the Book model.
    """
    # 1. Display these fields in the list view columns
    list_display = ('title', 'author', 'publication_year')

    # 2. Add a filter sidebar for these fields
    list_filter = ('publication_year', 'author')

    # 3. Add a search bar that searches these fields
    search_fields = ('title', 'author')

# Register the Book model with its custom admin class
admin.site.register(Book, BookAdmin)
