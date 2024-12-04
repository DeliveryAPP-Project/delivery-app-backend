from ..ext.database import db
from sqlalchemy.types import Time
from datetime import time

class Restaurant(db.Model):
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(20), unique=True, nullable=False)
    description: str = db.Column(db.String(120), nullable=False)
    classification: float = db.Column(db.Float(precision=3), nullable=False)
    location: str = db.Column(db.String(120), nullable=False)
    url_image_logo: str = db.Column(db.String(), nullable=True)
    url_image_banner: str = db.Column(db.String(), nullable=True)
    horario_funcionamento: time = db.Column(Time(), nullable=True)
    horario_fechamento: time = db.Column(Time(), nullable=True)
    products = db.relationship("Product", backref="restaurant", lazy=True)