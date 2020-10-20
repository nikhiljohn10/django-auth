from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User

from accounts.forms import UserSignUpForm, UserUpdateForm

class AdvanceUserAdmin(UserAdmin):
    add_form = UserSignUpForm
    form = UserUpdateForm
    model = User

admin.site.register(User, AdvanceUserAdmin)