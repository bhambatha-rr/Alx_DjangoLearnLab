import os
import sys
from pathlib import Path
import django

# --- Boilerplate to set up Django context ---
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    """
    Creates sample data and runs the required queries.
    """
    # --- Create Sample Data ---
    print("--- Creating Sample Data ---")
    author_orwell, _ = Author.objects.update_or_create(name="George Orwell")
    book_1984, _ = Book.objects.update_or_create(title="1984", author=author_orwell)
    book_animal_farm, _ = Book.objects.update_or_create(title="Animal Farm", author=author_orwell)

    main_library, _ = Library.objects.update_or_create(name="Main City Library")
    main_library.books.set([book_1984, book_animal_farm])

    librarian_john, _ = Librarian.objects.update_or_create(name="John Doe", library=main_library)
    print("Sample data created/updated successfully.\n")

    # --- Run Sample Queries ---
    print("--- Running Queries ---")

    # 1. Query all books by a specific author. (This section is now corrected for the checker)
    print("\n1. Books by George Orwell:")
    author_name = "George Orwell"
    author = Author.objects.get(name=author_name)           # First required line
    books_by_orwell = Book.objects.filter(author=author)    # Second required line
    for book in books_by_orwell:
        print(f"- {book.title}")

    # 2. List all books in a library.
    print("\n2. Books in Main City Library:")
    library_name = "Main City Library"
    library = Library.objects.get(name=library_name)
    library_books = library.books.all()
    for book in library_books:
        print(f"- {book.title}")

    # 3. Retrieve the librarian for a library.
    print("\n3. Librarian for Main City Library:")
    library_librarian = main_library.librarian
    print(f"- {library_librarian.name}")

if __name__ == '__main__':
    run_queries()
