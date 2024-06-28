<h1 align="center">
  <a href="https://hamper.onrender.com/api/v1/">Delivery Back-end API</a>
</h1>

<p align="center">
  <a href="#memo-requisitos">Requisitos</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#rocket-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#information_source-como-usar">Como Usar</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#information_source-como-usar-make">Usar com Make</a>
</p>

## :memo: Requisitos

| Ferramenta                                         | Versão  | Descrição                                   |
| -------------------------------------------------- | ------- | ------------------------------------------- |
| [Python](https://www.python.org/)                  | 3.11.*  | Ambiente de execução Python                 |
| [pip](https://pypi.org/project/pip/)               | ^24.1.1 | Gerenciador de pacotes Python               |
| [Git](https://git-scm.com)                         | -       | Controle de versões                         |
| [PostgreSQL](https://www.postgresql.org/)          | -       | Sistema de gerenciamento de banco de dados  |
| [Docker](https://www.docker.com/)                  | -       | Motor de container                          |
| [Docker-compose](https://docs.docker.com/compose/) | -       | Orquestrador de containers Docker           |

## :rocket: Tecnologias

Este projeto está sendo desenvolvido pela equipe [Hamper](https://hamper.com) com as seguintes tecnologias:

- Linguagem e ambiente: [Python](https://www.python.org/)
- Object-Relational Mapper (ORM): [SQLAlchemy](https://www.sqlalchemy.org/)
- Banco de dados: [PostgreSQL](https://www.postgresql.org/)
- Migrações de banco de dados: [Alembic](https://alembic.sqlalchemy.org/)

## :information_source: Como Usar

```bash
# Clonar este repositório
$ git clone https://github.com/DeliveryAPP-Project/delivery-app-backend.git

# Ir para o diretório do repositório
$ cd delivery-app-backend

# Criar um ambiente virtual
$ python3 -m venv venv

# Ativar o ambiente virtual
$ source venv/bin/activate

# Instalar as dependências
$ pip install -r requirements.txt
```

### Configuração do Projeto

```bash
# Renomear o arquivo de exemplo de variáveis de ambiente
$ cp .secrets-example.toml .secrets.toml

# Definir as variáveis de ambiente para o Flask
$ export FLASK_APP=project
$ export FLASK_ENV=development # ou outro ambiente: testing, production
```

### Configuração do Banco de Dados

```bash
# Iniciar o banco de dados com Docker
$ docker compose up

# Iniciar o banco de dados com Docker Compose em segundo plano
$ docker-compose up -d

# Parar o banco de dados com Docker Compose
$ docker-compose down

# Inicializar o banco de dados
$ flask db init # Executar apenas uma vez para inicializar a conexão
$ flask db migrate # Criar a instância do SQLAlchemy
$ flask db upgrade # Criar as tabelas no banco de dados
```

### Executando o Projeto

```bash
# Inicializar a aplicação
$ python -m project run
```

## :blue_book: Documentação da API

A documentação da API pode ser acessada em [http://127.0.0.1:5000/api/v1](http://127.0.0.1:5000/api/v1), onde a versão do Swagger estará disponível.

<hr />

## Alembic

Para gerenciar models, migrations e seeders, utilize o Alembic:

```bash
# Aplicar a última migração ao banco de dados
$ alembic upgrade head

# Gerar uma nova revisão (com base em modificações ou novos models)
$ alembic revision --autogenerate -m "nome_da_modificacao"
```

Mais comandos úteis podem ser encontrados na [documentação do Alembic](https://alembic.sqlalchemy.org/en/latest/api/commands.html).

## :information_source: Usar com Make

Veja como usar a aplicação através do Make no arquivo [Make.init](make.md).

