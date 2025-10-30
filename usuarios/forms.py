from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','documento','telefono','password1','password2')
