from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def home(request):
	return render(request, 'dashboard/home.html')

@login_required
def profile(request):
	return render(request, 'dashboard/profile.html')

@login_required
def edit_profile(request):
	return render(request, 'dashboard/profile.html')
