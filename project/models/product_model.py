from ..ext.database import db

products_establishment = db.Table(
    "products_establishment",
    db.metadata,
    db.Column("product_id", db.Integer, db.ForeignKey("product.id"), primary_key=True),
    db.Column("establishment_id", db.Integer, db.ForeignKey("establishment.id"), primary_key=True),
)


class Product(db.Model):
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(40), nullable=False, unique=False)
    value: float = db.Column(db.Float(precision=6), nullable=False)
    description: str = db.Column(db.String(120), nullable=False)
    url_image: str = db.Column(db.String(800), nullable=True)
    food_type: str = db.Column(db.Enum("Italiana", "Japonesa", "Árabe", "Chinesa", "Brasileira", "Mexicana", "Lanches", "Pizza", "Doces", name="food_type"), nullable=False)
    has_gluten: bool = db.Column(db.Boolean, nullable=False, default=False)
    has_lactose: bool = db.Column(db.Boolean, nullable=False, default=False)
    is_vegan: bool = db.Column(db.Boolean, nullable=False, default=False)
    is_vegetarian: bool = db.Column(db.Boolean, nullable=False, default=False)
    establishment_id: int = db.Column(
        db.Integer, db.ForeignKey("establishment.id"), nullable=False
    )
    associated_establishments = db.relationship(
        "Establishment", secondary=products_establishment, backref="associated_products"
    )