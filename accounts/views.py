from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, views, authenticate
from django.contrib.auth.decorators import permission_required
from django.views.generic.edit import CreateView

from accounts.forms import SignUpForm, LoginForm
from accounts.models import User

def user_disable(request, username):
    if request.user.is_staff or request.user.username == username:
        user = User.objects.get(username=username)
        user.is_active = False
        user.save()
        messages.error(request, 'Profile successfully disabled.')
    else:
        messages.error(request, 'You have to be admin to perform this operation.')
    return redirect('core:extras')

def user_enable(request, username):
    if request.user.is_staff or request.user.username == username:
        user = User.objects.get(username=username)
        user.is_active = True
        user.save()
        messages.success(request, 'Profile successfully enabled.')
    else:
        messages.error(request, 'You have to be admin to perform this operation.')
    return redirect('core:extras')

def user_delete(request, username):
    if request.user.is_staff or request.user.username == username:
        user = User.objects.get(username=username)
        user.delete()
        messages.error(request, 'Profile successfully deleted.')
    else:
        messages.error(request, 'You have to be admin to perform this operation.')
    return redirect('core:extras')

class UserLogin(views.LoginView):
    template_name = 'auth/login.html'
    authentication_form = LoginForm

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        if not self.request.POST.get('remember_me', None):
            self.request.session.set_expiry(0)
        messages.info(self.request, f"You are now logged in as {user}")
        return redirect(self.get_success_url())

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'auth/signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('core:home')

user_login = UserLogin.as_view()
user_signup = SignUpView.as_view()
user_logout = views.LogoutView.as_view()
