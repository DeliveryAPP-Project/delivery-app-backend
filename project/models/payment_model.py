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
    order_id = db.Column(db.ForeignKey("order.id"))
    order = db.relationship("Order", back_populates="payment")
