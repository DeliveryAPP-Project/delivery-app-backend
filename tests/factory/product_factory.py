import factory
from project.ext.database import db
from project.models.product_model import Product


class ProductFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Product
        sqlalchemy_session = db.session

    id = factory.Sequence(lambda n: n)
    name = factory.Sequence(lambda n: f"Product{n}")
    description = factory.Sequence(lambda n: f"Description{n}")
    value = factory.Sequence(lambda n: n)
    url_image = factory.Sequence(lambda n: f"Url{n}")
    food_type = factory.Sequence(lambda n: f"Food{n}")
    has_gluten = factory.Sequence(lambda n: n % 2 == 0)
    has_lactose = factory.Sequence(lambda n: n % 2 == 0)
    is_vegan = factory.Sequence(lambda n: n % 2 == 0)
    is_vegetarian = factory.Sequence(lambda n: n % 2 == 0)
    # TODO: o relacionamento com o restaurante
    # restaurant = factory.SubFactory(RestaurantFactory)
    restaurant = factory.SubFactory('tests.factory.restaurant_factory.RestaurantFactory')
    restaurant_id = factory.LazyAttribute(lambda obj: obj.restaurant.id)