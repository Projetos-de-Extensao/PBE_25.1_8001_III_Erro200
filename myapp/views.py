from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import transaction
from .models import Produto, Pedido, ItemPedido, ItemPedidoCustom

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
        # Coletar dados dos itens do formulário
        itens_data = []
        i = 0
        while f'nome_{i}' in request.POST:
            nome = request.POST.get(f'nome_{i}')
            descricao = request.POST.get(f'descricao_{i}')
            quantidade = int(request.POST.get(f'quantidade_{i}'))
            preco = float(request.POST.get(f'preco_{i}'))
            
            if nome and descricao and quantidade and preco:
                itens_data.append({
                    'nome': nome,
                    'descricao': descricao,
                    'quantidade': quantidade,
                    'preco_unitario': preco
                })
            i += 1
        
        if itens_data:
            with transaction.atomic():
                # Criar o pedido
                pedido = Pedido.objects.create(usuario=request.user)
                
                # Criar os itens do pedido
                for item_data in itens_data:
                    ItemPedidoCustom.objects.create(
                        pedido=pedido,
                        nome=item_data['nome'],
                        descricao=item_data['descricao'],
                        quantidade=item_data['quantidade'],
                        preco_unitario=item_data['preco_unitario']
                    )
                
                messages.success(request, 'Pedido criado com sucesso!')
                return redirect('meus-pedidos')
        else:
            messages.error(request, 'Adicione pelo menos um item ao pedido.')
            
    return render(request, 'pedidos/novo_pedido.html')

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
