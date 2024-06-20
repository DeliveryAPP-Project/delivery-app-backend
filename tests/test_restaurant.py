def test_list_restaurant_return_200(app_testing, restaurant_10):
    """
    Teste para verificar se o endpoint da API para listar restaurante retorna o código de status 200.
    """
    restaurant = app_testing.test_client()
    response = restaurant.get("http://127.0.0.1:5000/api/v1/restaurants/")
    print(response.json)
    assert response.status_code == 200
    for restaurant in response.json:
        assert "name" in restaurant
        assert "description" in restaurant


def test_post_restaurant_return_200(app_testing):
    """
    Testa se a rota '/api/v1/restaurants/' retorna o código de status 201 (Created) ao fazer uma requisição POST com dados válidos de products.
    """
    client = app_testing.test_client()

    restaurant_data = {
        "name": "Restaurante Teste",
        "description": "Descrição do restaurante de teste",
        "classification": 4.5,
        "location": "Cidade do Teste",
        "url_image_logo": "url_logo_teste",
        "url_image_banner": "url_banner_teste",
    }

    response = client.post("/api/v1/restaurants/", json=restaurant_data)

    assert response.status_code == 201
    assert response.json["message"] == "Restaurante cadastrado com sucesso!"


def test_post_restaurant_return_400(app_testing):
    """
    Testa se a rota '/api/v1/restaurants/' retorna o código de status 400 (Solicitação Incorreta) ao fazer uma requisição POST com dados invalidos de products.
    """
    client = app_testing.test_client()

    response = client.post("/api/v1/restaurants/", json={"invalid": "data"})

    assert response.status_code == 400
    assert (
        response.json["error"]
        == "'invalid' is an invalid keyword argument for Restaurant"
    )


def test_get_one_restaurant_return_200(app_testing, restaurant):
    """
    Testa se a rota '/api/v1/restaurants/<int:id>/' retorna o código de status 200 ao fazer uma requisição GET com um ID de restaurante válido.
    """
    client = app_testing.test_client()

    response = client.get("/api/v1/restaurants/1/products")
    assert response.status_code == 200
    assert response.json["id"] == 1
    assert "name" in response.json
    assert "description" in response.json


def test_get_one_restaurant_return_404(app_testing):
    """
    Testa se a rota '/api/v1/restaurants/<int:id>/' retorna o código de status 404 ao fazer uma requisição GET com um ID de restaurante invalido.
    """
    client = app_testing.test_client()
    response = client.get("/api/v1/restaurants/0/products")
    assert response.status_code == 404
    assert response.json["error"] == "Restaurante com ID 0 não encontrado."


def test_patch_restaurant_return_200(app_testing, restaurant):
    """
    Testa se a rota '/api/v1/restaurants/{restaurant.id}/products' retorna o código de status 200 ao fazer uma requisição PATCH com um ID de restaurante válido.
    """
    client = app_testing.test_client()

    restaurant_data = {
        "name": "Restaurante Teste",
        "description": "Descrição do restaurante de teste",
        "classification": 4.5,
        "location": "Cidade do Teste",
        "url_image_logo": "url_logo_teste",
        "url_image_banner": "url_banner_teste",
        "products": [
            {
                "id": 1,
                "name": "Produto Teste",
                "value": 10.5,
                "description": "Descrição do produto de teste",
                "url_image": "url_produto_teste",
                "restaurant_id": restaurant.id,
            }
        ],
    }

    response = client.patch(
        f"/api/v1/restaurants/{restaurant.id}/products", json=restaurant_data
    )
    assert response.status_code == 200
    assert (
        response.json["message"]
        == f"Restaurante com ID {restaurant.id} atualizado com sucesso!"
    )


def test_patch_restaurant_return_404(app_testing):
    """
    Testa se a rota '/api/v1/restaurants/<int:id>/' retorna o código de status 500 ao fazer uma requisição PATCH com um ID de restaurante invalido.
    """
    client = app_testing.test_client()
    response = client.patch("/api/v1/restaurants/0/products", json={})
    print(response.json)
    assert response.status_code == 404


def test_delete_restaurant_return_200(app_testing, restaurant):
    """
    Testa se a rota '/api/v1/restaurants/<int:id>/' retorna o código de status 200 ao fazer uma requisição DELETE com um ID de restaurante válido.
    """
    client = app_testing.test_client()
    response = client.delete("/api/v1/restaurants/1/products")
    assert response.status_code == 200
    print(response.json)
    assert response.json["message"] == "Restaurante com ID 1 deletado com sucesso."


def test_delete_restaurant_return_404(app_testing):
    """
    Testa se a rota '/api/v1/restaurants/<int:id>/' retorna o código de status 404 ao fazer uma requisição DELETE com um ID de restaurante invalido.
    """
    client = app_testing.test_client()
    response = client.delete("/api/v1/restaurants/0/products")
    assert response.status_code == 404
    print(response.json)
    assert response.json["error"] == "Restaurante com ID 0 não encontrado"
