from dataclasses import fields
import email
from pyexpat import model
from django import forms
from .models import Comentario
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class ComentarioForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ["nombre", "email" ,"telefono", "comentario"]
        #fields = '__all__'


class userForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'password2']

class loginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholer': 'Username','class': 'form-field-label',}))
    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-field-label', 'data-toggle': 'password', 'id': 'password', 'name': 'password',}))
    remember_me = forms.BooleanField(required=False)
