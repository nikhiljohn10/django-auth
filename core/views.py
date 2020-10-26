from django.shortcuts import render

from accounts.models import User


def home(request):
    return render(request, 'core/home.html')

def extras(request):
    users = User.objects.filter(is_active=False)
    return render(request, 'core/extras.html', {'users': users})
