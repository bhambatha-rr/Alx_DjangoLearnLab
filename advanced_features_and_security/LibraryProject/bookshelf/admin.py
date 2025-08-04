from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Fields', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_of_birth')

# Register your models
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book)
