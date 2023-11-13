from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

""" A classe UserCreationForm vem com alguns campos de formulário
predefinidos que são necessários para criar um usuário, como username, email e password1 e password2.
Ela também inclui a lógica para validar que as duas senhas são iguais e para salvar o usuário no banco 
de dados.""" 

# Create your views here.
def novo_usuario(request):
    #tipo, validar, informar, salvar
    if request.method == 'POST':
        formulario = UserRegisterForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            usuario = formulario.cleaned_data.get('username')
            messages.success(request, f'O usuário {usuario} foi criado com sucesso!')
            return redirect('login')    
    else:
        formulario = UserRegisterForm()
        
        
    return render(request, 'usuarios/registrar.html', {'formulario':formulario})    
    
    
"""A função cleaned_data no Django é usada para 
acessar os dados limpos e validados de um formulário."""    