from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from userauth.forms import SignUpForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def home(request):
	if request.user.is_authenticated and request.user.is_staff:
		users = User.objects.all()
		return render(request, 'home.html', {'users': users})
	return render(request, 'home.html')

def login_user(request):
	if not request.user.is_authenticated:
		form = LoginForm()
		if request.method == 'POST':
			form = LoginForm(data=request.POST)
			if form.is_valid():
				username = form.cleaned_data.get('username')
				password = form.cleaned_data.get('password')
				user = authenticate(username=username, password=password)
				login(request, user)
				return redirect('home')
		return render(request, 'login.html', {'form': form})
	return redirect('home')

def signup_user(request):
	form = SignUpForm()
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('home')
	return render(request, 'signup.html', {'form': form})

@login_required
def logout_user(request):
	logout(request)
	return redirect('home')