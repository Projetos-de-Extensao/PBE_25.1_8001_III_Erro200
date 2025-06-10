# Autenticação

A API utiliza autenticação baseada em JWT (JSON Web Tokens) para proteger os endpoints.

## Como Autenticar

Para acessar endpoints protegidos, é necessário incluir o token JWT no cabeçalho Authorization:

```
Authorization: Bearer <token>
```

## Obtendo um Token

Para obter um token, o usuário deve primeiro se registrar e depois fazer login no sistema.

### Registro de Usuário

POST `/api/users/`

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

### Tipos de Usuário

- **MORADOR**: Cliente que solicita entregas
- **ENTREGADOR**: Responsável pelo transporte até o porto
- **BARQUEIRO**: Responsável pela travessia
- **ADMIN**: Administrador do sistema

## Permissões

- Endpoints públicos: Registro de usuário
- Endpoints protegidos: Todos os outros endpoints requerem autenticação
- Algumas ações requerem tipos específicos de usuário (ex: apenas BARQUEIRO pode marcar uma travessia como concluída)
