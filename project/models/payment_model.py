from sqlalchemy import func

from ..ext.database import db


class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=func.now)
    total_value = db.Column(db.Float)
    type = db.Column(db.Enum("Dinheiro", "Pix", name="payment_type"), nullable=False)
    status = db.Column(
        db.Enum(
            "Aguardando Pagamento",
            "Pagamento Concluido",
            "Expirado",
            "Cancelado",
            name="payment_status",
        ),
        default="Aguardando Pagamento",
    )
    order_id = db.Column(db.ForeignKey("order.id"))
    order = db.relationship("Order", back_populates="payment")
