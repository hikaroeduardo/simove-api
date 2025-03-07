
![WhatsApp Image 2025-03-07 at 11 34 17](https://github.com/user-attachments/assets/bbc022c6-f3bf-4357-adf0-6425f3fafbf1)

# Simove - Sistema de Gestão de Veículos e Motoristas

## Sobre o Projeto

**Simove** é uma API bem estruturada e documentada, voltada para a gestão de solicitações de veículos e motoristas dentro de uma organização.

## Tecnologias Utilizadas

A aplicação foi desenvolvida utilizando as seguintes tecnologias:

- **Docker** - Para conteinerização e fácil deploy
- **Python** - Linguagem principal do projeto
- **FastAPI** - Framework web assíncrono e performático
- **SQLAlchemy** - ORM para manipulação do banco de dados
- **PyJWT** - Geração e validação de tokens JWT para autenticação
- **bcrypt** - Criptografia segura de senhas

## 📖 Documentação Completa

Todas as rotas da API estão detalhadamente documentadas no **Swagger**, incluindo:
- Status codes
- Exemplos de requisições e respostas

Para acessar a documentação interativa, basta rodar o projeto e acessar:
```
http://127.0.0.1:3333/docs
```

## Como Rodar o Projeto

### Pré-requisitos
Para iniciar, é necessário ter instalado:
- [Docker](https://www.docker.com/)
- [Python](https://www.python.org/downloads/)

### 🏗️ Rodando a aplicação
1. Clone o repositório:
```sh
git clone https://github.com/seu-usuario/simove.git && cd simove
```
2. Crie um ambiente virtual e instale as dependências:
```sh
python -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate
pip install -r requirements.txt
```
3. Inicie o Docker:
```sh
docker-compose up -d
```
4. Gere as migrações:
```sh
alembic revision --autogenerate -m "sua mensagem"
```
```sh
alembic upgrade head
```
5. Inicie a API:
```sh
python src/main.py
```

