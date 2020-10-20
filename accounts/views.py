from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from accounts.forms import SignUpForm, LoginForm

def user_login(request):
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
                    return redirect('dash:home')
        return render(request, 'auth/login.html', {'form': form})
    return redirect('dash:home')

def user_signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dash:home')
    return render(request, 'auth/signup.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('dash:home')
