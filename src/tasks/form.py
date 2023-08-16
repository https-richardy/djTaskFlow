from django import forms
from tasks.models import Task


class TaskForm(forms.ModelForm):
    title = forms.CharField(
        label='Título da Tarefa',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Um título para sua tarefa.'
        })
    )
    description = forms.CharField(
        label='Descrição da Tarefa',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Descreva sua tarefa.'
        })
    )

    class Meta:
        model = Task
        fields = (
            'title', 'description',
        )

    widgets = {
        'completed': forms.HiddenInput()
    }
