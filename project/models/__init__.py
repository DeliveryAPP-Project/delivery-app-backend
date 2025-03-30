from project.models import (
    client_model,
    establishment_model,
    order_model,
    payment_model,
    product_model,
    user_model,
)

from ..ext.database import db

order_model.Order.payment = db.relationship("Payment", back_populates="order")  # type: ignore


__all__ = [
    "client_model",
    "order_model",
    "payment_model",
    "product_model",
    "establishment_model",
    "user_model",
]
