from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from myapp.models import UserProfile, Porto, Posto, Pedido
from decimal import Decimal
import random

class Command(BaseCommand):
    help = 'Load initial data for development'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating initial data...')
        
        # Create Portos
        porto1 = Porto.objects.create(nome='Porto Principal', doca='Doca A1')
        porto2 = Porto.objects.create(nome='Porto Secundário', doca='Doca B2')
        
        # Create Postos
        posto1 = Posto.objects.create(nome='Posto Central', armario='ARM-101')
        posto2 = Posto.objects.create(nome='Posto Shopping', armario='ARM-202')
        posto3 = Posto.objects.create(nome='Posto Mercado', armario='ARM-303')

        # Create Admin
        admin_user = User.objects.create_user(
            username='admin',
            password='1234',
            first_name='Admin',
            last_name='System',
            email='admin@example.com',
            is_staff=True,
            is_superuser=True
        )
        UserProfile.objects.create(user=admin_user, user_type='ADMIN')

        # Create Entregadores
        entregadores = []
        for i in range(1):
            user = User.objects.create_user(
                username=f'entregador{i+1}',
                password='1234',
                first_name=f'Entregador{i+1}',
                last_name='Silva',
                email=f'entregador{i+1}@example.com'
            )
            UserProfile.objects.create(user=user, user_type='ENTREGADOR')
            entregadores.append(user)

        # Create Barqueiros
        barqueiros = []
        for i in range(1):
            user = User.objects.create_user(
                username=f'barqueiro{i+1}',
                password='1234',
                first_name=f'Barqueiro{i+1}',
                last_name='Santos',
                email=f'barqueiro{i+1}@example.com'
            )
            UserProfile.objects.create(user=user, user_type='BARQUEIRO')
            barqueiros.append(user)

        # Create Moradores (clients)
        moradores = []
        for i in range(3):
            user = User.objects.create_user(
                username=f'morador{i+1}',
                password='1234',
                first_name=f'Morador{i+1}',
                last_name='Pereira',
                email=f'morador{i+1}@example.com'
            )
            UserProfile.objects.create(user=user, user_type='MORADOR')
            moradores.append(user)

        # Create Pedidos (Orders)
        status_choices = ['A_CONFIRMAR']
        descriptions = [
            'Caixa com livros',
            'Pacote de roupas',
            'Material escolar',
            'Compras do mercado',
            'Documentos importantes',
            'Eletrônicos',
            'Materiais de construção',
            'Artigos de decoração'
        ]

        # Create multiple orders for each morador
        for morador in moradores:
            num_orders = random.randint(2, 4)  # Each morador will have 2-4 orders
            
            for _ in range(num_orders):
                status = random.choice(status_choices)
                valor_proposto = Decimal(random.randint(5000, 20000)) / 100  # Values between 50.00 and 200.00
                
                # Assign entregador and barqueiro based on status
                entregador = None
                barqueiro = None

                valor_final = valor_proposto if status == 'CONCLUIDO' else None

                Pedido.objects.create(
                    cliente=morador,
                    entregador=entregador,
                    barqueiro=barqueiro,
                    descricao=random.choice(descriptions),
                    valor_proposto=valor_proposto,
                    valor_final=valor_final,
                    porto_origem=random.choice([porto1, porto2]),
                    posto_destino=random.choice([posto1, posto2, posto3]),
                    status=status
                )

        self.stdout.write(self.style.SUCCESS('Successfully created initial data'))