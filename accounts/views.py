from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, views, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.sessions.models import Session
from django.views.generic.edit import CreateView

from accounts.forms import SignUpForm, LoginForm
from accounts.models import User
from accounts.tools import activater


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
        print(activater.make_token(user))
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


@login_required
@permission_required("is_staff", login_url='/dashboard/')
def user_force_logout(request, username):
    user = User.objects.get(username=username)
    sessions = [s.delete() for s in Session.objects.all()
                if s.get_decoded().get('_auth_user_id') == str(user.id)]
    print(sessions)
    return redirect('dash:users')


@login_required
@permission_required("is_staff", login_url='/dashboard/')
def user_verify_email(request, username, token):
    user = User.objects.get(username=username)
    if activater.check_token(user, token):
        print(user, "is verified")
        user.email_verified = True
        user.save()
    return redirect('dash:users')


@login_required
def user_disable(request, username):
    if user_manage_permission(request.user, username):
        user = User.objects.get(username=username)
        user.is_active = False
        user.save()
        messages.error(request, 'Profile successfully disabled.')
    else:
        messages.error(
            request, 'You are not allowed to perform this operation.')
    if request.user.is_staff:
        return redirect('dash:users')
    else:
        return redirect('dash:profile')


@login_required
def user_enable(request, username):
    if user_manage_permission(request.user, username):
        user = User.objects.get(username=username)
        user.is_active = True
        user.save()
        messages.success(request, 'Profile successfully enabled.')
    else:
        messages.error(
            request, 'You are not allowed to perform this operation.')
    if request.user.is_staff:
        return redirect('dash:users')
    else:
        return redirect('dash:profile')


@login_required
def user_delete(request, username):
    if user_manage_permission(request.user, username):
        user = User.objects.get(username=username)
        user.delete()
        messages.error(request, 'Profile successfully deleted.')
    else:
        messages.error(
            request, 'You are not allowed to perform this operation.')
    if request.user.is_staff:
        return redirect('dash:users')
    else:
        return redirect('dash:profile')


user_login = UserLogin.as_view()
user_signup = SignUpView.as_view()
user_logout = views.LogoutView.as_view()
