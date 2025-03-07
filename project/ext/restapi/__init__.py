from flask import Blueprint
from flask_restx import Api

from project.controller.lead_controller import LeadResource
from project.controller.user_controller import UserResource, UserResourceID
from project.models import (
    client_model,
    lead_model,
    order_model,
    product_model,
    restaurant_model,
    user_model,
)
from project.utils.namespace import (
    client_ns,
    lead_ns,
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

restaurant_ns.models["RestaurantModel"] = restaurant_model
user_ns.models["UserModel"] = user_model
product_ns.models["ProductModel"] = product_model
client_ns.models["ClientModel"] = client_model
order_ns.models["OrderModel"] = order_model
lead_ns.models["LeadModel"] = lead_model

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

lead_ns.add_resource(LeadResource, "/")


api.add_namespace(restaurant_ns)
api.add_namespace(user_ns)
api.add_namespace(product_ns)
api.add_namespace(client_ns)
api.add_namespace(order_ns)
api.add_namespace(lead_ns)


def init_app(app):
    app.register_blueprint(bp)
    api.add_namespace(restaurant_ns)
    api.add_namespace(user_ns)
    api.add_namespace(product_ns)
    api.add_namespace(client_ns)
    api.add_namespace(order_ns)
    api.add_namespace(lead_ns)
