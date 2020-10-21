from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, UsernameField
from accounts.models import User
from django.utils.translation import gettext_lazy as _
from django import forms

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'bio', 'dob', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
        self.fields['first_name'].widget = forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'First Name'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
        self.fields['email'].widget = forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Email'})
        self.fields['bio'].widget = forms.Textarea(attrs={'rows': '3', 'class': 'form-control mb-3', 'placeholder': 'Bio'})
        self.fields['dob'].widget = forms.DateInput(attrs={'type': 'date', 'class': 'form-control mb-3', 'placeholder': 'Date of Birth'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'New Password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Confirm Password'})


class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'})



class UserSignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username',)

class UserUpdateForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username',)
