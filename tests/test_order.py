def test_list_order_return_200(
    app_testing, client_10, restaurant_10, product_10, order_10
):
    order = app_testing.test_client()
    response = order.get("http://127.0.0.1:5000/api/v1/orders/")
    assert response.status_code == 200
    for order in response.json:
        assert "client" in order
        assert "restaurant" in order
        assert "products" in order
        assert "created_at" in order


def test_post_order_return_200(app_testing, client_10, restaurant_10, product_10):
    client = app_testing.test_client()

    order_data = {
        "client_id": 4,
        "restaurant_id": 5,
        "products": [{"product_id": 5, "quantity": 1}],
        "created_at": "2024-03-11 10:00:00",
    }

    response = client.post("/api/v1/orders/", json=order_data)

    assert response.status_code == 201
    assert response.json["message"] == "Pedido criado com sucesso!"


def test_post_order_return_400(app_testing, restaurant_10, product_10):
    client = app_testing.test_client()

    order_data = {
        "client_id": 4,
        "restaurant_id": 5,
        "products": [5],
        "created_at": "2024-03-11 10:00:00",
    }

    response = client.post("/api/v1/orders/", json=order_data)

    assert response.status_code == 400
    assert response.json["error"] == "404 Not Found: Cliente com ID 4 não encontrado."


def test_get_one_order_return_200(app_testing, cliente, restaurant, product, order):
    client = app_testing.test_client()

    response = client.get("/api/v1/orders/1")
    assert response.status_code == 200
    assert response.json["client"] == 1
    assert response.json["restaurant"] == 1


def test_get_one_order_return_404(app_testing):
    client = app_testing.test_client()
    response = client.get("/api/v1/orders/0")
    assert response.status_code == 404
    assert response.json["error"] == "Ordem com ID 0 não encontrado."


def test_patch_order_return_200(app_testing, cliente, restaurant, product, order):
    client = app_testing.test_client()

    order_data = {
        "client_id": 1,
        "restaurant_id": 1,
        "products": [1],
    }

    response = client.patch("/api/v1/orders/1", json=order_data)
    assert response.status_code == 200
    assert response.json["message"] == "Ordem com ID 1 atualizado com sucesso!"


def test_patch_order_return_404(app_testing):
    client = app_testing.test_client()

    order_data = {
        "client_id": 1,
        "restaurant_id": 1,
        "products": [1],
    }
    response = client.patch("/api/v1/orders/0", json=order_data)
    assert response.status_code == 404
    assert response.json["error"] == "Ordem com ID 0 não encontrado."


def test_delete_order_return_200(app_testing, cliente, restaurant, product, order):
    client = app_testing.test_client()

    response = client.delete("/api/v1/orders/1")
    assert response.status_code == 200
    assert response.json["message"] == "Ordem com ID 1 deletado com sucesso."


def test_delete_order_return_404(app_testing):
    client = app_testing.test_client()

    response = client.delete("/api/v1/orders/0")
    assert response.status_code == 404
    assert response.json["error"] == "Ordem com ID 0 não encontrado"
