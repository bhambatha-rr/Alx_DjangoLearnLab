from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Add your custom fields to the fieldsets
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Fields', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    # Display custom fields in the list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_of_birth')

admin.site.register(CustomUser, CustomUserAdmin)
