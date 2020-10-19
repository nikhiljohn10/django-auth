from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def home(request):
	if request.user.is_authenticated and request.user.is_staff:
		users = User.objects.all()
		return render(request, 'dashboard/home.html', {'users': users})
	return render(request, 'dashboard/home.html')

@login_required
def profile(request):
	return render(request, 'dashboard/profile.html')
