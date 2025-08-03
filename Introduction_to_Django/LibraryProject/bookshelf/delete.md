### Delete Operation

**Command:**
```python
book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")
book_to_delete.delete()

# Confirm deletion
all_books = Book.objects.all()
print(all_books)

# <QuerySet []>
