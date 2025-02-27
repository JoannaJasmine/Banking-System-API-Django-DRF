from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'first_name', 'last_name', 'is_active', 'is_staff', 'date_joined']
    list_filter = ['is_staff', 'is_active']
    search_fields = ['email', 'username']
    ordering = ['email']
    filter_horizontal = []  # Remove 'groups' and 'user_permissions' from here


admin.site.register(CustomUser, CustomUserAdmin)
