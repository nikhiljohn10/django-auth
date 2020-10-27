from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, views, authenticate
from django.contrib.auth.decorators import permission_required
from django.views.generic.edit import CreateView

from accounts.forms import SignUpForm, LoginForm
from accounts.models import User


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


def user_manage_permission(user, username):
    if not user.is_staff:
        if user.username == username:
            return True
    else:
        if user.username != username:
            return True
    return False


def user_disable(request, username):
    if user_manage_permission(request.user, username):
        user = User.objects.get(username=username)
        user.is_active = False
        user.save()
        messages.error(request, 'Profile successfully disabled.')
        return redirect('core:extras')
    else:
        messages.error(
            request, 'You are not allowed to perform this operation.')
    return redirect('dash:profile')


def user_enable(request, username):
    if user_manage_permission(request.user, username):
        user = User.objects.get(username=username)
        user.is_active = True
        user.save()
        messages.success(request, 'Profile successfully enabled.')
        return redirect('core:extras')
    else:
        messages.error(
            request, 'You are not allowed to perform this operation.')
    return redirect('dash:profile')


def user_delete(request, username):
    if user_manage_permission(request.user, username):
        user = User.objects.get(username=username)
        user.delete()
        messages.error(request, 'Profile successfully deleted.')
        return redirect('core:extras')
    else:
        messages.error(
            request, 'You are not allowed to perform this operation.')
    return redirect('dash:profile')


user_login = UserLogin.as_view()
user_signup = SignUpView.as_view()
user_logout = views.LogoutView.as_view()
