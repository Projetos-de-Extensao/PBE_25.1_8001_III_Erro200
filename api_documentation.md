Ao dar clone no repositório, faça:
python manage.py makemigrations
python manage.py migrate
python manage.py load_initial_data
python manage.py createsuperuser
python manage.py runserver


# Endpoints Atuais
## Pedidos
- GET /api/pedidos/ - Lista todos os pedidos
- POST /api/pedidos/ - Cria novo pedido
- GET /api/pedidos/{id}/ - Obtém pedido específico
- PUT /api/pedidos/{id}/ - Atualiza pedido
- DELETE /api/pedidos/{id}/ - Remove pedido
- GET /api/pedidos/{id}/itens/ - Lista itens de um pedido
## Itens
- GET /api/itens/ - Lista todos os itens
- POST /api/itens/ - Cria novo item
- GET /api/itens/{id}/ - Obtém item específico
- PUT /api/itens/{id}/ - Atualiza item
- DELETE /api/itens/{id}/ - Remove item
- GET /api/itens/{id}/pedidos/ - Lista pedidos com este item
## Usuários
- GET /api/users/ - Lista todos os usuários
- POST /api/users/ - Cria novo usuário
- GET /api/users/{id}/ - Obtém usuário específico
- PUT /api/users/{id}/ - Atualiza usuário
- DELETE /api/users/{id}/ - Remove usuário
- GET /api/users/{id}/pedidos/ - Lista pedidos do usuário

## Status Codes
- 200: Sucesso
- 400: Erro na requisição
- 401: Não autorizado
- 404: Não encontrado
