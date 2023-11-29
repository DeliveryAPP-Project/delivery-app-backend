
from project.models.client_model import Client
from project.models.product_model import Product
from project.models.restaurant_model import Restaurant

from ..ext.database import db

order_product_association = db.Table(
    "order_product_association",
    db.Column("order_id", db.Integer, db.ForeignKey("order.id")),
    db.Column("product_id", db.Integer, db.ForeignKey("product.id")),
)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_id = db.Column(db.Integer, db.ForeignKey(Client.id))
    restaurant_id = db.Column(db.Integer, db.ForeignKey(Restaurant.id))
    products = db.relationship(
        "Product", secondary=order_product_association,
        backref=db.backref("orders", lazy="dynamic")
    )

    def __init__(self, client_id, restaurant_id, products=None):
        self.client_id = client_id
        self.restaurant_id = restaurant_id
        self.products = products or []

    def to_dict(self):
        return {
            "id": self.id,
            "client_id": self.client_id,
            "restaurant_id": self.restaurant_id,
            "products": [product.to_dict() for product in self.products]
        }
