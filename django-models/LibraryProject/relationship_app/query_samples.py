import os
import sys
from pathlib import Path
import django

# --- This is the new, crucial part ---
# 1. Find the project's root directory. This is the directory that contains 'manage.py'.
#    Path(__file__) is the path to this script.
#    .resolve() makes it an absolute path.
#    .parent gets the directory containing the script ('relationship_app').
#    .parent again gets the parent of that, which is our project root.
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# 2. Add the project root to Python's path.
#    This allows Python to find the 'LibraryProject' module below.
sys.path.append(str(PROJECT_ROOT))
# --- End of the new part ---

# This boilerplate can now correctly find the settings module.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    """
    Creates sample data and runs the required queries.
    """
    # --- Create Sample Data ---
    print("--- Creating Sample Data ---")
    # Use update_or_create to avoid errors if the script is run multiple times
    author_orwell, _ = Author.objects.update_or_create(name="George Orwell")
    book_1984, _ = Book.objects.update_or_create(title="1984", author=author_orwell)
    book_animal_farm, _ = Book.objects.update_or_create(title="Animal Farm", author=author_orwell)

    main_library, _ = Library.objects.update_or_create(name="Main City Library")
    main_library.books.set([book_1984, book_animal_farm]) # .set() is safer for ManyToMany

    librarian_john, _ = Librarian.objects.update_or_create(name="John Doe", library=main_library)
    print("Sample data created/updated successfully.\n")

    # --- Run Sample Queries ---
    print("--- Running Queries ---")

    # 1. Query all books by a specific author.
    print("\n1. Books by George Orwell:")
    books_by_orwell = Book.objects.filter(author__name="George Orwell")
    for book in books_by_orwell:
        print(f"- {book.title}")

    # 2. List all books in a library.
    print("\n2. Books in Main City Library:")
    library_books = main_library.books.all()
    for book in library_books:
        print(f"- {book.title}")

    # 3. Retrieve the librarian for a library.
    print("\n3. Librarian for Main City Library:")
    # Accessing the one-to-one related object is direct
    library_librarian = main_library.librarian
    print(f"- {library_librarian.name}")

if __name__ == '__main__':
    run_queries()
