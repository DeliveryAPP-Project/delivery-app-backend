def test_get_payment_by_id_return_200(app_testing):
    client = app_testing.test_client()
    response = client.get("/api/v1/payments/1")
    assert response.status_code == 200
    assert response.json["id"] == 1


def test_get_payment_by_id_return_404(app_testing):
    client = app_testing.test_client()
    response = client.get("/api/v1/payments/999")
    assert response.status_code == 404
    assert response.json["message"] == "Pagamento com ID 999 não encontrado."


def test_update_payment_return_200(app_testing):
    client = app_testing.test_client()

    updated_payment_data = {
        "status": "approved",
    }

    response = client.patch("/api/v1/payments/1", json=updated_payment_data)
    assert response.status_code == 200
    assert response.json["message"] == "Pagamento com ID 1 atualizado com sucesso"


def test_update_payment_return_404(app_testing):
    client = app_testing.test_client()

    updated_payment_data = {
        "status": "approved",
    }

    response = client.patch("/api/v1/payments/999", json=updated_payment_data)
    assert response.status_code == 404
    assert response.json["message"] == "Pagamento com ID 999 não encontrado"


def test_create_payment_dinheiro_return_201(app_testing):
    client = app_testing.test_client()
    new_payment_data = {
        "order_id": 1,
        "payment_type": "Dinheiro",
    }
    response = client.post("/api/v1/payments/", json=new_payment_data)
    assert response.status_code == 201
    assert response.json["message"] == "Pagamento com ID 2 cadastrado com sucesso!"


def test_create_payment_return_400_missing_data(app_testing):
    client = app_testing.test_client()
    new_payment_data = {
        "order_id": 1,
        # Missing payment_type
    }

    response = client.post("/api/v1/payments/", json=new_payment_data)

    assert response.status_code == 400
    assert response.json["message"] == "Missing required field: payment_type"


def test_create_payment_return_404_invalid_order(app_testing):
    client = app_testing.test_client()
    new_payment_data = {
        "order_id": 999,  # Invalid order ID
        "payment_type": "Pix",
    }
    response = client.post("/api/v1/payments/", json=new_payment_data)
    assert response.status_code == 404
    assert response.json["message"] == "Pedido com o ID 999"


def test_get_all_payments_return_200(app_testing):
    client = app_testing.test_client()
    response = client.get("/api/v1/payments/")
    assert response.status_code == 200
    assert isinstance(response.json, list)
