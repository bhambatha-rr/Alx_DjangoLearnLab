from django.db import models

class Author(models.Model):
    """
    Represents an author of one or more books.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Represents a book, written by a single author.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()

    # Establishes a many-to-one relationship. Many books can belong to one author.
    # on_delete=models.CASCADE ensures that if an author is deleted, all their books are also deleted.
    # related_name='books' allows us to easily access an author's books (e.g., author.books.all()).
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
