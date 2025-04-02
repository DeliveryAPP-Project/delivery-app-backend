import os

import fakeredis
import pytest

from project import create_app_wsgi
from project.ext.database import db

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
    users = UserFactory.create_batch(3)
    db.session.commit()
    return users

@pytest.fixture
def restaurant_factory():
    restaurants = RestaurantFactory.create_batch(3)
    db.session.commit()
    return restaurants

@pytest.fixture
def client_factory():
    clients = ClientFactory.create_batch(3)
    db.session.commit()
    return clients

@pytest.fixture
def product_factory():
    products = ProductFactory.create_batch(5)
    db.session.commit()
    return products

@pytest.fixture
def order_factory():
    orders = OrderFactory.create_batch(3)
    db.session.commit()
    return orders