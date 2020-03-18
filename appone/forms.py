from django import forms
from django.core import validators
from django.contrib.auth.models import User
from appone.models import protfoluser

class userform (forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields=('username','password','email')

class userprotfform(forms.ModelForm):
    class Meta():
        model=protfoluser
        fields=('prourl','profilepic')

