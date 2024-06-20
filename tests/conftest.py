import os

import pytest

from project import create_app_wsgi
from project.ext.database import db
from sqlalchemy import Engine, event
from project.models.user_model import User
from project.models.restaurant_model import Restaurant
from project.models.product_model import Product
from project.models.client_model import Client
from project.models.order_model import Order
from tests.factory.client_factory import ClientFactory
from tests.factory.order_factory import OrderFactory
from tests.factory.product_factory import ProductFactory
from tests.factory.restaurant_factory import RestaurantFactory
from tests.factory.user_factory import UserFactory


# TODO: Define o pragma de chaves estrangeiras para conexões de banco de dados SQLite.
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    """
    Define o pragma de chaves estrangeiras para conexões de banco de dados SQLite.

    Args:
        dbapi_connection: O objeto de conexão com o banco de dados.
        connection_record: O objeto de registro de conexão.
    """
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


@pytest.fixture
def app_testing():
    """
    Configura o ambiente de teste para a aplicação.

    Define a variável de ambiente 'FLASK_ENV' como 'testing'.
    Cria uma instância da aplicação usando a função 'create_app_wsgi()'.
    Cria o banco de dados usando o contexto da aplicação.
    Retorna a instância da aplicação.
    Ao finalizar o teste, remove o banco de dados.

    Returns:
        app: Instância da aplicação configurada para teste.
    """
    os.environ["FLASK_ENV"] = "testing"
    app = create_app_wsgi()
    with app.app_context():
        db.create_all()
    yield app
    with app.app_context():
        db.drop_all()


@pytest.fixture
def user(app_testing):
    """
    Cria uma ingessão de User para os testes.

    Args:
        session (Session): Uma instância de Session do SQLAlchemy.

    Returns:
        User: Uma instância de User do sistema.
    """
    app = app_testing
    with app.app_context():
        user = User(firstname="Tony", lastname="Stark", email="ironman@icloud.com")
        db.session.add(user)
        db.session.commit()
        db.session.refresh(user)

    return user


@pytest.fixture
def User_10(app_testing):
    """
    Cria uma lista de 10 objetos usuário para os testes.
    """
    UserFactory.reset_sequence()
    users = UserFactory.build_batch(10)

    app = app_testing
    with app.app_context():
        for user in users:
            db.session.add(user)
        db.session.commit()

    return users


@pytest.fixture
def cliente(app_testing):
    """
    Cria uma ingessão de cliente para os testes.

    Returns:
        cliente: Uma instância de cliente do sistema.
    """
    app = app_testing
    with app.app_context():
        cliente = Client(
            client_name="John Doe",
            client_cellphone="69999999999",
            client_address="1600 Amphitheatre Parkway",
            client_address_number="1600",
            client_address_complement="",
            client_address_neighborhood="Mountain View",
            client_zip_code="94043",
        )
        db.session.add(cliente)
        db.session.commit()
        db.session.refresh(cliente)

    return cliente


@pytest.fixture
def client_10(app_testing):
    """
    Cria uma lista de 10 objetos cliente para os testes.
    """
    ClientFactory.reset_sequence()
    clients = ClientFactory.build_batch(10)

    app = app_testing
    with app.app_context():
        for client in clients:
            db.session.add(client)
        db.session.commit()

    return clients


@pytest.fixture
def restaurant(app_testing):
    """
    Cria uma ingessão de restaurante para os testes.

    Returns:
        restaurant: Uma instância de restaurante do sistema.
    """
    app = app_testing
    with app.app_context():
        restaurant = Restaurant(
            name="Bóde do Nô",
            description="Descrição do restaurante",
            classification=4.9,
            location="Recife-PE",
            url_image_logo="url_logo",
            url_image_banner="url_banner",
        )
        # product = Product(
        #     name='Produto Exemplo',
        #     value=10.5,
        #     description='Descrição do produto exemplo',
        #     url_image='url_produto',
        #     restaurant_id=1
        # )
        db.session.add(restaurant)
        # db.session.add(product)
        db.session.commit()
        db.session.refresh(restaurant)
        # db.session.refresh(product)

    return restaurant


@pytest.fixture
def restaurant_10(app_testing):
    """
    Cria uma lista de 10 objetos restaurante para os testes.
    """
    RestaurantFactory.reset_sequence()
    restaurants = RestaurantFactory.build_batch(10)

    app = app_testing
    with app.app_context():
        for restaurant in restaurants:
            db.session.add(restaurant)
        db.session.commit()

    return restaurants


@pytest.fixture
# TODO: Essa fixture precisa ser usada em conjunto com a fixtures (restaurant)
def product(app_testing):
    """
    Cria uma ingessão de produtos para os testes.

    Returns:
        product: Uma instância de produtos do sistema.
    """
    app = app_testing
    with app.app_context():
        product = Product(
            name="X-Bacon",
            value=20,
            description="Bacon",
            url_image="url_image",
            restaurant_id=1,
        )
        db.session.add(product)
        db.session.commit()
        db.session.refresh(product)

    return product


@pytest.fixture
def product_10(app_testing):
    """
    Cria uma lista de 10 objetos produtos para os testes.
    """
    ProductFactory.reset_sequence()
    products = ProductFactory.build_batch(10)

    app = app_testing
    with app.app_context():
        for product in products:
            db.session.add(product)
        db.session.commit()

    return products


@pytest.fixture
# TODO: essa fixture precisa ser usada em conjunto com as fixtures (cliente, restaurant, product)
def order(app_testing):
    """
    Cria uma ingessão de ordem de pedido para os testes.

    Returns:
        order: Uma instância de ordem de pedido do sistema.
    """
    app = app_testing
    with app.app_context():
        product = db.session.query(Product).get(1)
        order = Order(client_id=1, restaurant_id=1, products=[product])
        db.session.add(order)
        db.session.commit()
        db.session.refresh(order)

    return order


@pytest.fixture
def order_10(app_testing):
    """
    Cria uma lista de 10 objetos ordem de pedido para os testes.
    """
    OrderFactory.reset_sequence()
    orders = OrderFactory.build_batch(10)

    app = app_testing
    with app.app_context():
        for order in orders:
            db.session.add(order)
        db.session.commit()

    return orders
