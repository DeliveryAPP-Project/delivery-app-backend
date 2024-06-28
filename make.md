# Guia de Comandos Make

Este guia fornece instruções para usar comandos Make para testar, inicializar e gerenciar a API hamper.

## Comandos de Formatação e Teste

Para testar os endpoints da aplicação e formatar o código:

```sh
# Formatar o código de acordo com o ruff e o pylint
$ make format

# Iniciar os testes com pytest
$ make test
```

## Comandos Make e Atalhos na Aplicação

### Informações Gerais

- Todos os comandos devem ser executados na raiz da aplicação.
- Sempre ative o ambiente virtual antes de usar os comandos.

### Definindo o Ambiente e Nome da Aplicação

Antes de inicializar a aplicação, defina o tipo de ambiente e o nome da aplicação (APP_NAME) no terminal. Exemplo:

```sh
export FLASK_APP=project
export FLASK_ENV=development
```

### Inicializar a Aplicação

- **Comando:** `make up`
  - Executa: `python -m project run` para inicializar a aplicação.

## Gerenciamento do Banco de Dados com flask-migrate

### Inicializar o Banco de Dados

1. **Comando:** `make db-init`
   - Executa: `flask db init` (Inicializa a instância SQLAlchemy)

2. **Comando:** `make migrate`
   - Executa: `flask db migrate` (Executa as migrações das tabelas no banco de dados)

3. **Comando:** `make upgrade`
   - Executa: `flask db upgrade` (Cria as tabelas no banco de dados)

## Configuração dos Ambientes (ENV e APP)

### Ambiente Padrão

- **Comando:** `make env-default`
  - Executa:
    ```sh
    export FLASK_APP=project
    export FLASK_ENV=default
    python -m project run
    ```

### Ambiente de Desenvolvimento

- **Comando:** `make env-development`
  - Executa:
    ```sh
    export FLASK_APP=project
    export FLASK_ENV=development
    python -m project run
    ```

### Ambiente de Teste

- **Comando:** `make env-testing`
  - Executa:
    ```sh
    export FLASK_APP=project
    export FLASK_ENV=testing
    python -m project run
    ```

### Ambiente de Produção

- **Comando:** `make env-production`
  - Executa:
    ```sh
    export FLASK_APP=project
    export FLASK_ENV=production
    python -m project run
    ```

- **Comando:** `make up-prod`
  - Executa:
    ```sh
    export FLASK_APP=project
    export FLASK_ENV=production
    gunicorn -w 4 -b 0.0.0.0:5000 "project:create_app()"
    ```

### Ambiente de Homologação

- **Comando:** `make up-homologacao`
  - Executa:
    ```sh
    export FLASK_APP=project
    export FLASK_ENV=homologacao
    python -m project run
    ```