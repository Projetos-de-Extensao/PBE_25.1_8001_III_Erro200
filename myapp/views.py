from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import transaction
from .models import Produto, Pedido, ItemPedido

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

def is_admin(user):
    return user.is_superuser

@login_required
def home_view(request):
    if request.user.is_superuser:
        return redirect('gerenciar-pedidos')
    return redirect('meus-pedidos')

@login_required
def produtos_baratos(request):
    produtos = Produto.objects.filter(preco__lt=50).order_by('preco')
    return render(request, 'produtos/baratos.html', {'produtos': produtos})

@login_required
def meus_pedidos(request):
    pedidos = Pedido.objects.filter(usuario=request.user).order_by('-data_criacao')
    return render(request, 'pedidos/meus_pedidos.html', {'pedidos': pedidos})

@login_required
def novo_pedido(request):
    if request.method == 'POST':
        produtos_selecionados = []
        for key, value in request.POST.items():
            if key.startswith('produto_') and int(value) > 0:
                produto_id = int(key.split('_')[1])
                quantidade = int(value)
                produtos_selecionados.append((produto_id, quantidade))
        
        if produtos_selecionados:
            with transaction.atomic():
                pedido = Pedido.objects.create(usuario=request.user)
                for produto_id, quantidade in produtos_selecionados:
                    produto = Produto.objects.get(id=produto_id)
                    ItemPedido.objects.create(
                        pedido=pedido,
                        produto=produto,
                        quantidade=quantidade,
                        preco_unitario=produto.preco
                    )
                messages.success(request, 'Pedido criado com sucesso!')
                return redirect('meus-pedidos')
        else:
            messages.error(request, 'Selecione pelo menos um produto.')
    
    produtos = Produto.objects.filter(disponivel=True)
    return render(request, 'pedidos/novo_pedido.html', {'produtos': produtos})

@user_passes_test(is_admin)
def gerenciar_pedidos(request):
    pedidos = Pedido.objects.all().order_by('-data_criacao')
    return render(request, 'pedidos/gerenciar_pedidos.html', {'pedidos': pedidos})

@user_passes_test(is_admin)
def processar_pedido(request, pedido_id):
    if request.method == 'POST':
        pedido = get_object_or_404(Pedido, id=pedido_id)
        acao = request.POST.get('acao')
        
        if acao == 'aceitar':
            pedido.status = 'ACEITO'
            messages.success(request, 'Pedido aceito com sucesso!')
        elif acao == 'rejeitar':
            pedido.status = 'REJEITADO'
            messages.success(request, 'Pedido rejeitado com sucesso!')
        
        pedido.save()
    return redirect('gerenciar-pedidos')

@login_required
def confirmar_entrega(request, pedido_id):
    if request.method == 'POST':
        pedido = get_object_or_404(Pedido, id=pedido_id, usuario=request.user)
        if pedido.status == 'ACEITO':
            pedido.status = 'ENTREGUE'
            pedido.save()
            messages.success(request, 'Entrega confirmada com sucesso!')
        else:
            messages.error(request, 'Este pedido não pode ser confirmado como entregue.')
    return redirect('meus-pedidos')
