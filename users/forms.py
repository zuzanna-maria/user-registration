from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import CustomUser

from django.contrib.auth.models import User

from django.forms.widgets import SelectDateWidget
from .schools import SCHOOL_NAMES

import sys
sys.setrecursionlimit(600000000)

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=101)
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()
    date_of_birth = forms.DateField(widget=SelectDateWidget)
    school= forms.CharField(widget=forms.Select(choices=SCHOOL_NAMES))


    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'school', 'date_of_birth']

    def save(self, commit = True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        user.is_active = True
        if commit:
            user.save()
        return user
