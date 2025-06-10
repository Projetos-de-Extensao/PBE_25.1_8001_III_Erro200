
# Projeto Erro 200

**Número do Grupo**: 3<br>
**Código da Disciplina**: FGA0208-T01<br>

## Alunos

| Matrícula       | Nome |            |
|------------|-------|--------------|
| 202402798502      | Breno Chaves da Cunha
| 202402875361      | Gustavo Leonel Salvador
| 202402075365      | Guilherme Resende da Rocha
| 202402697706      | João Gabriel Guedes
| 202401614513      | Bryan Amorim dos Santos

## Sobre o Projeto

O Projeto Erro 200 é uma aplicação web desenvolvida para gerenciar o processo de entrega de mercadorias na Ilha Primeira, conectando moradores, entregadores e barqueiros em um sistema integrado. O projeto aborda a necessidade específica de gerenciar entregas em um local onde o transporte é feito principalmente por barcos.

### Principais Funcionalidades

- Gerenciamento de pedidos de entrega
- Sistema de rastreamento por status
- Integração entre diferentes tipos de usuários (moradores, entregadores e barqueiros)
- Gestão de portos e postos de entrega
- API REST completa para todas as operações

## Estrutura da Documentação

 **Aplicativo de Entregas para Ilha Primeira**
 O projeto propõe um app de entregas focado nas necessidades dos moradores da Ilha Primeira, onde o transporte é feito principalmente por barcos. A solução garante praticidade, rastreabilidade e segurança nas entregas, com funcionalidades específicas para três tipos de usuários: moradores, entregadores e barqueiros. O desenvolvimento inclui a criação de uma API REST.

## Tecnologias Utilizadas

- **Backend**:
  - Django REST Framework para a API
  - SQLite como banco de dados
  - JWT para autenticação
  
- **Frontend**:
  - HTML5, CSS3 e JavaScript
  - Interface responsiva e moderna
  
- **Documentação**:
  - MkDocs com Material Theme
  - Diagramas UML
  - Protótipos de interface

## Instalação e Uso

Para iniciar o projeto localmente:

```bash
# Clone o repositório
git clone [URL_DO_REPOSITORIO]

# Crie e ative um ambiente virtual
python -m venv env
source env/bin/activate  # Linux/macOS
# ou
env\Scripts\activate  # Windows

# Instale as dependências
pip install -r requirements.txt

# Aplique as migrações
python manage.py migrate

# Carregue os dados iniciais
python manage.py load_initial_data

# Inicie o servidor
python manage.py runserver
```

## Estrutura do Projeto

1. **Frontend** (`/Front`)
   - Interface web responsiva
   - Autenticação de usuários
   - Painéis específicos para cada tipo de usuário

2. **Backend** (`/myapp`)
   - API REST completa
   - Modelos de dados
   - Autenticação e autorização
   - Gerenciamento de pedidos

3. **Documentação** (`/docs`)
   - Documentação técnica
   - Guias de usuário
   - Documentação da API


# Como Baixar e Configurar a Aplicação

## Pré-requisitos
Antes de iniciar, certifique-se de ter os seguintes softwares instalados:

- [Python](https://www.python.org/downloads/) (versão mais recente recomendada)
- [Django](https://www.djangoproject.com/)

## Passos para Configuração

1. **Baixar e instalar o Python**
   - Acesse o site oficial do [Python](https://www.python.org/downloads/).
   - Baixe e instale a versão mais recente.
   - Durante a instalação, marque a opção **"Add Python to PATH"**.
   - Para verificar se a instalação foi concluída, abra o terminal e digite:
     ```sh
     python --version
     ```

2. **Criar um ambiente virtual**
   - No diretório do código, abra o terminal e execute:
     ```sh
     python -m venv env
     ```
   - Ative o ambiente virtual:
     - No Windows:
       ```sh
       env\Scripts\activate
       ```
     - No macOS/Linux:
       ```sh
       source env/bin/activate
       ```

3. **Instalar o Django**
   - Com o ambiente virtual ativado, instale o Django com:
     ```sh
     pip install django
     ```
   - Para verificar a instalação, execute:
     ```sh
     django-admin --version
     ```

4. **Instalar o MkDocs**
   - Ainda com o ambiente virtual ativado, instale o MkDocs:
     ```sh
     pip install mkdocs
     ```
   - Para testar a instalação, execute:
     ```sh
     mkdocs --version
     ```

Agora sua aplicação está pronta para ser configurada e executada!

