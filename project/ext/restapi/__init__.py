from project.controller.lead_controller import LeadResource
from project.controller.user_controller import UserResource, UserResourceID
from project.doc_model.doc_models import (
    api,
    bp,
    client_model,
    establishment_model,
    lead_model,
    order_model,
    payment_model,
    product_model,
    user_model,
)
from project.utils.namespace import (
    client_ns,
    establishment_ns,
    lead_ns,
    notification_ns,
    order_ns,
    payment_ns,
    product_ns,
    user_ns,
)

from ...controller.client_controller import ClientResource, ClientResourceID
from ...controller.establishment_controller import (
    EstablishmentResource,
    EstablishmentResourceID,
)
from ...controller.notification_controller import NotificationResource
from ...controller.order_controller import OrderResource, OrderResourceID
from ...controller.payment_controller import PaymentResource, PaymentResourceID
from ...controller.product_controller import ProductResource, ProductResourceID

establishment_ns.models["EstablishmentModel"] = establishment_model
user_ns.models["UserModel"] = user_model
product_ns.models["ProductModel"] = product_model
client_ns.models["ClientModel"] = client_model
order_ns.models["OrderModel"] = order_model
payment_ns.models["PaymentModel"] = payment_model
lead_ns.models["LeadModel"] = lead_model

establishment_ns.add_resource(EstablishmentResource, "/")
establishment_ns.add_resource(EstablishmentResourceID, "/<int:id>/products")

user_ns.add_resource(UserResource, "/")
user_ns.add_resource(UserResourceID, "/<int:id>")

product_ns.add_resource(ProductResource, "/")
product_ns.add_resource(ProductResourceID, "/<int:id>")

client_ns.add_resource(ClientResource, "/")
client_ns.add_resource(ClientResourceID, "/<int:id>")

order_ns.add_resource(OrderResource, "/")
order_ns.add_resource(OrderResourceID, "/<int:id>")

payment_ns.add_resource(PaymentResource, "/")
payment_ns.add_resource(PaymentResourceID, "/<int:id>")

lead_ns.add_resource(LeadResource, "/")

notification_ns.add_resource(NotificationResource, "/")

api.add_namespace(establishment_ns)
api.add_namespace(user_ns)
api.add_namespace(product_ns)
api.add_namespace(client_ns)
api.add_namespace(order_ns)
api.add_namespace(payment_ns)
api.add_namespace(lead_ns)
api.add_namespace(notification_ns)


def init_app(app):
    app.register_blueprint(bp)
    api.add_namespace(establishment_ns)
    api.add_namespace(user_ns)
    api.add_namespace(product_ns)
    api.add_namespace(client_ns)
    api.add_namespace(order_ns)
    api.add_namespace(payment_ns)
    api.add_namespace(lead_ns)
    api.add_namespace(notification_ns)
