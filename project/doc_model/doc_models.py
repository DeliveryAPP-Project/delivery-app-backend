from flask import Blueprint
from flask_restx import Api, fields

bp = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = Api(bp)

lead_model = api.model(
    "Lead",
    {
        "email": fields.String(required=True, description="E-mail do lead"),
    },
)


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
