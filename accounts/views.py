from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from accounts.models import User
from django.contrib.auth.decorators import login_required

from accounts.forms import SignUpForm, LoginForm


def user_login(request):
    redirect_to = request.GET.get('next', None) or 'dash:home'
    if not request.user.is_authenticated:
        form = LoginForm()
        if request.method == 'POST':
            form = LoginForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    if not request.POST.get('remember_me', None):
                        request.session.set_expiry(0)
                    login(request, user)
                    messages.info(request, f"You are now logged in as {username}")
                    return redirect(redirect_to)
        return render(request, 'auth/login.html', {'form': form})
    return redirect(redirect_to)


def user_signup(request):
    redirect_to = request.GET.get('next', None) or 'dash:home'
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(redirect_to)
    return render(request, 'auth/signup.html', {'form': form})


def user_logout(request):
    redirect_to = request.GET.get('next', None) or 'dash:home'
    if request.user.is_authenticated:
        logout(request)
    return redirect(redirect_to)
