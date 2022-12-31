from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from apps.userprofile.models import UserProfile
from django.contrib.auth.forms import UserCreationForm


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ("avatar",)

        widgets = {
            'avatar': forms.FileInput(attrs={'accept': 'image/*'}),
        }