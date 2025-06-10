
# Projeto Erro 200

**Número do Grupo**: 3<br>
**Código da Disciplina**: FGA0208-T01<br>

## Alunos
| Matrícula | Aluno |
| 202402798502 | Breno Chaves da Cunha |
| 202402875361 | Gustavo Leonel Salvador |
| 202402075365 | Guilherme Resende da Rocha |
| 202402697706 | João Gabriel Guedes |
| 202401614513 | Bryan Amorim dos Santos |

## Sobre
O projeto propõe um app de entregas focado nas necessidades dos moradores da Ilha Primeira, onde o transporte é feito principalmente por barcos. A solução garante praticidade, rastreabilidade e segurança nas entregas, com funcionalidades específicas para três tipos de usuários: moradores, entregadores e barqueiros. O desenvolvimento inclui a criação de uma API REST.


## Screenshots
- 3 telas ao mesmo tempo ( Morador, entregador e barqueiro ) :
![image](https://github.com/user-attachments/assets/991cba57-c79d-4b4c-a0d1-95a84230abab)

- Cadastro:
![image](https://github.com/user-attachments/assets/d788f58c-ed85-4a1b-877f-d16732a99299)

- Login:
![image](https://github.com/user-attachments/assets/b59795b5-1310-4235-9a09-4da5f5451940)

- Swagger:
![image](https://github.com/user-attachments/assets/5368306c-9965-4091-9877-e4b0f5f70e5b)

## Vídeo

https://github.com/user-attachments/assets/39d0bdd5-3647-4d57-b43d-0341da1eb5ff


## Instalação
**Linguagens**: Python<br>
**Tecnologias**: Django<br>
**Use o requirements.txt** para o resto das dependências

## Uso
Após a migração, suba o servidor da api e somente depois disso, suba o index.html do front.
Comandos estão todos citados em api_documentation.md


## Link do Canva
(https://www.canva.com/design/DAGkEt2vP9g/dsBjUmVpyzwLrZkqis9htA/edit?utm_content=DAGkEt2vP9g&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
)


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

