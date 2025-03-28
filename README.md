# DeliveryAPP Backend

Este é o backend do projeto DeliveryAPP. Ele é construído usando Flask e fornece uma API RESTful para gerenciar usuários, clientes, estabelecimentos, produtos e pedidos.

## Estrutura do Projeto

TODO: Documentar estrutura de pastas e responsabilidades.

## Configuração

### Requisitos

- Python 3.11
- PostgreSQL
- Redis

### Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seuusuario/delivery-app-backend.git
cd delivery-app-backend
```

2. Crie um ambiente virtual e ative-o:

```bash
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:

```bash
export FLASK_APP=project
export FLASK_ENV=local (local | staging | production)
```

5. Rode a aplicação:

```bash
docker compose up
flask run
```

9. Inicialize o banco de dados:

```bash
flask db init
```

10. Migrações

```bash
# para criar uma nova migração
flask db migrate
# para atualizar o banco para a nova migração
flask db upgrade
```

Popule o banco de dados com dados iniciais:

```bash
python scripts/populate_database.py
```

## Executando a Aplicação

### TL:DR

Para executar a aplicação localmente, use o seguinte comando:

```bash
export FLASK_ENV = local
docker compose up
flask run
```

### Docker

#### Dockerfile

```bash
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --user --no-cache-dir -r requirements.txt

FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /root/.local /root/.local

COPY . .

ENV PATH=/root/.local/bin:$PATH

EXPOSE 5000

CMD ["gunicorn","-w", "4", "-b", "0.0.0.0:5000", "project:create_app()"]

```

#### Docker Compose

1. Arquivo compose com a aplicação, caso FLASK_ENV for "local" você deve subir os serviços com o outro docker-compose.yml listado abaixo

```bash
services:
  backend:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: backend
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=local
      - FLASK_APP=project
    volumes:
      - .:/app
```

2. Compose com a infra, para rodar o ambiente externo localmente, você deve definir as váriaveis de ambiente para local. Para testar com a build que vai para homologação podemos usar em conjunto com o **docker-compose.ext.yml**

```bashs
services:
  postgres:
    image: postgres:14
    container_name: postgres-container
    environment:
      POSTGRES_DB: mydatabase
      POSTGRES_USER: myuser
      POSTGRES_PASSWORD: mypassword1
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

  redis:
    image: redis:latest
    container_name: redis
    ports:
      - "6379:6379"

volumes:
  pgdata:
```

para rodar a aplicação local edite FLASK_ENV para **local** e rode o comando:

```bash
docker compose -f docker-compose.yml -f docker-compose.ext.yml
```

para rodar o ambiente de homologação mude o FLASK_ENV para **staging** e rode:

```bash
docker compose -f docker-compose.ext.yml up
```

Você perceberá que ao tentara executar com FLASK_ENV como **production** você receberá um erro. Isso acontece pois não é possível se conectar ao banco de dados e cache diretamente de uma maquina local. Essa configuração deverá ser usada apenas pelo host da aplicação.

## Ambiente

A aplicação usa Dynaconf para gerenciamento de configuração. A configuração é definida no arquivo `settings.toml`.

### Variáveis de Ambiente

- `FLASK_APP`: O nome da aplicação Flask.
- `FLASK_ENV`: O ambiente em que a aplicação está sendo executada (local | staging | production).

## Contato

Para quaisquer perguntas ou problemas, entre em contato com os mantenedores do projeto.
