from ..ext.database import db


class Client(db.Model):
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_name: str = db.Column(db.String(80), nullable=False)
    client_cellphone: str = db.Column(db.String(11), nullable=False)
    client_address: str = db.Column(db.String(120), nullable=False)
    client_address_number: int = db.Column(db.Integer, nullable=False)
    client_address_complement: str = db.Column(db.String(120), nullable=False)
    client_address_neighborhood: str = db.Column(db.String(40), nullable=True)
    client_zip_code: str = db.Column(db.String(8), nullable=False)