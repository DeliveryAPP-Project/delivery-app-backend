import requests

mock_establishments = [
    {
        "id": 1,
        "official_name": "Bóde do Nô",
        "fantasy_name": "Bóde do Nô",
        "cnpj": "12345678000199",
        "telephone": "81999998888",
        "zip_code": "50000-000",
        "state": "Pernambuco",
        "city": "Recife",
        "address": "Rua das Ostras, 123",
        "complement": "Ao lado do mercado central",
    },
    {
        "id": 2,
        "official_name": "Imperador dos Camarões",
        "fantasy_name": "Imperador dos Camarões",
        "cnpj": "98765432000188",
        "telephone": "82988887777",
        "zip_code": "57000-000",
        "state": "Alagoas",
        "city": "Maceió",
        "address": "Av. Beira Mar, 456",
        "complement": "Próximo ao shopping",
    },
]


mock_products = [
    {
        "id": 1,
        "name": "Espetinho de carne",
        "food_type": "Brasileira",
        "value": 9.50,
        "description": "Espetinho de carne de boi, acompanhado de farofa",
        "url_image": "https://www.estadao.com.br/resizer/v2/GM7NDPXYHBLGRJ6BSOSOK35BYQ.jpg?quality=80&auth=2f03dd4aee8450f958b7f6a5b59c4ea50418183cc15561c066168b008203aa19&width=720&height=503&focal=0,0",
        "has_gluten": True,
        "has_lactose": True,
        "is_vegan": False,
        "is_vegetarian": False,
        "establishment_id": 1,
    },
    {
        "id": 2,
        "name": "Alcatra com acompanhamento",
        "food_type": "Brasileira",
        "value": 32.50,
        "description": "Corte de carne bovina, muito macio e saboroso. Acompanhado de arroz, feijão e purê de batata",
        "url_image": "https://clubfitlife.com.br/lojas/clubfitlife/conteudo/uploads/carne-em-tiras-aceboladas-com-arroz-branco-feijao-e-pure-de-batatas-60f71b00f2aa3-643d52f8781d9.jpg",
        "has_gluten": False,
        "has_lactose": False,
        "is_vegan": False,
        "is_vegetarian": False,
        "establishment_id": 1,
    },
    {
        "id": 3,
        "name": "Iscas de camarão",
        "food_type": "Brasileira",
        "value": 35,
        "description": "Iscas de camarão, mergulhado em temperos e especiarias, empanado com farinha de rosca e parmesão",
        "url_image": "https://gastronomiasdicas.com.br/wp-content/uploads/2023/11/Receita-de-camarao-alho-e-oleo-delicioso-igual-de-praia.webp",
        "has_gluten": True,
        "has_lactose": False,
        "is_vegan": False,
        "is_vegetarian": False,
        "establishment_id": 2,
    },
    {
        "id": 4,
        "name": "Moqueca de Peixe",
        "food_type": "Brasileira",
        "value": 26,
        "description": "Ensopado de peixe cozido com leite de coco, azeite de dendê, tomates, cebolas, pimentões e coentro.",
        "url_image": "https://cdn0.tudoreceitas.com/pt/posts/0/8/9/moqueca_de_peixe_baiana_9980_orig.jpg",
        "has_gluten": False,
        "has_lactose": False,
        "is_vegan": False,
        "is_vegetarian": False,
        "establishment_id": 2,
    },
]


mock_users = [
    {
        "id": 1,
        "firstname": "João",
        "lastname": "Pereira",
        "email": "joaopereira@gmail.com",
    },
    {
        "id": 2,
        "firstname": "Maria",
        "lastname": "Silva",
        "email": "mariasilva@hotmail.com",
    },
]


mock_clients = [
    {
        "id": 1,
        "name": "João Pereira",
        "cellphone": "47999567032",
        "cpf": "12345678911",
        "address": "Rua das Palmeiras",
        "address_number": 67,
        "address_complement": "Casa verde, ao lado de uma padaria",
        "address_neighborhood": "Bela Vista",
        "zip_code": "12345678",
        "email": "joaopereira@gmail.com",
    },
    {
        "id": 2,
        "name": "Maria Silva",
        "cellphone": "41996314578",
        "cpf": "12345678910",
        "address": "Rua Teodoro Sampaio",
        "address_number": 251,
        "address_complement": "Casa azul, em frente ao mercado",
        "address_neighborhood": "Bom Fim",
        "zip_code": "98765432",
        "email": "mariasilva@hotmail.com",
    },
]


mock_orders = [
    {
        "id": 1,
        "client_id": 1,
        "establishment_id": 1,
        "products": [1],
        "payment": "Dinheiro",
    },
    {
        "id": 2,
        "client_id": 2,
        "establishment_id": 2,
        "products": [3, 4],
        "payment": "Pix",
    },
]


url = "http://127.0.0.1:5000/api/v1/"


headers = {"Content-Type": "application/json"}


for establishment in mock_establishments:
    response = requests.post(
        f"{url}/establishments/", json=establishment, headers=headers
    )
    print(response.status_code, "establishment")

for product in mock_products:
    response = requests.post(f"{url}/products/", json=product, headers=headers)
    print(response.status_code, "products")

for user in mock_users:
    response = requests.post(f"{url}/users/", json=user, headers=headers)
    print(response.status_code, "users")

for client in mock_clients:
    response = requests.post(f"{url}/clients/", json=client, headers=headers)
    print(response.status_code, "clients")

for order in mock_orders:
    response = requests.post(f"{url}/orders/", json=order, headers=headers)
    print(response.status_code, "orders")
