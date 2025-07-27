# CRUD Operations for Book Model

## Create Operation
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(f"Book created with ID: {book.id}")
# Output: Book created with ID: 1
retrieved_book = Book.objects.get(id=1)
print(f"Title: {retrieved_book.title}")
print(f"Author: {retrieved_book.author}")
print(f"Publication Year: {retrieved_book.publication_year}")
# Output:
# Title: 1984
# Author: George Orwell
# Publication Year: 1949
from bookshelf.models import Book
book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()
print(f"Updated title: {book.title}")
# Output: Updated title: Nineteen Eighty-Four
from bookshelf.models import Book
book = Book.objects.get(id=1)
book.delete()
# Output: (1, {'bookshelf.Book': 1})

# Confirm deletion
all_books = Book.objects.all()
print(f"Number of books after deletion: {all_books.count()}")
# Output: Number of books after deletion: 0
