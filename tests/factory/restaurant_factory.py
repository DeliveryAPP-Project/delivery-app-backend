from datetime import time, timedelta, datetime
import random
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
    horario_funcionamento = factory.LazyFunction(lambda: time(9, 0))  # Abre às 9:00
    horario_fechamento = factory.LazyFunction(lambda: time(21, 0))    # Fecha às 21:00
    url_image_logo = factory.Sequence(lambda n: f"Url{n}")
    url_image_banner = factory.Sequence(lambda n: f"Url{n}")