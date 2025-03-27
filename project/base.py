"""
Inicialização do app
"""

from dynaconf import FlaskDynaconf
from flask import Flask, request, jsonify
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

    # Configuração do CORS para permitir requisições do frontend
    CORS(
        app,
        resources={
            r"/api/v1/*": {
                "origins": [
                    "hamper.duckdns.org:5173"
                    "https://homologacao.d3izdss14he5ng.amplifyapp.com",
                    "http://localhost:5173",
                    "http://100.26.203.78:5173",
                ],
                "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
                "allow_headers": ["Content-Type", "Authorization"],
            }
        },
        supports_credentials=True,
    )

    # 🔹 Intercepta e responde a requisições OPTIONS antes que o navegador bloqueie
    @app.before_request
    def handle_preflight():
        if request.method == "OPTIONS":
            return "", 200

    # 🔹 Exemplo de rota para testar o CORS
    @app.route("/api/v1/leads", methods=["GET"])
    def get_leads():
        return jsonify({"message": "Sucesso!"})

    print(f"Ambiente atual: {app.config.env}")  # type: ignore
    print(f"Banco de dados atual: {app.config.get('SQLALCHEMY_DATABASE_URI')}")
    print("Aplicação inicializada com sucesso!")

    return app


def create_app_wsgi():
    """
    Método que inicializa o app
    """
    return create_app()


# 🔹 Permite rodar o servidor diretamente
if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
