from project.models.mock_data import mock_clients

def test_list_client_return_200(app_testing):
    """
    Teste para verificar se o endpoint da API para listar clientes retorna o código de status 200.

    Args:
        app_testing: Uma instância do cliente de teste.

    Returns:
        None
    """
    client = app_testing.test_client()
    response = client.get('http://127.0.0.1:5000/api/v1/clients/')
    assert response.status_code == 200
    assert response.json == mock_clients

def test_post_client_return_200(app_testing):
    """
    Testa se a rota '/api/v1/clients/' retorna o código de status 201 (Created) ao fazer uma requisição POST com dados válidos de cliente.
    """
    client = app_testing.test_client()

    client_data = {
        "client_name": "Maria Oliveira",
        "client_cellphone": "69996666666",
        "client_address": "Rua do Teste, 123",
        "client_address_number": 123,
        "client_address_complement": "Apto 101",
        "client_address_neighborhood": "Bairro do Teste",
        "client_zip_code": "12345-678"
    }

    response = client.post('/api/v1/clients/', json=client_data)

    assert response.status_code == 201
    assert response.json['message'] == 'Cliente cadastrado com sucesso!'

def test_post_client_return_400(app_testing):
    """
    Testa se a rota '/api/v1/clients/' retorna o código de status 400 (Solicitação Incorreta) ao fazer uma requisição POST com dados invalidos de cliente.
    """
    client = app_testing.test_client()

    response = client.post('/api/v1/clients/', json={"invalid": "data"})


    assert response.status_code == 400
    assert response.json['error'] == "'invalid' is an invalid keyword argument for Client"

def test_get_one_client_return_200(app_testing):
    """
    Testa se a rota '/api/v1/clients/<int:id>/' retorna o código de status 200 ao fazer uma requisição GET com um ID de cliente válido.
    """
    client = app_testing.test_client()
    response = client.get(f'/api/v1/clients/{mock_clients[1]["id"]}')
    assert response.status_code == 200
    assert response.json == mock_clients[1]

def test_get_one_client_return_404(app_testing):
    """
    Testa se a rota '/api/v1/clients/<int:id>/' retorna o código de status 404 ao fazer uma requisição GET com um ID de cliente invalido.
    """
    client = app_testing.test_client()
    response = client.get('/api/v1/clients/0')
    assert response.status_code == 404
    assert response.json['error'] == 'Cliente com ID 0 não encontrado.'

def test_patch_client_return_200(app_testing):
    """
    Testa se a rota '/api/v1/clients/<int:id>/' retorna o código de status 200 ao fazer uma requisição PATCH com um ID de cliente válido.
    """
    client = app_testing.test_client()

    client_data = {
        "client_name": "Maria Oliveira",
        "client_cellphone": "69996666666",
        "client_address": "Rua do Teste, 123",
        "client_address_number": 123,
        "client_address_complement": "Apto 101",
        "client_address_neighborhood": "Bairro do Teste",
        "client_zip_code": "12345-678"
    }

    response = client.patch(f'/api/v1/clients/{mock_clients[1]["id"]}', json=client_data)

    assert response.status_code == 200
    assert response.json['message'] == 'Cliente com ID 2 atualizado com sucesso!'

def test_patch_client_return_500(app_testing):
    """
    Testa se a rota '/api/v1/clients/<int:id>/' retorna o código de status 500 ao fazer uma requisição PATCH com um ID de cliente invalido.
    """
    client = app_testing.test_client()
    response = client.patch('/api/v1/clients/0', json={})
    #FIXME: Não deveria ser 404??
    assert response.status_code == 500
    #FIXME: Não deveriamos ter um exception 'Cliente com ID 0 não encontrado'

def test_delete_client_return_200(app_testing):
    """
    Testa se a rota '/api/v1/clients/<int:id>/' retorna o código de status 200 ao fazer uma requisição DELETE com um ID de cliente válido.
    """
    client = app_testing.test_client()
    response = client.delete(f'/api/v1/clients/{mock_clients[1]["id"]}')
    assert response.status_code == 200
    assert response.json['message'] == 'CLiente com ID 2 deletado com sucesso.'

def test_delete_client_return_404(app_testing):
    """
    Testa se a rota '/api/v1/clients/<int:id>/' retorna o código de status 404 ao fazer uma requisição DELETE com um ID de cliente invalido.
    """
    client = app_testing.test_client()
    response = client.delete('/api/v1/clients/0')
    assert response.status_code == 404
    assert response.json['error'] == 'Cliente com ID 0 não encontrado'
    





