# API Testing Strategy

This document outlines the approach for testing the API endpoints in this project.

## 1. Framework and Setup

-   **Framework:** The project uses Django's built-in test framework, leveraging the `rest_framework.test.APITestCase` class for API-specific testing.
-   **Database:** All tests are run against a separate, temporary test database that is created and destroyed automatically for each test run, ensuring no impact on development data.
-   **Test Data:** A `setUp` method is used within the test suite to create a consistent set of users, authors, and books before each test is executed. This ensures that tests are isolated and repeatable.

## 2. How to Run Tests

To execute the full test suite for the `api` app, navigate to the project root directory and run the following command:

```bash
python manage.py test api
