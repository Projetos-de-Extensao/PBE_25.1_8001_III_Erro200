from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from myapp.models import Item, Pedido, Porto, Posto, UserProfile
import json
import os
from django.conf import settings
from datetime import datetime
from django.utils.timezone import make_aware

class Command(BaseCommand):
    help = 'Carrega dados iniciais do arquivo JSON'

    def handle(self, *args, **options):
        json_file_path = os.path.join(settings.BASE_DIR, 'myapp', 'fixtures', 'initial_data.json')
        
        try:
            with open(json_file_path, 'r') as file:
                data = json.load(file)

            # Criar usuários
            for user_data in data['users']:
                fields = user_data['fields']
                user = User.objects.create_user(
                    username=fields['username'],
                    email=fields['email'],
                    password=fields['password'],
                    first_name=fields['first_name'],
                    last_name=fields['last_name'],
                )
                self.stdout.write(f'Usuário {fields["username"]} criado com sucesso!')

            # Criar perfis de usuário
            for profile_data in data['user_profiles']:
                fields = profile_data['fields']
                UserProfile.objects.create(
                    user_id=fields['user'],
                    user_type=fields['user_type']
                )
                self.stdout.write(f'Perfil criado para usuário ID {fields["user"]}')

            # Criar portos
            for porto_data in data['portos']:
                fields = porto_data['fields']
                Porto.objects.create(
                    nome=fields['nome'],
                    doca=fields['porto']
                )
                self.stdout.write(f'Porto {fields["nome"]} criado com sucesso!')

            # Criar postos
            for posto_data in data['postos']:
                fields = posto_data['fields']
                Posto.objects.create(
                    nome=fields['nome'],
                    armario=fields['armario']
                )
                self.stdout.write(f'Posto {fields["nome"]} criado com sucesso!')

            # Criar itens
            for item_data in data['items']:
                fields = item_data['fields']
                Item.objects.create(
                    nome=fields['nome'],
                    descricao=fields['descricao']
                )
                self.stdout.write(f'Item {fields["nome"]} criado com sucesso!')

            # Criar pedidos
            for pedido_data in data['pedidos']:
                fields = pedido_data['fields']
                pedido = Pedido.objects.create(
                    cliente_id=fields['cliente'],
                    entregador_id=fields['entregador'],
                    barqueiro_id=fields['barqueiro'],
                    valor_proposto=fields['valor_proposto'],
                    valor_final=fields['valor_final'],
                    porto_origem_id=fields['porto_origem'],
                    posto_destino_id=fields['posto_destino'],
                    status=fields['status'],
                    created_at=make_aware(datetime.strptime(fields['created_at'], '%Y-%m-%dT%H:%M:%SZ')),
                    updated_at=make_aware(datetime.strptime(fields['updated_at'], '%Y-%m-%dT%H:%M:%SZ'))
                )
                pedido.itens.set(fields['itens'])
                self.stdout.write(f'Pedido {pedido.id} criado com sucesso!')

            self.stdout.write(self.style.SUCCESS('Dados carregados com sucesso!'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'Arquivo não encontrado: {json_file_path}'))
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR('Erro ao decodificar o arquivo JSON'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Erro ao carregar dados: {str(e)}'))