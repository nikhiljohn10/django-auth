
from accounts.models import User
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'bio', 'birthday', 'picture']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Email'}),
            'bio': forms.Textarea(attrs={'rows': '3', 'class': 'form-control mb-3', 'placeholder': 'Bio'}),
            'birthday': forms.DateInput(attrs={'type': 'date', 'class': 'form-control mb-3', 'placeholder': 'Date of Birth'}),
            'picture': forms.ClearableFileInput(attrs={ 'class': 'form-control mb-3', 'placeholder': 'Profile Picture'}),
        }
