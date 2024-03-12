from flask_marshmallow import Marshmallow
from marshmallow import fields

from project.models.order_model import Order
from project.models.product_model import Product
from project.models.restaurant_model import Restaurant
from project.models.user_model import User
from project.models.client_model import Client


ma = Marshmallow()


def init_app(app):
    ma.init_app(app)


class ClientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Client
        load_instance = True


class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order
        load_instance = True
        include_relationships = True


class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = True


class RestaurantSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Restaurant
        load_instance = True


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        orders = fields.Nested(OrderSchema)
        include_relationships = True