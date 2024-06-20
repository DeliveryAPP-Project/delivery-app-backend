from .database import db
from ..models.client_model import Client
from ..models.product_model import Product
from ..models.restaurant_model import Restaurant


def populate_database() -> None:
    data = [
        Client(
            client_name="João",
            client_cellphone="47999999999",
            client_address="Rua da Sé",
            client_address_number=60,
            client_address_complement="Casa",
            client_address_neighborhood="Bairro da Sé",
            client_zip_code="89898989",
        ),
        Product(
            name="X-Picanha",
            value=4,
            description="Carne",
            url_image="url image",
            restaurant_id=1,
        ),
        Restaurant(
            name="Bóde do Nô",
            description="Descrição do restaurante",
            classification=4.9,
            location="Recife-PE",
            url_image_logo="url_logo",
            url_image_banner="url_banner",
        ),
    ]

    db.session.bulk_save_objects(data)
    db.session.commit()
