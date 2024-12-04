from datetime import time
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
            horario_funcionamento=time(8, 0, 0),  # 08:00:00
            horario_fechamento=time(22, 0, 0)     # 22:00:00
        ),
    ]

    db.session.bulk_save_objects(data)
    db.session.commit()
