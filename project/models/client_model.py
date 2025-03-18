from ..ext.database import db


class Client(db.Model):
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(80), nullable=False)
    cellphone: str = db.Column(db.String(11), nullable=False)
    cpf: str = db.Column(db.String(11), nullable=False)
    address: str = db.Column(db.String(120), nullable=False)
    address_number: int = db.Column(db.Integer, nullable=False)
    address_complement: str = db.Column(db.String(120), nullable=False)
    address_neighborhood: str = db.Column(db.String(40), nullable=True)
    zip_code: str = db.Column(db.String(8), nullable=False)
    email: str = db.Column(db.String(120), nullable=False, index=True)
