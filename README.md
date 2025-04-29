# DeliveryAPP Backend

Este é o backend do projeto DeliveryAPP. Ele é construído usando Flask e fornece uma API RESTful para gerenciar usuários, clientes, estabelecimentos, produtos e pedidos.

## Estrutura do Projeto

TODO: Documentar estrutura de pastas e responsabilidades.

## Requisitos

- Python 3.11
- PostgreSQL
- Redis

## Clone o repositório

```bash=
git clone https://github.com/seuusuario/delivery-app-backend.git
cd delivery-app-backend
```

## Rodando Local

> A aplicação não está rodando na branch main e sim em homologação, não esqueça de fazer:
> `git checkout homologacao`

1. Crie um ambiente virtual e ative-o:

```bash=
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
```

2. Instale as dependências:

```bash=
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente:

```bash=
export FLASK_APP=project
export FLASK_ENV=local (local | staging | production)
```

4. Rode a aplicação:

```bash=
docker compose up # Sobe apenas o banco de dados e redis.
flask run # Roda a aplicação em modo desenvolvimento.
```

## Rodando com Docker

Existem dois arquivos docker-compose no projeto. O docker-compose.yml roda apenas a infra e o docker-compose.backend.yml que sobe o backend.

Isso é util para subir a aplicação em modo produção antes de enviar para homologação.

Você pode rodar multiplos arquivos compose adicionando a tag -f.

```bash=
docker-compose -f docker-compose.yml -f docker-compose.backend.yml down
```

## Banco de dados e Migrações

```bash=
# Inicia a conexão com o banco de dados.
flask db init

# Para criar uma nova migração
flask db migrate -m "Pequena descrição sobre o que a nova migração faz"

# Para atualizar o banco para a nova migração
flask db upgrade
```

Popule o banco de dados com dados iniciais:

```bash
python scripts/populate_database.py
```

## Ambiente

A aplicação usa Dynaconf para gerenciamento de configuração. A configuração é definida no arquivo `settings.toml` e `.secrets.toml`.

### Variáveis de Ambiente

- `FLASK_APP`: O nome da aplicação Flask.
- `FLASK_ENV`: O ambiente em que a aplicação está sendo executada (local | staging | production).

## Documentação da API

TODO

## Testes

TODO

## Contato

Para quaisquer perguntas ou problemas, entre em contato com os mantenedores do projeto.
