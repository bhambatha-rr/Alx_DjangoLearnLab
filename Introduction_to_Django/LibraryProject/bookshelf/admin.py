from django.contrib import admin
from .models import Book

# Define the admin class
class BookAdmin(admin.ModelAdmin):
    # 1. Customize the list display
    list_display = ('title', 'author', 'publication_year')

    # 2. Add search functionality
    search_fields = ('title', 'author')

    # 3. Add filters
    list_filter = ('publication_year', 'author')

# Register the model with the custom admin class
admin.site.register(Book, BookAdmin)