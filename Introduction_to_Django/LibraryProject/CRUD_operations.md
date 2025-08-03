# Django ORM CRUD Operations

## Create

**Command:**
```python
from bookshelf.models import Book
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()

# A new Book object is created in the database. No direct output is shown in the shell for a successful save.

retrieved_book = Book.objects.get(title="1984")
print(f"Title: {retrieved_book.title}, Author: {retrieved_book.author}, Year: {retrieved_book.publication_year}")

# Title: 1984, Author: George Orwell, Year: 1949

book_to_update = Book.objects.get(title="1984")
book_to_update.title = "Nineteen Eighty-Four"
book_to_update.save()

# Verify the update
updated_book = Book.objects.get(title="Nineteen Eighty-Four")
print(updated_book.title)

# Nineteen Eighty-Four

book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")
book_to_delete.delete()

# Confirm deletion
all_books = Book.objects.all()
print(all_books)

# <QuerySet []>
