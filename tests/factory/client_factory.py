import factory


from project.models.client_model import Client
from project.ext.database import db


class ClientFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Client
        sqlalchemy_session = db.session

    id = factory.Sequence(lambda n: n)
    client_name = factory.Sequence(lambda n: f"Client{n}")
    client_cellphone = factory.Sequence(lambda n: f"123456789{n}")
    client_cpf = factory.Sequence(lambda n: f"123456789{n}")
    client_address = factory.Sequence(lambda n: f"Street{n}")
    client_address_number = factory.Sequence(lambda n: n)
    client_address_complement = factory.Sequence(lambda n: f"Complement{n}")
    client_address_neighborhood = factory.Sequence(lambda n: f"Neighborhood{n}")
    client_zip_code = factory.Sequence(lambda n: f"Zip{n}")