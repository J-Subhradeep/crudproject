
from django import forms
from .models import TodoList


class Todo(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ["todo", "time"]
        labels = {'todo': 'What to do ? :', "time": 'Set the due time : '}
        widgets = {'todo': forms.TextInput(attrs={'class': 'form-control'}
                                           ), 'time': forms.TimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'})}
