from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from .models import Book, Library, UserProfile
from .forms import BookForm

# --- Helper functions for role checks ---
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# --- Existing Views ---
def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

# ... other existing views like register, admin_view, etc. ...
def register(request):
    # ... your existing register code ...
    pass

@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


# --- NEW Function-Based Views with Permission Decorators ---

@permission_required('relationship_app.can_add_book', raise_exception=True)
def book_add(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('relationship_app:list_books')
    else:
        form = BookForm()
    return render(request, 'relationship_app/book_form.html', {'form': form})

@permission_required('relationship_app.can_change_book', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('relationship_app:list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/book_form.html', {'form': form})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('relationship_app:list_books')
    return render(request, 'relationship_app/book_confirm_delete.html', {'object': book})
```*Note: I've left placeholders for your other views to make it clear you should replace the file's content but ensure all necessary functions are present.*

### **Step 2: Update `urls.py` to Use the New Views**

Now we must update `relationship_app/urls.py` to point to these new function-based views instead of the old class-based ones.

**Replace the entire content of `relationship_app/urls.py` with this version:**

```python
# relationship_app/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'relationship_app'

urlpatterns = [
    # Existing URLs
    path('books/', views.list_books, name='list_books'),
    # path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'), # This might need to be removed if LibraryDetailView was deleted
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),

    # UPDATED CRUD URLs for Books pointing to function-based views
    path('book/add/', views.book_add, name='book_add'),
    path('book/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('book/<int:pk>/delete/', views.book_delete, name='book_delete'),
]
