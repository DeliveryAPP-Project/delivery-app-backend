from flask import Blueprint
from flask_restx import Api, fields

from project.controller.user_controller import UserResource, UserResourceID
from project.utils.namespace import (
    client_ns,
    order_ns,
    product_ns,
    restaurant_ns,
    user_ns,
)

from ...controller.client_controller import ClientResource, ClientResourceID
from ...controller.order_controller import OrderResource, OrderResourceID
from ...controller.product_controller import ProductResource, ProductResourceID
from ...controller.restaurant_controller import RestaurantResource, RestaurantResourceID


bp = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = Api(bp)


restaurant_model = api.model(
    "Restaurant",
    {
        "name": fields.String(required=True, description="Nome do restaurante"),
        "description": fields.String(
            required=True, description="Descrição do restaurante"
        ),
        "classification": fields.Float(
            required=True, description="Classificação do restaurante"
        ),
        "location": fields.String(
            required=True, description="Localização do restaurante"
        ),
        "url_image_logo": fields.String(
            required=True, description="URL da logo do restaurante"
        ),
        "url_image_banner": fields.String(
            required=True, description="URL do banner do restaurante"
        ),
        "horario_funcionamento": fields.String(
            required=False, description="Horário de funcionamento"
        ),
        "horario_fechamento": fields.String(
            required=False, description="Horário de fechamento"
        ),
    },
)

user_model = api.model(
    "User",
    {
        "firstname": fields.String(required=True, description="Nome de usuário"),
        "lastname": fields.String(required=True, description="Sobrenome de usuário"),
        "email": fields.String(required=True, description="E-mail"),
    },
)

product_model = api.model(
    "Product",
    {
        "name": fields.String(required=True, description="Nome do produto"),
        "value": fields.Float(required=True, description="Valor do produto"),
        "description": fields.String(required=True, description="Descrição do produto"),
        "url_image": fields.String(
            required=True, description="URL da imagem do produto"
        ),
        "restaurant_id": fields.Integer(required=True, description="ID do restaurante"),
    },
)

order_model = api.model(
    "Order",
    {
        "created_at": fields.DateTime(required=True, description="Data de criação"),
        "client_id": fields.Integer(required=True, description="ID do cliente"),
        "restaurant_id": fields.Integer(required=True, description="ID do restaurante"),
        "products": fields.List(fields.Integer, description="ID dos produtos"),
    },
)

client_model = api.model(
    "Client",
    {
        "client_name": fields.String(required=True, description="Nome do cliente"),
        "client_cellphone": fields.String(
            required=True, description="Celular do cliente"
        ),
        "client_address": fields.String(
            required=True, description="Endereço do cliente"
        ),
        "client_address_number": fields.Integer(
            required=True, description="Número do endereço do cliente"
        ),
        "client_address_complement": fields.String(
            required=True, description="Complemento do endereço do cliente"
        ),
        "client_address_neighborhood": fields.String(
            required=True, description="Bairro do endereço do cliente"
        ),
        "client_zip_code": fields.String(
            required=True, description="CEP do endereço do cliente"
        ),
    },
)

# Adicionar os modelos aos namespaces
restaurant_ns.models["RestaurantModel"] = restaurant_model
user_ns.models["UserModel"] = user_model
product_ns.models["ProductModel"] = product_model
client_ns.models["ClientModel"] = client_model
order_ns.models["OrderModel"] = order_model

# # Adicionar os recursos aos namespaces
restaurant_ns.add_resource(RestaurantResource, "/")
restaurant_ns.add_resource(RestaurantResourceID, "/<int:id>/products")

user_ns.add_resource(UserResource, "/")
user_ns.add_resource(UserResourceID, "/<int:id>")

product_ns.add_resource(ProductResource, "/")
product_ns.add_resource(ProductResourceID, "/<int:id>")

client_ns.add_resource(ClientResource, "/")
client_ns.add_resource(ClientResourceID, "/<int:id>")

order_ns.add_resource(OrderResource, "/")
order_ns.add_resource(OrderResourceID, "/<int:id>")


# Adicionar os namespaces ao API
api.add_namespace(restaurant_ns)
api.add_namespace(user_ns)
api.add_namespace(product_ns)
api.add_namespace(client_ns)
api.add_namespace(order_ns)


def init_app(app):
    app.register_blueprint(bp)
    api.add_namespace(restaurant_ns)
    api.add_namespace(user_ns)
    api.add_namespace(product_ns)
    api.add_namespace(client_ns)
    api.add_namespace(order_ns)
