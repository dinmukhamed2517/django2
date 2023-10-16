from django import forms
from .models import Problem

class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        exclude = ['date_of_creation', 'reported_by']

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)