from django.contrib.auth.models import User
from django import forms
from .models import Users_listt, Photo
from django.forms import ModelForm


class UserForm(forms.ModelForm):

    class Meta:
        model = Users_listt
        fields = "__all__"

