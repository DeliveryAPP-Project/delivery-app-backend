"""
Inicialização do app

"""

from dynaconf import FlaskDynaconf
from flask import Flask
from flask_cors import CORS



def create_app(**config) -> Flask:
    """
    Configuração do CORS e carregamento das extensões

    """
    app = Flask(__name__)
    FlaskDynaconf(app, envvar_prefix="FLASK", settings_files=["settings.toml"])
    # pylint: disable=E1101
    app.config.load_extensions("EXTENSIONS")
    app.config.update(config)
    CORS(app)

    print(f"Ambiente atual: {app.config.env}")
    print(f"Banco de dados atual: {app.config.get('SQLALCHEMY_DATABASE_URI')}")
    print("Aplicação inicializada com sucesso!")

    return app


def create_app_wsgi() -> create_app:
    """
    Método que inicializa o app

    """

    return create_app()
