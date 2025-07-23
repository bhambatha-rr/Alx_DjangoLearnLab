# Delete Operation

## Command:
```python
from bookshelf.models import Book
book = Book.objects.get(id=1)
book.delete()
# Confirm deletion
all_books = Book.objects.all()
print(f"Number of books after deletion: {all_books.count()}")
# (1, {'bookshelf.Book': 1})
# Number of books after deletion: 0
