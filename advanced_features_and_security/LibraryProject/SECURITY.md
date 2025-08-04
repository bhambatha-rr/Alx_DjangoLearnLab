# Application Security Measures

This document outlines the security measures implemented in this project.

## 1. Secure Settings (`settings.py`)

-   `DEBUG` is set to `False` to prevent leaking sensitive information in production.
-   `ALLOWED_HOSTS` is configured to only accept requests from trusted domains.
-   `CSRF_COOKIE_SECURE = True` and `SESSION_COOKIE_SECURE = True` enforce the use of HTTPS for cookies.
-   `SECURE_BROWSER_XSS_FILTER`, `SECURE_CONTENT_TYPE_NOSNIFF`, and `X_FRAME_OPTIONS` are enabled to add extra layers of browser-side security against XSS, MIME-sniffing, and clickjacking.

## 2. CSRF Protection

All forms that modify data use the `{% csrf_token %}` template tag to protect against Cross-Site Request Forgery attacks.

## 3. SQL Injection Prevention

All database queries are performed using the Django ORM. The search functionality in the `book_list` view uses `Model.objects.filter(title__icontains=query)`, which parameterizes the query and makes it safe from SQL injection. No raw SQL queries with string formatting are used.

## 4. Content Security Policy (CSP)

The `django-csp` middleware is enabled. The policy is configured to be very strict (`CSP_DEFAULT_SRC = ("'self'",)`), allowing content to be loaded only from the same domain. This significantly reduces the risk of Cross-Site Scripting (XSS) from external sources.
