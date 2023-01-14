from django import forms
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError


class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email"]

    def clean_email(self):
        data = self.cleaned_data["email"]
        user = User.objects.filter(email=data)
        if user:
            raise ValidationError("User with that email already exist")

        return data
