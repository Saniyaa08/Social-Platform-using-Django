# social_app/forms.py

from django import forms

class SignupForm(forms.Form):
    name = forms.CharField(max_length=100)
    mobile = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class LoginForm(forms.Form):
    mobile = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
