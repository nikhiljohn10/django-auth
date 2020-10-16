from django import forms

from todo.models import Task

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('title',)
        widgets = {
            'title': forms.TextInput(attrs={
                'autofocus': '',
                'placeholder': 'Task'}),}
