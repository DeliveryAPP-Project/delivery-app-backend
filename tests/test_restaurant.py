def test_list_restaurant_return_200(app_testing):
    restaurant = app_testing.test_client()
    response = restaurant.get("http://127.0.0.1:5000/api/v1/restaurants/")
    assert response.status_code == 200


def test_post_restaurant_return_200(app_testing):
    client = app_testing.test_client()

    restaurant_data = {
        "name": "Restaurante Teste",
        "description": "Descrição do restaurante de teste",
        "classification": 4.5,
        "location": "Cidade do Teste",
        "url_image_logo": "url_logo_teste",
        "url_image_banner": "url_banner_teste",
        "telephone": "1234567890",
        "has_plastic": False,
    }

    response = client.post("/api/v1/restaurants/", json=restaurant_data)

    assert response.status_code == 201
