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

@login_required(login_url='/auth/login/')
def user_profile(request):
	return render(request, 'profile.html')

def user_login(request):
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

def user_signup(request):
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
def user_logout(request):
	logout(request)
	return redirect('home')
