from flask import abort
from typing import Dict, Optional
from project.ext.database import db
from project.models.client_model import Client
from project.models.order_model import Order
from project.models.product_model import Product
from project.models.restaurant_model import Restaurant
from datetime import datetime

from ..utils.twilio_utils import send_whatsapp_message


def get_all_orders() -> list[Order]:
    return Order.query.all()

def post_order(order_data: dict, current_time: Optional[datetime.time] = None) -> tuple[dict, int]:
    if not Client.query.get(order_data["client_id"]):
        abort(404, f"Cliente com ID {order_data['client_id']} não encontrado.")

    restaurant = Restaurant.query.get(order_data["restaurant_id"])
    if not restaurant:
        abort(404, f"Restaurante com ID {order_data['restaurant_id']} não encontrado.")
    
    if "current_time" in order_data:
        current_time = datetime.strptime(order_data["current_time"], "%H:%M:%S").time()
    elif current_time is None:
        current_time = datetime.now().time()
    
    if restaurant.horario_funcionamento and restaurant.horario_fechamento:
        if not (restaurant.horario_funcionamento <= current_time <= restaurant.horario_fechamento):
            abort(403, "O restaurante está fora do horário de funcionamento.")
        
    if not all(Product.query.get(product["product_id"]) for product in order_data["products"]):
        abort(404, "Um ou mais produtos não foram encontrados.")

    products = [
        (Product.query.get(product["product_id"]), product["quantity"])
        for product in order_data["products"]
    ]

    products_value = [product.value * quantity for product, quantity in products]

    new_order = Order(
        client_id=order_data["client_id"],
        restaurant_id=order_data["restaurant_id"],
        products=[product for product, quantity in products],
        total_value=sum(products_value),
    )
    db.session.add(new_order)
    db.session.commit()

    send_whatsapp_message(new_order)

    return {"message": "Pedido cadastrado com sucesso!"}, 201


def get_one_order(order_id) -> Optional[Order]:
    return order if (order := Order.query.get(order_id)) else None


def update_order(id, updated_data) -> Dict[str, str]:
    order = get_one_order(id)

    if order is None:
        return {"error": f"Ordem com ID {id} não encontrado."}

    try:
        for key, value in updated_data.items():
            if key == "products":
                value = [Product.query.get(product_id) for product_id in value]
            setattr(order, key, value)

        db.session.commit()
        return {"message": f"Ordem com ID {id} atualizado com sucesso!"}

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}


def delete_one_order(id) -> Dict[str, str]:
    order = get_one_order(id)

    if order is None:
        return {"error": f"Ordem com ID {id} não encontrado"}

    try:
        db.session.delete(order)
        db.session.commit()
        return {"message": f"Ordem com ID {id} deletado com sucesso."}

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}


def total_order_value(order_data):
    order_data
