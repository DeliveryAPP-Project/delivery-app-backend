import factory
from factory.alchemy import SQLAlchemyModelFactory
from project.ext.database import db
from project.models.user_model import User


class UserFactory(SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = db.session

    id = factory.Sequence(lambda n: n)
    firstname = factory.Sequence(lambda n: f"Firstname{n}")
    lastname = factory.Sequence(lambda n: f"Lastname{n}")
    email = factory.Sequence(lambda n: f"email{n}@test.com")
