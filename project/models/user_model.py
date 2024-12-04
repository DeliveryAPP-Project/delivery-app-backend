from ..ext.database import db


class User(db.Model):
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname: str = db.Column(db.String(20), nullable=False)
    lastname: str = db.Column(db.String(20), nullable=False)
    email: str = db.Column(db.String(120), unique=True, nullable=False)
