from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Produto

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, 'As senhas não conferem.')
            return render(request, 'register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Nome de usuário já existe.')
            return render(request, 'register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email já está em uso.')
            return render(request, 'register.html')

        user = User.objects.create_user(username=username, email=email, password=password1)
        login(request, user)
        messages.success(request, 'Conta criada com sucesso!')
        return redirect('home')

    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Logout realizado com sucesso!')
    return redirect('login')

@login_required
def home_view(request):
    return render(request, 'home.html')

@login_required
def produtos_baratos(request):
    produtos = Produto.objects.filter(preco__lt=50).order_by('preco')
    return render(request, 'produtos/baratos.html', {'produtos': produtos})
