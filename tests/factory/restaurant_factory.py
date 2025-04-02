# from datetime import time
import factory
from project.ext.database import db
from project.models.restaurant_model import Restaurant
from tests.factory.product_factory import ProductFactory


class RestaurantFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Restaurant
        sqlalchemy_session = db.session

    id = factory.Sequence(lambda n: n)
    name = factory.Sequence(lambda n: f"Restaurant{n}")
    description = factory.Sequence(lambda n: f"Description{n}")
    classification = factory.Sequence(lambda n: round(n * 0.5, 1))
    url_image_logo = factory.Sequence(lambda n: f"Url{n}")
    url_image_banner = factory.Sequence(lambda n: f"Url{n}")
    telephone = factory.Sequence(lambda n: f"1234567890{n % 10}")
    has_plastic = factory.Sequence(lambda n: n % 2 == 0)

    # TODO: Retiraram o horário de funcionamento???
    # horario_funcionamento = factory.LazyFunction(lambda: time(9, 0))  # Abre às 9:00
    # horario_fechamento = factory.LazyFunction(lambda: time(21, 0))    # Fecha às 21:00
    
    # Remover estas linhas:
    # products = factory.SubFactory(ProductFactory) 
    # products_id = factory.LazyAttribute(lambda obj: obj.products.id)
    
    # Para criar produtos relacionados ao restaurante após sua criação:
    @factory.post_generation
    def create_products(self, create, extracted, **kwargs):
        if not create:
            return
        
        # Criar 3 produtos para este restaurante
        for _ in range(3):
            ProductFactory(restaurant=self)
