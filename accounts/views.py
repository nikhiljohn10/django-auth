from django.shortcuts import render, redirect as redirect_url
from django.contrib import messages
from django.contrib.auth import login, logout, views
from accounts.forms import SignUpForm, LoginForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Custom redirection function to use next parameter from url
def redirect(request, default='dash:home'):
    return redirect_url(request.GET.get('next', None) or default)


class UserLogin(views.LoginView):
    template_name = 'auth/login.html'
    authentication_form = LoginForm

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        if not self.request.POST.get('remember_me', None):
            self.request.session.set_expiry(0)
        messages.info(self.request, f"You are now logged in as {user}")
        return redirect_url(self.get_success_url())

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'auth/signup.html'
    success_url = reverse_lazy('core:home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

user_login = UserLogin.as_view()
user_signup = SignUpView.as_view()
user_logout = views.LogoutView.as_view()
