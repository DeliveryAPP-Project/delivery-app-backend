def test_list_user_return_200(app_testing, User_10):
    """
    Testa se a rota '/api/v1/users/' retorna o código de status 200 e os dados contidos em mock_users.
    """
    user = app_testing.test_client()
    response = user.get("http://127.0.0.1:5000/api/v1/users/")
    assert response.status_code == 200
    for user in response.json:
        assert "firstname" in user
        assert "Firstname" in user["firstname"]


def test_post_user_return_200(app_testing):
    """
    Testa se a rota '/api/v1/clients/' retorna o código de status 201 (Created) ao fazer uma requisição POST com dados válidos de Usuário.
    """
    client = app_testing.test_client()

    user_data = {
        "firstname": "João",
        "lastname": "Silva",
        "email": "joao.silva@example.com",
    }

    response = client.post("/api/v1/users/", json=user_data)

    assert response.status_code == 201
    assert response.json["message"] == "Usuário cadastrado com sucesso!"


def test_post_user_return_400(app_testing):
    """
    Testa se a rota '/api/v1/users/' retorna o código de status 400 (Solicitação Incorreta) ao fazer uma requisição POST com dados invalidos de usuario.
    """
    client = app_testing.test_client()

    response = client.post("/api/v1/users/", json={"invalid": "data"})

    assert response.status_code == 400
    assert response.json["error"] == "'invalid' is an invalid keyword argument for User"


def test_get_one_user_return_200(app_testing, user):
    """
    Testa se a rota '/api/v1/users/<int:id>/' retorna o código de status 200 ao fazer uma requisição GET com um ID de Usuário válido.
    """
    client = app_testing.test_client()
    response = client.get("/api/v1/users/1")
    assert response.status_code == 200
    assert response.json["firstname"] == "Tony"


def test_get_one_user_return_404(app_testing):
    """
    Testa se a rota '/api/v1/users/<int:id>/' retorna o código de status 404 ao fazer uma requisição GET com um ID de Usuário invalido.
    """
    client = app_testing.test_client()
    response = client.get("/api/v1/users/1")
    assert response.status_code == 404
    assert response.json["error"] == "Usuário com ID 1 não encontrado."


def test_patch_users_return_200(app_testing, user):
    """
    Testa se a rota '/api/v1/clients/<int:id>/' retorna o código de status 200 ao fazer uma requisição PATCH com um ID de Usuario válido.
    """
    client = app_testing.test_client()

    user_data = {
        "firstname": "João",
        "lastname": "Silva",
        "email": "joao.silva@example.com",
    }

    response = client.patch("/api/v1/users/1", json=user_data)

    assert response.status_code == 200
    assert response.json["message"] == "Usuário com ID 1 atualizado com sucesso!"


def test_patch_users_return_500(app_testing):
    """
    Testa se a rota '/api/v1/users/<int:id>/' retorna o código de status 500 ao fazer uma requisição PATCH com um ID de Usuario invalido.
    """
    client = app_testing.test_client()
    response = client.patch("/api/v1/users/1", json={})
    assert response.status_code == 500


def test_delete_client_return_200(app_testing, user):
    """
    Testa se a rota '/api/v1/users/<int:id>/' retorna o código de status 200 ao fazer uma requisição DELETE com um ID de cliente válido.
    """
    client = app_testing.test_client()
    response = client.delete("/api/v1/users/1")
    assert response.status_code == 200
    assert response.json["message"] == "Usuário com ID 1 deletado com sucesso."


def test_delete_client_return_404(app_testing):
    """
    Testa se a rota '/api/v1/users/<int:id>/' retorna o código de status 404 ao fazer uma requisição DELETE com um ID de cliente invalido.
    """
    client = app_testing.test_client()
    response = client.delete("/api/v1/users/1")
    assert response.status_code == 404
    assert response.json["error"] == "Usuário com ID 1 não encontrado"
