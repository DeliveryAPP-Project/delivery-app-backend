import os

import fakeredis
import pytest

from project import create_app_wsgi
from project.ext.database import db
from project.models.client_model import Client
from project.models.mock_data import (
    mock_clients,
    mock_orders,
    mock_products,
    mock_establishments,
    mock_users,
)
from project.models.order_model import Order
from project.models.payment_model import Payment
from project.models.product_model import Product
from project.models.establishment_model import Establishment
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

    establishments = [
        Establishment(
            name="Good Food",
            description="A nice place to eat",
            classification=4.5,
            location="456 Food St",
            telephone="09876543210",
        ),
        Establishment(
            name="Great Eats",
            description="Delicious meals",
            classification=4.7,
            location="789 Eatery Ave",
            telephone="01234567890",
        ),
        Establishment(
            name="Tasty Bites",
            description="Yummy snacks",
            classification=4.6,
            location="321 Snack Blvd",
            telephone="12345098765",
        ),
    ]
    db.session.add_all(establishments)
    db.session.commit()

    products = [
        Product(
            name="Pizza",
            value=19.99,
            description="Delicious cheese pizza",
            food_type="Pizza",
            establishment_id=establishments[0].id,
        ),
        Product(
            name="Burger",
            value=9.99,
            description="Juicy beef burger",
            food_type="Lanches",
            establishment_id=establishments[0].id,
        ),
        Product(
            name="Pasta",
            value=14.99,
            description="Creamy Alfredo pasta",
            food_type="Italiana",
            establishment_id=establishments[1].id,
        ),
        Product(
            name="Salad",
            value=7.99,
            description="Fresh garden salad",
            food_type="Brasileira",
            establishment_id=establishments[1].id,
        ),
        Product(
            name="Sushi",
            value=24.99,
            description="Assorted sushi platter",
            food_type="Japonesa",
            establishment_id=establishments[2].id,
        ),
        Product(
            name="Taco",
            value=4.99,
            description="Spicy chicken taco",
            food_type="Mexicana",
            establishment_id=establishments[2].id,
        ),
        Product(
            name="Steak",
            value=29.99,
            description="Grilled ribeye steak",
            food_type="Brasileira",
            establishment_id=establishments[0].id,
        ),
        Product(
            name="Ice Cream",
            value=5.99,
            description="Vanilla ice cream",
            food_type="Doces",
            establishment_id=establishments[1].id,
        ),establishments
    ]
    db.session.add_all(products)
    db.session.commit()

    orders = [
        Order(
            client_id=client.id,
            establishment_id=establishments[0].id,
            total_value=19.99,
        ),
        Order(
            client_id=client.id,
            establishment_id=establishments[1].id,
            total_value=59.99,
        ),
    ]

    db.session.add_all(orders)
    db.session.commit()

    payment = Payment(
        total_value=19.99, type="Dinheiro", status="pending", order_id=orders[0].id
    )

    db.session.add(payment)

    db.session.commit()
    