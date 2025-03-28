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

establishment_model = api.model(
    "Establishment",
    {
        "id": fields.Integer(description="ID do estabelecimento"),
        "official_name": fields.String(required=True, description="Nome oficial do estabelecimento"),
        "fantasy_name": fields.String(required=True, description="Nome fantasia do estabelecimento"),
        "cnpj": fields.String(required=True, description="CNPJ do estabelecimento"),
        "telephone": fields.String(required=True, description="Telefone do estabelecimento"),
        "zip_code": fields.String(required=True, description="CEP do estabelecimento"),
        "state": fields.String(required=True, description="Estado do estabelecimento"),
        "city": fields.String(required=True, description="Cidade do estabelecimento"),
        "address": fields.String(required=True, description="Endereço do estabelecimento"),
        "complement": fields.String(description="Complemento do endereço")
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
        "establishment_id": fields.Integer(required=True, description="ID do estabelecimento"),
    },
)

order_model = api.model(
    "Order",
    {
        "client_id": fields.Integer(required=True, description="ID do cliente"),
        "establishment_id": fields.Integer(required=True, description="ID do estabelecimento"),
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
        "payment_type": fields.String(
            required=True, description="Tipo de pagamento Ex: Pix ou Dinheiro"
        ),
        "order_id": fields.Integer(required=True, description="ID do pedido"),
    },
)
