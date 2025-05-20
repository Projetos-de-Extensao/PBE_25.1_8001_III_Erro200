from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from myapp.models import Item, Pedido

class Command(BaseCommand):
    help = 'Carrega dados iniciais para o sistema'

    def handle(self, *args, **kwargs):
        # Criando usuários
        users_data = [
            {
                'username': 'admin',
                'first_name': 'Admin',
                'last_name': 'Sistema',
                'email': 'admin@exemplo.com',
                'password': 'admin123',
                'is_staff': True,
                'is_superuser': True
            },
            {
                'username': 'cliente1',
                'first_name': 'João',
                'last_name': 'Silva',
                'email': 'joao@exemplo.com',
                'password': 'senha123'
            },
            {
                'username': 'cliente2',
                'first_name': 'Maria',
                'last_name': 'Santos',
                'email': 'maria@exemplo.com',
                'password': 'senha123'
            }
        ]

        for user_data in users_data:
            user_data['password'] = make_password(user_data['password'])
            User.objects.get_or_create(username=user_data['username'], defaults=user_data)
            self.stdout.write(f"Usuário {user_data['username']} criado com sucesso!")

        # Criando itens
        items_data = [
            {
                'nome': 'Pizza Margherita',
                'descricao': 'Pizza tradicional italiana com molho de tomate, mussarela e manjericão'
            },
            {
                'nome': 'Pizza Calabresa',
                'descricao': 'Pizza com molho de tomate, mussarela e calabresa fatiada'
            },
            {
                'nome': 'Pizza Portuguesa',
                'descricao': 'Pizza com molho de tomate, mussarela, presunto, ovos, cebola e ervilhas'
            }
        ]

        for item_data in items_data:
            Item.objects.get_or_create(nome=item_data['nome'], defaults=item_data)
            self.stdout.write(f"Item {item_data['nome']} criado com sucesso!")

        # Criando pedidos
        pedidos_data = [
            {
                'cliente': User.objects.get(username='cliente1'),
                'valor_total': '89.90',
                'status': 'Entregue',
                'itens_nomes': ['Pizza Margherita', 'Pizza Calabresa']
            },
            {
                'cliente': User.objects.get(username='cliente2'),
                'valor_total': '94.90',
                'status': 'Em trânsito',
                'itens_nomes': ['Pizza Calabresa', 'Pizza Portuguesa']
            }
        ]

        for pedido_data in pedidos_data:
            itens_nomes = pedido_data.pop('itens_nomes')
            pedido = Pedido.objects.create(
                cliente=pedido_data['cliente'],
                valor_total=pedido_data['valor_total'],
                status=pedido_data['status']
            )
            for item_nome in itens_nomes:
                item = Item.objects.get(nome=item_nome)
                pedido.itens.add(item)
            self.stdout.write(f"Pedido {pedido.id} criado com sucesso!")
