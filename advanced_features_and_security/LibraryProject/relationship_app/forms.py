from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        # Only list the fields that are in your Book model
        fields = ['title', 'author' , 'publication_year']
