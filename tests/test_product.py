def test_list_product_return_200(app_testing):
    product = app_testing.test_client()
    response = product.get("http://127.0.0.1:5000/api/v1/products/")
    assert response.status_code == 200


def test_post_product_return_200(app_testing):
    client = app_testing.test_client()

    product_data = {
        "name": "X-Teste",
        "value": 15.0,
        "description": "Descrição do produto de teste",
        "url_image": "url_image_teste",
        "food_type": "Brasileira",
        "has_gluten": False,
        "has_lactose": False,
        "is_vegan": False,
        "is_vegetarian": False,
        "restaurant_id": 1,
    }

    response = client.post("/api/v1/products/", json=product_data)
    assert response.status_code == 201
