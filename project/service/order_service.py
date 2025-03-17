import logging
from typing import List, TypedDict

from project.errors.NotFoundErr import NotFoundError
from project.ext.database import get_database_session
from project.models.client_model import Client
from project.models.order_model import Order
from project.models.product_model import Product
from project.models.restaurant_model import Restaurant
from project.utils.calculate_total import calculate_total


class CreateOrderDTO(TypedDict):
    client_id: int
    restaurant_id: int
    products: List[int]


def get_all_orders():
    return Order.query.all()


def create_order(order_data: CreateOrderDTO):
    existing_restaurant = Restaurant.query.get(order_data["restaurant_id"])
    existing_client = Client.query.get(order_data["client_id"])

    if not existing_restaurant:
        raise NotFoundError(
            f"Restaurante com ID {order_data['restaurant_id']} não encontrado."
        )

    if not existing_client:
        raise NotFoundError(f"Cliente com ID {order_data['client_id']} não encontrado.")

    existing_products = []

    for id in order_data["products"]:
        product = Product.query.get(id)

        if not product:
            raise NotFoundError(f"Produto com ID {id} não encontrado.")

        existing_products.append(product)

    total = calculate_total(existing_products)

    new_order = Order(
        client_id=existing_client.id,
        restaurant_id=existing_restaurant.id,
        total_value=total,
        products=existing_products,
    )

    with get_database_session() as db_session:
        try:
            db_session.add(new_order)
            db_session.commit()

            return new_order.id

        except Exception as e:
            logging.error(f"Erro ao criar pedido: {e}")
            db_session.rollback()
            raise e


def get_order(order_id: int):
    return order if (order := Order.query.get(order_id)) else None


def update_order(id: int, updated_data: dict):
    order: Order | None = get_order(id)

    if order is None:
        raise NotFoundError(f"Ordem com ID {id} não encontrado")

    existing_products = []

    for id in updated_data["products"]:
        product = Product.query.get(id)
        if not product:
            raise NotFoundError(f"Produto com ID {id} não encontrado")
        existing_products.append(product)

    updated_data["products"] = existing_products

    for k, v in updated_data.items():
        setattr(order, k, v)

    with get_database_session() as db_session:
        try:
            db_session.commit()

        except Exception as e:
            db_session.rollback()
            raise e

        finally:
            return {"message": f"Ordem com ID {id} atualizado com sucesso!"}


def delete_order(id: int):
    order = get_order(id)

    if order is None:
        raise NotFoundError(f"Ordem com ID {id} não encontrado")

    with get_database_session() as db_session:
        try:
            db_session.delete(order)
            db_session.commit()
            return {"message": f"Ordem com ID {id} deletado com sucesso."}

        except Exception as e:
            db_session.rollback()
            raise e
