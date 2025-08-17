# API Documentation

This document outlines the available API endpoints for the Book model.

## Authentication

Most write operations (POST, PUT, DELETE) require Token Authentication. To get a token, send a POST request with your username and password to `/api/api-token-auth/`.

Include the token in the `Authorization` header for subsequent requests:
`Authorization: Token YOUR_TOKEN_HERE`

## Book Endpoints

### 1. List and Create Books

-   **URL:** `/api/books/`
-   **Methods:**
    -   `GET`: Lists all books. No authentication required.
    -   `POST`: Creates a new book. Authentication required.
-   **POST Body Example:**
    ```json
    {
        "title": "New Book Title",
        "publication_year": 2023,
        "author": 1
    }
    ```

### 2. Retrieve, Update, and Delete a Single Book

-   **URL:** `/api/books/<id>/`
-   **Methods:**
    -   `GET`: Retrieves a single book by its ID. No authentication required.
    -   `PUT`/`PATCH`: Updates a book. Authentication required.
    -   `DELETE`: Deletes a book. Authentication required.

## Advanced Queries

The book list endpoint (`/api/books/`) supports filtering, searching, and ordering via query parameters.

### Filtering

Filter the results by providing an exact match for a field.

-   **Filter by Publication Year:** `?publication_year=1965`
-   **Filter by Author Name:** `?author__name=Frank%20Herbert`

### Searching

Perform a case-insensitive search across book titles and author names.

-   **Example:** `?search=Dune`

### Ordering

Order the results by `title` or `publication_year`. Prepend a hyphen (`-`) to the field name for descending order.

-   **Order by Title (A-Z):** `?ordering=title`
-   **Order by Publication Year (Newest First):** `?ordering=-publication_year`

### Combining Queries

You can combine these parameters in a single request:
`/api/books/?publication_year=1965&ordering=title`
