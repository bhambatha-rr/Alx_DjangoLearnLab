from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
    """
    Handles new user registration.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Log the user in automatically after registration
            messages.success(request, 'Registration successful. You are now logged in.')
            return redirect('blog:post_list') # Redirect to a future post list page
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    """
    Allows users to view and update their profile.
    """
    if request.method == 'POST':
        # For simplicity, we'll just handle email updates for now.
        # A more robust solution would use a dedicated UserChangeForm.
        user = request.user
        user.email = request.POST.get('email', user.email)
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.save()
        messages.success(request, 'Your profile has been updated successfully.')
        return redirect('blog:profile')

    return render(request, 'blog/profile.html', {'user': request.user})

def post_list(request):
    # This is a placeholder. We will add posts later.
    return render(request, 'blog/post_list.html', {'posts': []})
