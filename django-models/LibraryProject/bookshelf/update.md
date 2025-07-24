# Update Operation

## Command:
```python
from bookshelf.models import Book
book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()
print(f"Updated title: {book.title}")
# Updated title: Nineteen Eighty-Four
