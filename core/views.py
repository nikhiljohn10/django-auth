from django.shortcuts import render

def home(request):
	# if request.user.is_authenticated and request.user.is_staff:
	# 	users = User.objects.all()
	# 	return render(request, 'dashboard/home.html', {'users': users})
	return render(request, 'core/home.html')
