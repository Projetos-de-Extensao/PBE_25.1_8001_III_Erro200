Ao dar clone no repositório, faça:
python manage.py makemigrations
python manage.py migrate
python manage.py load_initial_data
python manage.py createsuperuser
python manage.py runserver

# API Documentation


## Authentication
Most endpoints require authentication using JWT tokens. Include the token in the Authorization header:
```
Authorization: Bearer <token>
```

## Endpoints

### Users

#### List Users
- **URL**: `/api/users/`
- **Method**: GET
- **Auth**: Required
- **Response**: List of user profiles
```json
[
  {
    "id": 1,
    "user": {
      "id": 1,
      "username": "string",
      "email": "string",
      "first_name": "string",
      "last_name": "string"
    },
    "user_type": "MORADOR|ENTREGADOR|BARQUEIRO|ADMIN"
  }
]
```

#### Create User
- **URL**: `/api/users/`
- **Method**: POST
- **Auth**: Not Required
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

#### Get User Pedidos
- **URL**: `/api/users/{id}/pedidos/`
- **Method**: GET
- **Auth**: Required
- **Response**: List of pedidos associated with the user

### Pedidos

#### List Pedidos
- **URL**: `/api/pedidos/`
- **Method**: GET
- **Auth**: Required
- **Response**: List of pedidos filtered by user role
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

#### Create Pedido
- **URL**: `/api/pedidos/`
- **Method**: POST
- **Auth**: Required
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

#### Accept Delivery (Entregador)
- **URL**: `/api/pedidos/{id}/aceitar_entrega/`
- **Method**: POST
- **Auth**: Required (Entregador only)
- **Response**: Updated pedido object

#### Accept Water Transport (Barqueiro)
- **URL**: `/api/pedidos/{id}/aceitar_travessia/`
- **Method**: POST
- **Auth**: Required (Barqueiro only)
- **Response**: Updated pedido object



### Portos

#### List Portos
- **URL**: `/api/portos/`
- **Method**: GET
- **Auth**: Required
- **Response**: List of portos
```json
[
  {
    "id": 1,
    "nome": "string",
    "doca": "string"
  }
]
```

#### Get Porto Pedidos
- **URL**: `/api/portos/{id}/pedidos/`
- **Method**: GET
- **Auth**: Required
- **Response**: List of pedidos at the porto

### Postos

#### List Postos
- **URL**: `/api/postos/`
- **Method**: GET
- **Auth**: Required
- **Response**: List of postos
```json
[
  {
    "id": 1,
    "nome": "string",
    "armario": "string"
  }
]
```

#### Get Posto Pedidos
- **URL**: `/api/postos/{id}/pedidos/`
- **Method**: GET
- **Auth**: Required
- **Response**: List of pedidos at the posto

## Status Codes

- 200: Success
- 201: Created
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 500: Internal Server Error

## Pedido Status Flow

1. `A_CONFIRMAR`: Initial status when pedido is created
2. `ACEITO`: After entregador accepts the delivery
3. `EM_TRANSITO`: When entregador is transporting to porto
4. `NO_PORTO`: When delivered to porto
5. `EM_TRAVESSIA`: When barqueiro is transporting
6. `NO_POSTO`: When delivered to posto
7. `ENTREGUE`: When customer receives
8. `CONCLUIDO`: Final status