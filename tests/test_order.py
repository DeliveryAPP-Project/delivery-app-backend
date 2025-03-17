def test_list_order_return_200(app_testing):
    order = app_testing.test_client()
    response = order.get("http://127.0.0.1:5000/api/v1/orders/")
    assert response.status_code == 200


def test_post_order_return_200(app_testing):
    client = app_testing.test_client()

    order_data = {
        "client_id": 1,
        "restaurant_id": 1,
        "products": [1],
        "total_value": 100.0,
        "status": "pre_order",
    }

    response = client.post("/api/v1/orders/", json=order_data)

    assert response.status_code == 201
