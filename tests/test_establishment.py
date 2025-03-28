def test_list_establishment_return_200(app_testing):
    establishments = app_testing.test_client()
    response = establishments.get("http://127.0.0.1:5000/api/v1/establishments/")
    assert response.status_code == 200


def test_post_establishment_return_200(app_testing):
    client = app_testing.test_client()
    
    establishment_data = {
        "official_name": "Estabelecimento do Teste",
        "fantasy_name": "Estabelecimento Nome do Teste",
        "cnpj": "12345678000199",
        "telephone": "1234567890",
        "zip_code": "01001000",
        "state": "Estado do Teste",
        "city": "Cidade do Teste",
        "address": "Rua do Teste",
        "complement": "Complemento do Teste"
    }

    response = client.post("/api/v1/establishments/", json=establishment_data)
    
    assert response.status_code == 201
