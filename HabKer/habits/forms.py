from django import forms
from django.forms import ModelForm

from .models import HabitModel


class HabitForm(ModelForm):

    class Meta:
        model = HabitModel
        fields = ('title', 'description', 'duration', 'start_at', 'finish_at')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.Select(attrs={'class': 'form-control'}),
            'start_at': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}, format="%d/%m/%Y"),
            'finish_at': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
        }
