from django import forms
from django.forms import ModelForm, Form
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField()

    class Meta:
        fields = ['username', 'password']
