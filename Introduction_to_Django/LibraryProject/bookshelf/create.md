### Create Operation

**Command:**
```python
from bookshelf.models import Book
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()

# A new Book object is created in the database. No direct output is shown in the shell for a successful save.
