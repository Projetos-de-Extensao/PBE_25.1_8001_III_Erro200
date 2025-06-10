# Endpoints da API

## Usuários

### Listar Usuários
- **URL**: `/api/users/`
- **Método**: GET
- **Auth**: Requerida
- **Resposta**: Lista de perfis de usuário

### Criar Usuário
- **URL**: `/api/users/`
- **Método**: POST
- **Auth**: Não Requerida
- **Body**:
```json
{
  "user": {
    "username": "string",
    "password": "string",
    "email": "string",
    "first_name": "string",
    "last_name": "string"
  },
  "user_type": "MORADOR|ENTREGADOR|BARQUEIRO|ADMIN"
}
```

## Pedidos

### Listar Pedidos
- **URL**: `/api/pedidos/`
- **Método**: GET
- **Auth**: Requerida
- **Resposta**: Lista de pedidos filtrada por papel do usuário
```json
[
  {
    "id": 1,
    "cliente": 1,
    "cliente_nome": "string",
    "entregador": 2,
    "entregador_nome": "string",
    "barqueiro": 3,
    "barqueiro_nome": "string",
    "descricao": "string",
    "valor_proposto": "100.00",
    "valor_final": "100.00",
    "porto_origem": 1,
    "porto_nome": "string",
    "posto_destino": 1,
    "posto_nome": "string",
    "status": "A_CONFIRMAR",
    "created_at": "2024-03-21T10:00:00Z",
    "updated_at": "2024-03-21T10:00:00Z"
  }
]
```

### Criar Pedido
- **URL**: `/api/pedidos/`
- **Método**: POST
- **Auth**: Requerida
- **Body**:
```json
{
  "cliente": 1,
  "descricao": "string",
  "valor_proposto": "100.00",
  "porto_origem": 1,
  "posto_destino": 1
}
```

### Ações em Pedidos

#### Aceitar Entrega (Entregador)
- **URL**: `/api/pedidos/{id}/aceitar_entrega/`
- **Método**: POST
- **Auth**: Requerida (apenas Entregador)

#### Iniciar Transporte (Entregador)
- **URL**: `/api/pedidos/{id}/iniciar_transporte/`
- **Método**: POST
- **Auth**: Requerida (apenas Entregador)

#### Entregar no Porto (Entregador)
- **URL**: `/api/pedidos/{id}/entregar_no_porto/`
- **Método**: POST
- **Auth**: Requerida (apenas Entregador)

#### Aceitar Travessia (Barqueiro)
- **URL**: `/api/pedidos/{id}/aceitar_travessia/`
- **Método**: POST
- **Auth**: Requerida (apenas Barqueiro)

#### Marcar Entregue (Barqueiro)
- **URL**: `/api/pedidos/{id}/marcar_entregue/`
- **Método**: POST
- **Auth**: Requerida (apenas Barqueiro)

#### Marcar Concluído (Morador)
- **URL**: `/api/pedidos/{id}/marcar_concluido/`
- **Método**: POST
- **Auth**: Requerida (apenas Morador)

## Portos

### Listar Portos
- **URL**: `/api/portos/`
- **Método**: GET
- **Auth**: Requerida
- **Resposta**:
```json
[
  {
    "id": 1,
    "nome": "string",
    "doca": "string"
  }
]
```

### Pedidos no Porto
- **URL**: `/api/portos/{id}/pedidos/`
- **Método**: GET
- **Auth**: Requerida

## Postos

### Listar Postos
- **URL**: `/api/postos/`
- **Método**: GET
- **Auth**: Requerida
- **Resposta**:
```json
[
  {
    "id": 1,
    "nome": "string",
    "armario": "string"
  }
]
```

### Pedidos no Posto
- **URL**: `/api/postos/{id}/pedidos/`
- **Método**: GET
- **Auth**: Requerida
