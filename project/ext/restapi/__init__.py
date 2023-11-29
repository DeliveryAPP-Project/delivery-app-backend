from flask import Blueprint
from flask_restx import Api

from project.controller.user_controller import UserResource
from project.utils.namespace import (client_ns, order_ns, product_ns,
                                     restaurant_ns, user_ns)

from ...controller.client_controller import ClientResource
from ...controller.order_controller import OrderResource
from ...controller.product_controller import ProductResource
from ...controller.restaurant_controller import RestaurantResource

bp = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = Api(bp)


def init_app(app):
    app.register_blueprint(bp)
    api.add_resource(RestaurantResource, "/restaurants/")
    api.add_namespace(restaurant_ns)
    api.add_resource(UserResource, "/users/")
    api.add_namespace(user_ns)
    api.add_resource(ProductResource, "/products/")
    api.add_namespace(product_ns)
    api.add_resource(ClientResource, "/clients/")
    api.add_namespace(client_ns)
    api.add_resource(OrderResource, "/orders/")
    api.add_namespace(order_ns)
