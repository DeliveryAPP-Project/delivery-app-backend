from flask import Blueprint
from flask_restx import Api, fields

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
        "url_image_logo": fields.String(description="URL da logo do restaurante"),
        "url_image_banner": fields.String(description="URL do banner do restaurante"),
        "telephone": fields.String(
            required=True, description="Telefone do restaurante"
        ),
        "has_plastic": fields.Boolean(
            required=True, description="Indica se o restaurante usa plástico"
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
        "url_image": fields.String(description="URL da imagem do produto"),
        "food_type": fields.String(required=True, description="Tipo de comida"),
        "has_gluten": fields.Boolean(
            required=True, description="Indica se o produto contém glúten"
        ),
        "has_lactose": fields.Boolean(
            required=True, description="Indica se o produto contém lactose"
        ),
        "is_vegan": fields.Boolean(
            required=True, description="Indica se o produto é vegano"
        ),
        "is_vegetarian": fields.Boolean(
            required=True, description="Indica se o produto é vegetariano"
        ),
        "restaurant_id": fields.Integer(required=True, description="ID do restaurante"),
    },
)

order_model = api.model(
    "Order",
    {
        "client_id": fields.Integer(required=True, description="ID do cliente"),
        "restaurant_id": fields.Integer(required=True, description="ID do restaurante"),
        "total_value": fields.Float(description="Valor total do pedido"),
        "status": fields.String(description="Status do pedido"),
        "products": fields.List(fields.Integer, description="ID dos produtos"),
    },
)

client_model = api.model(
    "Client",
    {
        "name": fields.String(required=True, description="Nome do cliente"),
        "cellphone": fields.String(required=True, description="Celular do cliente"),
        "cpf": fields.String(required=True, description="CPF do cliente"),
        "address": fields.String(required=True, description="Endereço do cliente"),
        "address_number": fields.Integer(
            required=True, description="Número do endereço do cliente"
        ),
        "address_complement": fields.String(
            description="Complemento do endereço do cliente"
        ),
        "address_neighborhood": fields.String(
            description="Bairro do endereço do cliente"
        ),
        "zip_code": fields.String(
            required=True, description="CEP do endereço do cliente"
        ),
        "email": fields.String(required=True, description="E-mail do cliente"),
    },
)
payment_model = api.model(
    "Payment",
    {
        "id": fields.Integer(description="ID do pagamento"),
        "created_at": fields.DateTime(description="Data de criação do pagamento"),
        "total_value": fields.Float(
            required=True, description="Valor total do pagamento"
        ),
        "type": fields.String(required=True, description="Tipo de pagamento"),
        "status": fields.String(description="Status do pagamento"),
        "order_id": fields.Integer(required=True, description="ID do pedido"),
    },
)
