'''Criando este arquivo para poder alterar o formulario para receber outras informações 
como email, além de usuario e senha'''

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Abaixo, criaremos uma nova classe

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']