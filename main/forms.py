from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:  # extra settings
        model = Task
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': "form-control",
                'placeholder': "Write a title"
            }),
            "task": Textarea(attrs={
                'class': "form-control",
                'placeholder': "Write a task"
            }),
        }
