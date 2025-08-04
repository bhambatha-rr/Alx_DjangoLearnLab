### Update Operation

**Command:**
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# The title attribute of the book is updated in the database. No direct output is shown.
