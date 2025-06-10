# Visão Geral da API

A API do projeto Erro 200 é um sistema RESTful que gerencia o processo de entrega de pacotes através de portos e postos, envolvendo diferentes tipos de usuários:

## Tipos de Usuários

- **MORADOR**: Usuário que solicita entregas
- **ENTREGADOR**: Responsável por transportar pacotes até o porto
- **BARQUEIRO**: Responsável pela travessia dos pacotes
- **ADMIN**: Administrador do sistema

## Principais Recursos

- Gerenciamento de usuários e autenticação
- Criação e acompanhamento de pedidos
- Gestão de portos e postos de entrega
- Sistema de status para rastreamento de pedidos

## Tecnologias

- Django REST Framework
- JWT para autenticação
- SQLite como banco de dados
