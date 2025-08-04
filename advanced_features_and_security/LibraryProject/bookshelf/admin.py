from django.contrib import admin
from .models import CustomUser, Book

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'date_of_birth')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_active')
    ordering = ('email',)

# Register your models
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book)
