from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from tarefas.models import Usuario
from django.contrib.auth.hashers import make_password

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
        
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'Email já cadastrado.')
            return redirect('cadastro')
        
        usuario = Usuario.objects.create_user(
            email=email,
            nome=nome,
            password=senha 
        )

        
        messages.success(request, 'Cadastro realizado com sucesso!')
        return redirect('login')
    
    return render(request, 'auth/cadastro.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        
        usuario = authenticate(request, email=email, password=senha)
        
        if usuario is not None:
            login(request, usuario)
            return redirect('home')
        else:
            messages.error(request, 'Email ou senha incorretos.')
            return redirect('login')
    
    return render(request, 'auth/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')