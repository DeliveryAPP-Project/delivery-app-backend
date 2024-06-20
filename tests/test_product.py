def test_list_product_return_200(app_testing, restaurant_10, product_10):
    """
    Teste para verificar se o endpoint da API para listar produtos e retorna o código de status 200.
    """
    product = app_testing.test_client()
    response = product.get("http://127.0.0.1:5000/api/v1/products/")
    assert response.status_code == 200
    for product in response.json:
        assert "name" in product
        assert "Description" in product["description"]


def test_post_product_return_200(app_testing, restaurant_10):
    """
    Testa se a rota '/api/v1/products/' retorna o código de status 201 (Created) ao fazer uma requisição POST com dados válidos de products.
    """
    client = app_testing.test_client()

    product_data = {
        "name": "X-Teste",
        "value": 15,
        "description": "Descrição do produto de teste",
        "url_image": "url_image_teste",
        "restaurant_id": 5,
    }

    response = client.post("/api/v1/products/", json=product_data)

    assert response.status_code == 201
    assert response.json["message"] == "Produto cadastrado com sucesso!"


def test_post_product_return_400(app_testing):
    """
    Testa se a rota '/api/v1/products/' retorna o código de status 400 (Solicitação Incorreta) ao fazer uma requisição POST com dados invalidos de products.
    """
    client = app_testing.test_client()

    response = client.post("/api/v1/products/", json={"invalid": "data"})

    assert response.status_code == 400
    assert (
        response.json["error"] == "'invalid' is an invalid keyword argument for Product"
    )


def test_get_one_product_return_200(app_testing, restaurant, product):
    """
    Testa se a rota '/api/v1/products/<int:id>/' retorna o código de status 200 ao fazer uma requisição GET com um ID de products válido.
    """
    client = app_testing.test_client()

    response = client.get("/api/v1/products/1")
    assert response.status_code == 200
    assert response.json["name"] == "X-Bacon"
    assert response.json["value"] == 20


def test_get_one_product_return_404(app_testing):
    """
    Testa se a rota '/api/v1/products/<int:id>/' retorna o código de status 404 ao fazer uma requisição GET com um ID de products invalido.
    """
    client = app_testing.test_client()
    response = client.get("/api/v1/products/0")
    assert response.status_code == 404


def test_patch_product_return_200(app_testing, restaurant, product):
    """
    Testa se a rota '/api/v1/products/<int:id>/' retorna o código de status 200 ao fazer uma requisição PATCH com um ID de products válido.
    """
    client = app_testing.test_client()

    product_data = {
        "name": "X-Teste",
        "value": 15,
        "description": "Descrição do produto de teste",
        "url_image": "url_image_teste",
        "restaurant_id": 1,
    }

    response = client.patch("/api/v1/products/1", json=product_data)
    assert response.status_code == 200
    assert response.json["message"] == "Produto com ID 1 atualizado com sucesso!"


def test_patch_product_return_404(app_testing):
    """
    Testa se a rota '/api/v1/products/<int:id>/' retorna o código de status 404 ao fazer uma requisição PATCH com um ID de products invalido.
    """
    client = app_testing.test_client()

    product_data = {
        "name": "X-Teste",
        "value": 15,
        "description": "Descrição do produto de teste",
        "url_image": "url_image_teste",
        "restaurant_id": 5,
    }

    response = client.patch("/api/v1/products/0", json=product_data)
    assert response.status_code == 404
    assert response.json["error"] == "Produto com ID 0 não encontrado"


def test_delete_product_return_200(app_testing, restaurant, product):
    """
    Testa se a rota '/api/v1/products/<int:id>/' retorna o código de status 200 ao fazer uma requisição DELETE com um ID de products válido.
    """
    client = app_testing.test_client()
    response = client.delete("/api/v1/products/1")
    assert response.status_code == 200
    assert response.json["message"] == "Produto com ID 1 deletado com sucesso."


def test_delete_product_return_404(app_testing):
    """
    Testa se a rota '/api/v1/products/<int:id>/' retorna o código de status 404 ao fazer uma requisição DELETE com um ID de products invalido.
    """
    client = app_testing.test_client()
    response = client.delete("/api/v1/products/0")
    assert response.status_code == 404
    assert response.json["error"] == "Produto com ID 0 não encontrado"
