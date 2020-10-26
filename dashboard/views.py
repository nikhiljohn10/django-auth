from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from dashboard.forms import ProfileForm
from accounts.models import User

@login_required
def home(request):
    return render(request, 'dashboard/home.html')

@login_required
def profile(request):
    return render(request, 'dashboard/profile.html')

@login_required
def profile_disable(request):
    user = request.user
    user.is_active = False
    user.save()
    messages.error(request, 'Profile successfully disabled.')
    return redirect('core:home')

@login_required
def profile_delete(request):
    user = request.user
    user.delete()
    messages.success(request, 'Profile successfully deleted.')
    return redirect('core:home')

class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'dashboard/profile_edit.html'
    success_url = '/dashboard/profile'
    form_class = ProfileForm

    def get_object(self, *args, **kwargs):
        return get_object_or_404(User, pk=self.request.user.pk)

profile_edit = ProfileEditView.as_view()
