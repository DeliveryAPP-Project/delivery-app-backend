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
        "establishment_id": 1,
        "products": [1],
    }
    response = client.post("/api/v1/orders/", json=new_order_data)
    assert response.status_code == 201
    assert response.json["message"] == "Pedido com ID 3 criado com sucesso!"


def test_create_order_return_400_missing_data(app_testing):
    client = app_testing.test_client()
    new_order_data = {
        "client_id": 1,
        "establishment_id": 1,
        # Missing products and total_value
    }

    response = client.post("/api/v1/orders/", json=new_order_data)

    assert response.status_code == 400
    assert response.json["message"] == "Validation Error: Missing 'products'"


def test_create_order_return_404_invalid_client(app_testing):
    client = app_testing.test_client()
    new_order_data = {
        "client_id": 999,  # Invalid client ID
        "establishment_id": 1,
        "products": [1],
        "total_value": 100.0,
        "status": "pre_order",
    }
    response = client.post("/api/v1/orders/", json=new_order_data)
    assert response.status_code == 404
    assert response.json["message"] == "Cliente com ID 999 não encontrado."


def test_create_order_return_404_invalid_establishment(app_testing):
    client = app_testing.test_client()
    new_order_data = {
        "client_id": 1,
        "establishment_id": 999,  # Invalid establishment ID
        "products": [1],
        "total_value": 100.0,
        "status": "pre_order",
    }
    response = client.post("/api/v1/orders/", json=new_order_data)
    assert response.status_code == 404
    assert response.json["message"] == "Estabelecimento com ID 999 não encontrado."


def test_create_order_return_404_invalid_product(app_testing):
    client = app_testing.test_client()
    new_order_data = {
        "client_id": 1,
        "establishment_id": 1,
        "products": [999],  # Invalid product ID
        "total_value": 100.0,
        "status": "pre_order",
    }
    response = client.post("/api/v1/orders/", json=new_order_data)
    assert response.status_code == 404
    assert response.json["message"] == "Produto com ID 999 não encontrado."
