from django.shortcuts import (
    render,
    redirect,
    get_object_or_404)

from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django_otp.plugins.otp_totp.models import TOTPDevice

class TOTPCreateView(LoginRequiredMixin, CreateView):
    model = TOTPDevice
    fields = ['name', 'confirmed']
    template_name = 'device/new.html'
    success_url = '/accounts/device/'

    def form_valid(self, form):
        try:
            TOTPDevice.objects.get(user=self.request.user).delete()
        except TOTPDevice.DoesNotExist:
            pass
        form.instance.user = self.request.user
        return super().form_valid(form)

@login_required
def user_device(request):
    try:
        device = TOTPDevice.objects.get(user=request.user)
        secret = [ param for param in device.config_url.split('?')[1].split('&') if 'secret' in param ][0].split('=')[1]
        return render(request, 'device/detail.html', {
            'name': device.name,
            'device_url': device.config_url,
            'secret': secret})
    except(TOTPDevice.MultipleObjectsReturned, TOTPDevice.DoesNotExist):
        return redirect('create_device')

@login_required
def user_profile(request):
    user = User.objects.get(username=request.user)
    return render(request, 'auth/user_detail.html', {"user":user})

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'auth/user_signup.html'
    success_url = '/accounts/profile'

class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'auth/user_edit.html'
    fields = ['username', 'first_name', 'last_name', 'email']
    success_url = '/accounts/profile'

    def get_object(self, *args, **kwargs):
        return get_object_or_404(User, pk=self.request.user.pk)
