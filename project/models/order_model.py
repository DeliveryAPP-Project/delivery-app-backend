from datetime import datetime

from project.models.client_model import Client
from project.models.establishment_model import Establishment

from ..ext.database import db

order_product_association = db.Table(
    "order_product_association",
    db.Column("order_id", db.Integer, db.ForeignKey("order.id")),
    db.Column("product_id", db.Integer, db.ForeignKey("product.id")),
)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    client_id = db.Column(db.Integer, db.ForeignKey(Client.id))
    establishment_id = db.Column(db.Integer, db.ForeignKey(Establishment.id))
    total_value = db.Column(db.Float)
    status = db.Column(
        db.Enum(
            "pre_order",
            "confirmed",
            "doing",
            "done",
            "canceled",
            name="order_status",
        ),
        default="pre_order",
    )
    products = db.relationship(
        "Product",
        secondary=order_product_association,
        backref=db.backref("orders", lazy="dynamic"),
    )
    client = db.relationship("Client", lazy=True)
    establishment = db.relationship("Establishment", lazy=True)
    payment = None
