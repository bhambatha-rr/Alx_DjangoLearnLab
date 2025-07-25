from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'library', 'publication_year', 'isbn']
        widgets = {
            'publication_year': forms.NumberInput(attrs={'min': 1000, 'max': 2100}),
        }
