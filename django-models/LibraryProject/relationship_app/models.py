from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    # ForeignKey relationship: Many books can belong to one author.
    # on_delete=models.CASCADE means if an Author is deleted, all their books are also deleted.
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)
    # ManyToMany relationship: A library can have many books, and a book can be in many libraries.
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    # OneToOne relationship: Each library has exactly one librarian.
    # on_delete=models.CASCADE means if a Library is deleted, its Librarian is also deleted.
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
