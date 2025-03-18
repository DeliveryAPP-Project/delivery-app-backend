from datetime import datetime

from ..ext.database import db


class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    total_value = db.Column(db.Float)
    type = db.Column(db.Enum("Dinheiro", "Pix", name="payment_type"), nullable=False)
    status = db.Column(
        db.Enum(
            "pending",
            "approved",
            "authorized",
            "in_process",
            "in_mediation",
            "rejected",
            "cancelled",
            "refunded",
            "charged_back",
            name="payment_status",
        ),
        default="pending",
    )
    qr_code = db.Column(db.String, nullable=True, default=None)
    qr_code_base64 = db.Column(db.Text, nullable=True, default=None)
    ticket_url = db.Column(db.String, nullable=True, default=None)
    mercadopago_id = db.Column(db.String, nullable=True, default=None)
    date_of_expiration = db.Column(db.DateTime, nullable=True, default=None)
    order_id = db.Column(db.ForeignKey("order.id"))
    order = db.relationship("Order", back_populates="payment")
