import factory
from factory.alchemy import SQLAlchemyModelFactory
from project.ext.database import db
from project.models.product_model import Product
from tests.factory.restaurant_factory import RestaurantFactory


class ProductFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Product
        sqlalchemy_session = db.session

    id = factory.Sequence(lambda n: n)
    name = factory.Sequence(lambda n: f"Product{n}")
    description = factory.Sequence(lambda n: f"Description{n}")
    value = factory.Sequence(lambda n: n)
    url_image = factory.Sequence(lambda n: f"Url{n}")
    # TODO: o relacionamento com o restaurante
    restaurant = factory.SubFactory(RestaurantFactory)
    restaurant_id = factory.LazyAttribute(lambda obj: obj.restaurant.id)
