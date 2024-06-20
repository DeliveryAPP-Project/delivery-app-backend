from flask import request

from ..ext.database import db
from ..models.restaurant_model import Restaurant


def get_all_restaurants():
    return Restaurant.query.all()


def post_restaurant(data_restaurant):
    data_restaurant = request.get_json()
    restaurant = Restaurant(**data_restaurant)
    db.session.add(restaurant)
    db.session.commit()


def get_one_restaurant(restaurant_id):
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


def update_restaurant(id, updated_data):
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


def delete_restaurant(id):
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
