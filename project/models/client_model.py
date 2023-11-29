from ..ext.database import db


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_name = db.Column(db.String(80), nullable=False)
    client_cellphone = db.Column(db.String(14), nullable=False)
    client_address = db.Column(db.String(120), nullable=False)
    client_address_number = db.Column(db.Integer, nullable=False)
    client_address_complement = db.Column(db.String(120), nullable=False)
    client_address_neighborhood = db.Column(db.String(40), nullable=True)
    client_zip_code = db.Column(db.String(8), nullable=False)

    def __init__(self,
                 client_name,
                 client_cellphone,
                 client_address,
                 client_address_number,
                 client_address_complement,
                 client_address_neighborhood,
                 client_zip_code):

        self.client_name = client_name
        self.client_cellphone = client_cellphone
        self.client_address = client_address
        self.client_address_number = client_address_number
        self.client_address_complement = client_address_complement
        self.client_address_neighborhood = client_address_neighborhood
        self.client_zip_code = client_zip_code

    def __str__(self):
        return self.client_name

    def to_dict(self):
        return {
            "id": self.id,
            "client_name": self.client_name,
            "client_cellphone": self.client_cellphone,
            "client_address": self.client_address,
            "client_address_number": self.client_address_number,
            "client_address_complement": self.client_address_complement,
            "client_address_neighborhood": self.client_address_neighborhood,
            "client_zip_code": self.client_zip_code
        }
