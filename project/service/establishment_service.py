from flask import request
from sqlalchemy.exc import IntegrityError

from ..ext.database import db
from ..models.establishment_model import Establishment


def get_all_establishments():
    return Establishment.query.all()


def post_establishment(data_establishment: dict):
    try:
        data_establishment = request.get_json()
        establishment = Establishment(**data_establishment)
        db.session.add(establishment)
        db.session.commit()
        return {"message": "Estabelecimento cadastrado com sucesso!"}, 201

    except IntegrityError:
        db.session.rollback()
        return {"error": "Estabelecimento já existe ou há dados duplicados."}, 400
    
    except Exception as e:
        db.session.rollback()
        return {"error": f"Erro ao cadastrar estabelecimento: {str(e)}"}, 500


def get_one_establishment_by_id(establishment_id: int):
    return Establishment.query.get(establishment_id)


def get_one_establishment_with_products(establishment_id: int):
    establishment = Establishment.query.get(establishment_id)
    
    if establishment:
        establishment_data = {
            "id": establishment.id,
            "name": establishment.name,
            "description": establishment.description,
            "classification": establishment.classification,
            "location": establishment.location,
            "url_image_logo": establishment.url_image_logo,
            "url_image_banner": establishment.url_image_banner,
            "telephone": establishment.telephone,
            "associated_products": []
        }

        for product in establishment.products:
            product_data = {
                "id": product.id,
                "name": product.name,
                "value": product.value,
                "description": product.description,
                "url_image": product.url_image,
                "establishment_id": product.establishment_id
            }
            establishment_data["associated_products"].append(product_data)

        return establishment_data
    else:
        return None


def update_establishment(id: int, updated_data: dict):
    establishment = get_one_establishment_by_id(id)

    if establishment is None:
        return {"error": f"Estabelecimento com ID {id} não encontrado"}

    try:
        for key, value in updated_data.items():
            setattr(establishment, key, value)

        db.session.commit()
        return {"message": f"Estabelecimento com ID {id} atualizado com sucesso!"}

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}


def delete_establishment(id: int):
    establishment = get_one_establishment_by_id(id)
    
    if establishment is None:
        return {"error": f"Estabelecimento com ID {id} não encontrado"}

    try:
        db.session.delete(establishment)
        db.session.commit()
        return {"message": f"Estabelecimento com ID {id} deletado com sucesso."}

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}