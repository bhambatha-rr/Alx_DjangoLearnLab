from rest_framework import serializers
from .models import Author, Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model. Includes all fields and adds
    custom validation for the publication_year.
    """
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """
        Check that the publication year is not in the future.
        """
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model. It includes a nested representation
    of all the books related to the author.
    """
    # This field uses the BookSerializer to represent the related books.
    # `many=True` indicates that this is a list of objects.
    # `read_only=True` means this field will be used for serialization (reading data)
    # but not for deserialization (creating/updating data).
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        # We explicitly list the fields to include the nested 'books' field.
        fields = ['id', 'name', 'books']
