from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Profile

# Taken from Django project docs - https://docs.djangoproject.com/en/1.11/topics/auth/customizing/#extending-the-existing-user-model
# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class Inline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (Inline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)