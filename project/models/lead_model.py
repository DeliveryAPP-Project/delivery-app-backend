from datetime import datetime

from sqlalchemy import func

from ..ext.database import db


class Lead(db.Model):
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at: datetime = db.Column(db.DateTime, default=func.now())
    email: str = db.Column(db.String(120), unique=True, nullable=False, index=True)
