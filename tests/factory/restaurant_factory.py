import factory
from factory.alchemy import SQLAlchemyModelFactory
from project.ext.database import db
from project.models.restaurant_model import Restaurant


class RestaurantFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Restaurant
        sqlalchemy_session = db.session

    id = factory.Sequence(lambda n: n)
    name = factory.Sequence(lambda n: f"Restaurant{n}")
    classification = factory.Sequence(lambda n: n)
    description = factory.Sequence(lambda n: f"Description{n}")
    location = factory.Sequence(lambda n: f"Location{n}")
    url_image_logo = factory.Sequence(lambda n: f"Url{n}")
    url_image_banner = factory.Sequence(lambda n: f"Url{n}")
