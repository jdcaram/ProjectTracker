from __future__ import division, print_function, unicode_literals

from django import forms
from django.contrib.auth.models import User

from tracker.models import UserProfile, Task


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')


class TaskForm(forms.ModelForm):
    name = forms.CharField(max_length=100, help_text="Please enter the task name.")
    description = forms.CharField(max_length=255)
    order = forms.IntegerField()
    status = forms.ChoiceField(choices=Task.STATUS_VALUES)

    class Meta:
        model = Task
        fields = ('name', 'description', 'order', 'status')
