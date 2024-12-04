from datetime import datetime

from project.models.client_model import Client
from project.models.restaurant_model import Restaurant
from ..ext.database import db

order_product_association = db.Table(
    "order_product_association",
    db.Column("order_id", db.Integer, db.ForeignKey("order.id")),
    db.Column("product_id", db.Integer, db.ForeignKey("product.id")),
)


class Order(db.Model):
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at: datetime = db.Column(db.DateTime, default=datetime.now)
    client_id: int = db.Column(db.Integer, db.ForeignKey(Client.id))
    restaurant_id: int = db.Column(db.Integer, db.ForeignKey(Restaurant.id))
    total_value: float = db.Column(db.Float)
    products = db.relationship(
        "Product",
        secondary=order_product_association,
        backref=db.backref("orders", lazy="dynamic"),
    )
    client = db.relationship("Client", lazy=True)
    restaurant = db.relationship("Restaurant", lazy=True)
