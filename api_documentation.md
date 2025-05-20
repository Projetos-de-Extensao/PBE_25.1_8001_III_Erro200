Ao dar clone no repositório, faça:
python manage.py makemigrations
python manage.py migrate
python manage.py load_inicial_data
python manage.py runserver

# API de Pedidos

## Autenticação
```http
Authorization: Token <seu-token>
```

## Endpoints

### Pedidos

**Listar Pedidos**
```http
GET /api/pedidos/
```

**Criar Pedido**
```http
POST /api/pedidos/
{
  "cliente": 1,
  "itens": [1, 2],
  "valor_total": "100.00"
}
```

**Obter Pedido por ID**
```http
GET /api/pedidos/{id}/
```

**Atualizar Pedido**
```http
PUT /api/pedidos/{id}/
{
  "cliente": 1,
  "itens": [1, 2],
  "valor_total": "150.00"
}
```

**Deletar Pedido**
```http
DELETE /api/pedidos/{id}/
```

### Itens

**Listar Itens**
```http
GET /api/items/
```

**Criar Item**
```http
POST /api/items/
{
  "nome": "Nome do Item",
  "descricao": "Descrição do Item"
}
```

**Obter Item por ID**
```http
GET /api/items/{id}/
```

**Atualizar Item**
```http
PUT /api/items/{id}/
{
  "nome": "Nome Atualizado",
  "descricao": "Descrição Atualizada"
}
```

**Deletar Item**
```http
DELETE /api/items/{id}/
```

## Status Codes
- 200: Sucesso
- 400: Erro na requisição
- 401: Não autorizado
- 404: Não encontrado
