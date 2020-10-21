from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from accounts.models import User

from accounts.forms import UserSignUpForm, UserUpdateForm

@admin.register(User)
class AdvanceUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (_('Profile'), {'fields': ('bio', 'dob')}),
    )
