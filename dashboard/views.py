from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.forms import TextInput, EmailInput

@login_required
def home(request):
    return render(request, 'dashboard/home.html')

@login_required
def profile(request):
    return render(request, 'dashboard/profile.html')

@login_required
def edit_profile(request):
    return render(request, 'dashboard/profile.html')

class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'dashboard/profile_edit.html'
    fields = ['username', 'first_name', 'last_name', 'email']
    success_url = '/dashboard/profile'
    widgets = {
        'username': TextInput(attrs={'class': 'form-control',})
    }

    def get_object(self, *args, **kwargs):
        return get_object_or_404(User, pk=self.request.user.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
