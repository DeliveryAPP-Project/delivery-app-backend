import pytest


def test_get_order_by_id_return_200(app_testing):
    client = app_testing.test_client()
    response = client.get("/api/v1/orders/1")
    assert response.status_code == 200
    assert response.json["id"] == 1


def test_get_order_by_id_return_404(app_testing):
    client = app_testing.test_client()
    response = client.get("/api/v1/orders/999")
    assert response.status_code == 404
    assert response.json["error"] == "Ordem com ID 999 não encontrado."


def test_update_order_return_200(app_testing):
    client = app_testing.test_client()

    updated_order_data = {
        "products": [1],
        "total_value": 150.0,
        "status": "confirmed",
    }

    response = client.patch("/api/v1/orders/1", json=updated_order_data)
    assert response.status_code == 200
    assert response.json["message"] == "Ordem com ID 1 atualizado com sucesso!"


def test_update_order_return_404(app_testing):
    client = app_testing.test_client()

    updated_order_data = {
        "products": [1],
        "total_value": 150.0,
        "status": "confirmed",
    }

    response = client.patch("/api/v1/orders/999", json=updated_order_data)
    assert response.status_code == 404
    assert response.json["message"] == "NotFoundError: Ordem com ID 999 não encontrado"


def test_delete_order_return_200(app_testing):
    client = app_testing.test_client()
    response = client.delete("/api/v1/orders/1")
    assert response.status_code == 200
    assert response.json["message"] == "Ordem com ID 1 deletado com sucesso."


def test_delete_order_return_404(app_testing):
    client = app_testing.test_client()
    response = client.delete("/api/v1/orders/999")
    assert response.status_code == 404


def test_create_order_return_201(app_testing):
    client = app_testing.test_client()
    new_order_data = {
        "client_id": 1,
        "restaurant_id": 1,
        "products": [1],
    }
    response = client.post("/api/v1/orders/", json=new_order_data)
    assert response.status_code == 201
    assert response.json["message"] == "Pedido com ID 2 criado com sucesso!"


@pytest.mark.skip()
def test_create_order_return_400_missing_data(app_testing):
    client = app_testing.test_client()
    new_order_data = {
        "client_id": 1,
        "restaurant_id": 1,
        # Missing products and total_value
    }
    response = client.post("/api/v1/orders/", json=new_order_data)
    assert response.status_code == 400
    assert response.json["error"] == "Dados do pedido não fornecidos."


@pytest.mark.skip()
def test_create_order_return_404_invalid_client(app_testing):
    client = app_testing.test_client()
    new_order_data = {
        "client_id": 999,  # Invalid client ID
        "restaurant_id": 1,
        "products": [1],
        "total_value": 100.0,
        "status": "pre_order",
    }
    response = client.post("/api/v1/orders/", json=new_order_data)
    assert response.status_code == 404
    assert response.json["error"] == "Cliente com ID 999 não encontrado."


@pytest.mark.skip()
def test_create_order_return_404_invalid_restaurant(app_testing):
    client = app_testing.test_client()
    new_order_data = {
        "client_id": 1,
        "restaurant_id": 999,  # Invalid restaurant ID
        "products": [1],
        "total_value": 100.0,
        "status": "pre_order",
    }
    response = client.post("/api/v1/orders/", json=new_order_data)
    assert response.status_code == 404
    assert response.json["error"] == "Restaurante com ID 999 não encontrado."


@pytest.mark.skip()
def test_create_order_return_404_invalid_product(app_testing):
    client = app_testing.test_client()
    new_order_data = {
        "client_id": 1,
        "restaurant_id": 1,
        "products": [999],  # Invalid product ID
        "total_value": 100.0,
        "status": "pre_order",
    }
    response = client.post("/api/v1/orders/", json=new_order_data)
    assert response.status_code == 404
    assert response.json["error"] == "Produto com ID 999 não encontrado."
