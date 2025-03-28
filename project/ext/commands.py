from .database import db
from ..models.client_model import Client
from ..models.product_model import Product
from ..models.establishment_model import Establishment

def populate_database():
        data = [
        Client( 
                client_name= "João",
                client_cellphone= "47999999999",
                client_address= "Rua da Sé",
                client_address_number= 60,
                client_address_complement= "Casa",
                client_address_neighborhood= "Bairro da Sé",
                client_zip_code= "89898989"
                ),
        Product(
                name= "X-Picanha",
                value= 4,
                description= "Carne",
                url_image= "url image",
                establishment_id= 1
                ),
       Establishment(
                official_name="Bóde do Nô",
                fantasy_name="Bóde do Nô",
                cnpj="12345678000199",
                telephone="11987654321",
                zip_code="01001000",
                state="Pernambuco",
                city="Recife",
                address="Rua das Flores, 123",
                complement="Próximo à praça central",
                )
        ]

        db.session.bulk_save_objects(data)
        db.session.commit()