"""
Inicialização do app

"""

from dynaconf import FlaskDynaconf
from flask import Flask
from flask_cors import CORS


def create_app(**config):
    """
    Configuração do CORS e carregamento das extensões

    """
    app = Flask(__name__)
    FlaskDynaconf(
        app, envvar_prefix="FLASK", settings_files=["settings.toml", ".secrets.toml"]
    )
    app.config.load_extensions("EXTENSIONS")  # type: ignore
    app.config.update(config)

    CORS(
        app,
        resources={
            "/api/v1/*": {
                "origins": [
                    "https://homologacao.d3izdss14he5ng.amplifyapp.com",
                    "http://localhost:5173",
                    "http://172.24.0.2:5173",
                ]
            }
        },
    )

    print(f"Ambiente atual: {app.config.env}")  # type: ignore
    print(f"Banco de dados atual: {app.config.get('SQLALCHEMY_DATABASE_URI')}")
    print("Aplicação inicializada com sucesso!")

    return app


def create_app_wsgi():
    """
    Método que inicializa o app

    """

    return create_app()
