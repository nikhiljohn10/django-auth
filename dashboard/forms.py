
from accounts.models import User
# from django.contrib.auth.models import User
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'bio', 'dob']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
        self.fields['first_name'].widget = forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'First Name'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
        self.fields['email'].widget = forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Email'})
        self.fields['bio'].widget = forms.Textarea(attrs={'rows': '3', 'class': 'form-control mb-3', 'placeholder': 'Bio'})
        self.fields['dob'].widget = forms.DateInput(attrs={'type': 'date', 'class': 'form-control mb-3', 'placeholder': 'Date of Birth'})