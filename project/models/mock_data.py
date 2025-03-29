"""Dados estáticos para uso em desenvolvimento"""

mock_establishments = [
    {
        "id": 1, "official_name": "Bóde do Nô", "fantasy_name": "Bóde do Nô",
        "cnpj": "12345678000199", "telephone": "81999998888", "zip_code": "50000-000",
        "state": "Pernambuco", "city": "Recife", "address": "Rua das Ostras, 123",
        "complement": "Ao lado do mercado central"
    },
    {
        "id": 2, "official_name": "Imperador dos Camarões", "fantasy_name": "Imperador dos Camarões",
        "cnpj": "98765432000188", "telephone": "82988887777", "zip_code": "57000-000",
        "state": "Alagoas", "city": "Maceió", "address": "Av. Beira Mar, 456",
        "complement": "Próximo ao shopping"
    },
    {
        "id": 3, "official_name": "Bar da Sogra", "fantasy_name": "Bar da Sogra",
        "cnpj": "11223344000177", "telephone": "71977776666", "zip_code": "40000-000",
        "state": "Bahia", "city": "Salvador", "address": "Rua do Porto, 789",
        "complement": "Em frente à praia"
    },
    {
        "id": 4, "official_name": "Raspa Tácho", "fantasy_name": "Raspa Tácho",
        "cnpj": "55667788000166", "telephone": "85966665555", "zip_code": "60000-000",
        "state": "Ceará", "city": "Fortaleza", "address": "Rua das Dunas, 321",
        "complement": "Atrás do mercado público"
    },
    {
        "id": 5, "official_name": "Boi na Brasa", "fantasy_name": "Boi na Brasa",
        "cnpj": "66778899000155", "telephone": "85955554444", "zip_code": "60000-001",
        "state": "Ceará", "city": "Fortaleza", "address": "Av. Central, 654",
        "complement": "Próximo ao estádio"
    }
]


mock_products = [
    {"id": 1, "name": "X-Bacon", "value": 20, "description": "Bacon",
     "url_image": "url_image", "establishment_id": 1},
    {"id": 2, "name": "X-Picanha", "value": 20, "description": "Picanha",
     "url_image": "url_image", "establishment_id": 2},
    {"id": 3, "name": "X-Salada", "value": 20, "description": "Salada",
     "url_image": "url_image", "establishment_id": 3},
    {"id": 4, "name": "X-Frango", "value": 20, "description": "Frango",
     "url_image": "url_image", "establishment_id": 4},
    {"id": 5, "name": "X-Batata", "value": 20, "description": "Batata",
     "url_image": "url_image", "establishment_id": 5},
]

mock_users = [
    {"id": 1,
     "firstname": "Tony",
     "lastname": "Stark",
     "email": "ironman@icloud.com"},
    {"id": 2,
     "firstname": "Peter",
     "lastname": "Parker",
     "email": "spiderman@icloud.com"},
    {"id": 3,
     "firstname": "Bruce",
     "lastname": "Banner",
     "email": "hulk@icloud.com"},
    {"id": 4,
     "firstname": "Natasha",
     "lastname": "Romanoff",
     "email": "blackwidow@icloud.com"},
    {"id": 5,
     "firstname": "Steve",
     "lastname": "Rogers",
     "email": "captainamerica@icloud.com"}
]

mock_clients = [
    {
        "id": 1,
        "client_name": "John Doe",
        "client_cellphone": "69999999999",
        "client_address": "1600 Amphitheatre Parkway",
        "client_address_number": 1600,
        "client_address_complement": "",
        "client_address_neighborhood": "Mountain View",
        "client_zip_code": "94043"
    },
    {
        "id": 2,
        "client_name": "Jane Smith",
        "client_cellphone": "69998887777",
        "client_address": "One Microsoft Way",
        "client_address_number": 1,
        "client_address_complement": "",
        "client_address_neighborhood": "Redmond",
        "client_zip_code": "98052"
    },
    {
        "id": 3,
        "client_name": "Alice Johnson",
        "client_cellphone": "69995554444",
        "client_address": "1600 Pennsylvania Avenue NW",
        "client_address_number": 1600,
        "client_address_complement": "",
        "client_address_neighborhood": "Washington",
        "client_zip_code": "20500"
    },
    {
        "id": 4,
        "client_name": "Bob Brown",
        "client_cellphone": "69992221111",
        "client_address": "221B Baker Street",
        "client_address_number": 221,
        "client_address_complement": "",
        "client_address_neighborhood": "London",
        "client_zip_code": "NW1 6XE"
    },
    {
        "id": 5,
        "client_name": "Eva Green",
        "client_cellphone": "69991112222",
        "client_address": "1600 Pennsylvania Avenue NW",
        "client_address_number": 1600,
        "client_address_complement": "",
        "client_address_neighborhood": "Washington",
        "client_zip_code": "20500"
    }
]

mock_orders = [
    {
        "id": 1,
        "client_id": 1,
        "establishment_id": 1,
        "products": [1]
    },
    {
        "id": 2,
        "client_id": 2,
        "establishment_id": 2,
        "products": [2, 3]
    },
    {
        "id": 3,
        "client_id": 3,
        "establishment_id": 1,
        "products": [4]
    },
    {
        "id": 4,
        "client_id": 4,
        "establishment_id": 2,
        "products": [5]
    },
    {
        "id": 5,
        "client_id": 5,
        "establishment_id": 4,
        "products": [1, 2, 5]
    }
]