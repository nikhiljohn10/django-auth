from django.shortcuts import render

from accounts.models import User


def home(request):
    return render(request, 'core/home.html')
