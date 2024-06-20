import factory
from factory.alchemy import SQLAlchemyModelFactory
from datetime import datetime


from project.ext.database import db
from project.models.order_model import Order
from tests.factory.client_factory import ClientFactory
from tests.factory.product_factory import ProductFactory
from tests.factory.restaurant_factory import RestaurantFactory


class OrderFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Order
        sqlalchemy_session = db.session

    id = factory.Sequence(lambda n: n)
    created_at = factory.LazyFunction(datetime.now)
    # TODO: o relacionamento com o cliente
    client = factory.SubFactory(ClientFactory)
    client_id = factory.LazyAttribute(lambda obj: obj.client.id)
    # TODO: o relacionamento com o restaurante
    restaurant = factory.SubFactory(RestaurantFactory)
    restaurant_id = factory.LazyAttribute(lambda obj: obj.restaurant.id)
    total_value = factory.Sequence(lambda n: n * 10.0)
    # TODO: uma lista de produtos
    products = factory.List([factory.SubFactory(ProductFactory) for _ in range(5)])
