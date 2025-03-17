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
    assert response.json["message"] == "NotFoundError: Ordem com ID 999 não encontrado"
