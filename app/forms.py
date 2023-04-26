from django import forms
from .models import Users_listt, Photo 


class UserForm(forms.ModelForm):

    class Meta:
        model = Users_listt
        fields = "__all__"

