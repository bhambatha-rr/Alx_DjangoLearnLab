from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import Author, Book

class BookAPITests(APITestCase):
    """
    Test suite for the Book API endpoints.
    """

    def setUp(self):
        """
        Set up the initial data for all tests.
        This method runs before every single test method.
        """
        # Create users
        self.user = User.objects.create_user(username='testuser', password='testpassword123')
        self.token = Token.objects.create(user=self.user)

        # Create authors and books for testing
        self.author1 = Author.objects.create(name='George Orwell')
        self.author2 = Author.objects.create(name='Frank Herbert')

        self.book1 = Book.objects.create(title='1984', publication_year=1949, author=self.author1)
        self.book2 = Book.objects.create(title='Dune', publication_year=1965, author=self.author2)

    def test_list_books_unauthenticated(self):
        """
        Ensure anyone can list books (read-only permission).
        """
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book_unauthenticated(self):
        """
        Ensure unauthenticated users cannot create a book.
        """
        data = {'title': 'Unauthorized Book', 'publication_year': 2024, 'author': self.author1.id}
        response = self.client.post('/api/books/create/', data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated(self):
        """
        Ensure authenticated users can create a book.
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        data = {'title': 'Animal Farm', 'publication_year': 1945, 'author': self.author1.id}
        response = self.client.post('/api/books/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(response.data['title'], 'Animal Farm')

    def test_update_book_authenticated(self):
        """
        Ensure authenticated users can update a book.
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        data = {'title': 'Dune Messiah', 'publication_year': 1969, 'author': self.author2.id}
        response = self.client.put(f'/api/books/update/{self.book2.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book2.refresh_from_db()
        self.assertEqual(self.book2.title, 'Dune Messiah')

    def test_delete_book_authenticated(self):
        """
        Ensure authenticated users can delete a book.
        """
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.delete(f'/api/books/delete/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filtering_by_year(self):
        """
        Test the API's ability to filter books by publication year.
        """
        response = self.client.get('/api/books/?publication_year=1965')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Dune')

    def test_searching_by_title(self):
        """
        Test the API's ability to search for books by title.
        """
        response = self.client.get('/api/books/?search=1984')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], '1984')

    def test_ordering_by_title(self):
        """
        Test the API's ability to order books by title.
        """
        response = self.client.get('/api/books/?ordering=title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # '1984' should come before 'Dune' alphabetically
        self.assertEqual(response.data[0]['title'], '1984')
