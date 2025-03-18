import os

from project import create_app_wsgi


def test_app_name():
    """Testa se o nome da aplicação 'project.base'"""
    os.environ["FLASK_ENV"] = "testing"
    app = create_app_wsgi()
    assert app.name == "project.base"


def test_route_swagger_status_code_200(app_testing):
    """Testa se o endpoint 'localhost:5000/api/v1/' retorna o status code 200"""
    client = app_testing.test_client()
    response = client.get("http://127.0.0.1:5000/api/v1/")
    assert response.status_code == 200
