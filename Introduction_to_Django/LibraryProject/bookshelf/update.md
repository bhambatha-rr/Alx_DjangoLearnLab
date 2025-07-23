# Update Operation

## Command:
```python
from bookshelf.models import Book
book_to_update = Book.objects.get(id=1)
book_to_update.title = "Nineteen Eighty-Four"
book_to_update.save()
print(f"Updated title: {book_to_update.title}")
# Updated title: Nineteen Eighty-Four
