from ..ext.database import db

products_restaurants = db.Table(
    "products_restaurants",
    db.Column("product_id", db.Integer, db.ForeignKey("product.id")),
    db.Column("restaurant_id", db.Integer, db.ForeignKey("restaurant.id")),
)


class Product(db.Model):
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(40), nullable=False, unique=False)
    value: float = db.Column(db.Float(precision=6), nullable=False)
    description: str = db.Column(db.String(120), nullable=False)
    url_image: str = db.Column(db.String(), nullable=True)
    restaurant_id: int = db.Column(
        db.Integer, db.ForeignKey("restaurant.id"), nullable=False
    )
    associated_restaurants = db.relationship(
        "Restaurant", secondary=products_restaurants, backref="associated_products"
    )