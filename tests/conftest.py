import os

import fakeredis
import pytest

from project import create_app_wsgi
from project.ext.database import db

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


@pytest.fixture
def app_testing():
    os.environ['FLASK_ENV'] = 'testing'
    app = create_app_wsgi()
    with app.app_context():
        db.create_all()

    yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def fake_redis():
    return fakeredis.FakeStrictRedis()

@pytest.fixture
def user_factory():
    for user_factory in UserFactory:
        user = User(**user_factory)
        db.session.add(user)

@pytest.fixture
def restaurant_factory():
    for restaurant_factory in RestaurantFactory:
        restaurant = Restaurant(**restaurant_factory)
        db.session.add(restaurant)

@pytest.fixture
def client_factory():
    for client_factory in ClientFactory:
        client = Client(**client_factory)
        db.session.add(client)

@pytest.fixture
def product_factory():
    for product_data in ProductFactory:
        product = Product(**product_data)
        db.session.add(product)

@pytest.fixture
def order_factory():
    for order_factory in OrderFactory:
        order = Order(**order_factory)
        db.session.add(order)
        

