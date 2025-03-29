from ..ext.database import db


class Establishment(db.Model):
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    official_name: str = db.Column(db.String(45), unique=True, nullable=False)
    fantasy_name: str = db.Column(db.String(45), unique=True, nullable=False)
    cnpj: str = db.Column(db.String(14), unique=True, nullable=False)
    telephone: str = db.Column(db.String(11), unique=True, nullable=False)
    zip_code: str = db.Column(db.String(9), nullable=False)
    state: str = db.Column(db.String(19), nullable=False)
    city: str = db.Column(db.String(30), nullable=False)
    address: str = db.Column(db.String(120), nullable=False)
    complement: str = db.Column(db.String(120), nullable=True)
    products = db.relationship(
        "Product", backref="establishment", lazy=True
    )
