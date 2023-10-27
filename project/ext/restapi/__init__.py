from flask import Blueprint
from flask_restx import Api

from project.controller.user_controller import UserResource, UserResourceId
from project.utils.namespace import product_ns, restaurant_ns, user_ns

from ...controller.product_controller import ProductResource, ProductResourceId
from ...controller.restaurant_controller import (RestaurantResource,
                                                 RestaurantResourceId)

bp = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = Api(bp)


def init_app(app):
    app.register_blueprint(bp)
    api.add_resource(RestaurantResource, "/restaurants/")
    api.add_resource(RestaurantResourceId, "/restaurant/<int:id>")
    api.add_namespace(restaurant_ns)
    api.add_resource(UserResource, "/users/")
    api.add_resource(UserResourceId, "/user/<int:id>")
    api.add_namespace(user_ns)
    api.add_resource(ProductResource, "/products")
    api.add_resource(ProductResourceId, "/product/<int:id>")
    api.add_namespace(product_ns)