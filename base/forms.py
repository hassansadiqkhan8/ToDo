from django import forms
from .models import Todo, User
from django.contrib.auth.forms import UserCreationForm



class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["name", "username", "email", "password1", "password2"]




class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "description", "completed"]