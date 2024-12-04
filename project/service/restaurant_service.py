from flask import request
from datetime import datetime
from ..ext.database import db
from ..models.restaurant_model import Restaurant
from typing import Dict, Optional


def get_all_restaurants() -> list[Restaurant]:
    return Restaurant.query.all()


def post_restaurant(data_restaurant) -> None:
    data_restaurant = request.get_json()
    data_restaurant['horario_funcionamento'] = datetime.strptime(data_restaurant['horario_funcionamento'], '%H:%M:%S').time()
    data_restaurant['horario_fechamento'] = datetime.strptime(data_restaurant['horario_fechamento'], '%H:%M:%S').time()
    restaurant = Restaurant(**data_restaurant)
    db.session.add(restaurant)
    db.session.commit()


def get_one_restaurant(restaurant_id) -> Optional[Dict[str, str]]:
    restaurant = Restaurant.query.get(restaurant_id)

    if restaurant:
        restaurant_data = {
            "id": restaurant.id,
            "name": restaurant.name,
            "description": restaurant.description,
            "classification": restaurant.classification,
            "location": restaurant.location,
            "url_image_logo": restaurant.url_image_logo,
            "url_image_banner": restaurant.url_image_banner,
            "horario_funcionamento": restaurant.horario_funcionamento.strftime("%H:%M:%S"),
            "horario_fechamento": restaurant.horario_fechamento.strftime("%H:%M:%S"),
            "associated_products": [],
        }

        for product in restaurant.products:
            product_data = {
                "id": product.id,
                "name": product.name,
                "value": product.value,
                "description": product.description,
                "url_image": product.url_image,
                "restaurant_id": product.restaurant_id,
            }
            restaurant_data["associated_products"].append(product_data)

        return restaurant_data
    else:
        return None


def update_restaurant(id, updated_data) -> Dict[str, str]:
    restaurant = get_one_restaurant(id)

    if restaurant is None:
        return {"error": f"Restaurante com ID {id} não encontrado"}

    try:
        for key, value in updated_data.items():
            restaurant[key] = value

        db.session.commit()
        return {"message": f"Restaurante com ID {id} atualizado com sucesso!"}

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}


def delete_restaurant(id) -> Dict[str, str]:
    restaurant = Restaurant.query.get(id)

    if restaurant is None:
        return {"error": f"Restaurante com ID {id} não encontrado"}

    try:
        db.session.delete(restaurant)
        db.session.commit()
        return {"message": f"Restaurante com ID {id} deletado com sucesso."}

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}
