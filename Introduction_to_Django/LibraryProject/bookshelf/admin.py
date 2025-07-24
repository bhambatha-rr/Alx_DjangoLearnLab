from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to display
    list_filter = ('author', 'publication_year')  # Right-side filters
    search_fields = ('title', 'author')  # Search box functionality

admin.site.register(Book, BookAdmin)
