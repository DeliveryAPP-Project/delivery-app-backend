import os

import fakeredis
import pytest

from project import create_app_wsgi
from project.ext.database import db
from project.models.client_model import Client
from project.models.order_model import Order
from project.models.payment_model import Payment
from project.models.product_model import Product
from project.models.restaurant_model import Restaurant
from project.models.user_model import User


@pytest.fixture
def app_testing():
    os.environ["FLASK_ENV"] = "testing"
    app = create_app_wsgi()
    with app.app_context():
        db.create_all()
        seed()

    yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def fake_redis():
    return fakeredis.FakeStrictRedis()


def seed():
    user = User(firstname="John", lastname="Doe", email="john.doe@example.com")
    db.session.add(user)
    db.session.commit()

    client = Client(
        name="Jane Doe",
        cellphone="12345678901",
        cpf="12345678901",
        address="123 Main St",
        address_number=123,
        address_complement="Apt 4",
        address_neighborhood="Downtown",
        zip_code="12345678",
        email="jane.doe@example.com",
    )
    db.session.add(client)
    db.session.commit()

    restaurant = Restaurant(
        name="Good Food",
        description="A nice place to eat",
        classification=4.5,
        location="456 Food St",
        telephone="09876543210",
    )
    db.session.add(restaurant)
    db.session.commit()

    product = Product(
        name="Pizza",
        value=19.99,
        description="Delicious cheese pizza",
        food_type="Pizza",
        restaurant_id=restaurant.id,
    )
    db.session.add(product)
    db.session.commit()

    order = Order(
        client_id=client.id,
        restaurant_id=restaurant.id,
        total_value=19.99,
        status="pre_order",
    )
    db.session.add(order)
    db.session.commit()

    payment = Payment(
        total_value=19.99, type="Dinheiro", status="pending", order_id=order.id
    )
    db.session.add(payment)

    db.session.commit()
