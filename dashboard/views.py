from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from dashboard.forms import ProfileForm
from accounts.models import User


@login_required
def home(request):
    return render(request, 'dashboard/home.html')


@login_required
def profile(request):
    return render(request, 'dashboard/profile.html')


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'dashboard/profile_edit.html'
    success_url = '/dashboard/profile'
    form_class = ProfileForm

    def get_object(self, *args, **kwargs):
        return get_object_or_404(User, pk=self.request.user.pk)
