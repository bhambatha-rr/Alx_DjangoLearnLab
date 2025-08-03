### Create Operation

**Command:**
```python
from bookshelf.models import Book
Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Creates and saves a new Book instance in a single step. Returns the new Book object.
