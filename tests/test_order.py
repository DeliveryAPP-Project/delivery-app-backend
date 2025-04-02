def test_list_order_return_200(app_testing, order_factory):
    # Agora order_factory contém uma lista de pedidos já criados
    client = app_testing.test_client()
    response = client.get('/api/v1/orders/')
    assert response.status_code == 200

def test_post_order_return_200(app_testing):
    client = app_testing.test_client()

    order_data = {
    "client_name":"João Silva",
    "client_cellphone": "12345678970",
    "client_address": "Rua Exemplo",
    "client_address_number": 55,
    "client_address_complement": "Casa",
    "client_address_neighborhood": "Bairro Exemplo",
    "client_zip_code": "12345678",
    "restaurant_id": 1,
    "products": [1]
}

    response = client.post('/api/v1/orders/', json=order_data)
   
    assert response.status_code == 201