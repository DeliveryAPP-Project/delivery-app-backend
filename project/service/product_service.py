from flask import request
from ..ext.database import db
from typing import Dict, Optional
from ..models.product_model import Product


def get_all_products() -> list[Product]:
    return Product.query.all()


def post_product(product_data) -> None:
    product_data = request.get_json()
    product = Product(**product_data)
    db.session.add(product)
    db.session.commit()


def get_one_product(product_id) -> Optional[Product]:
    return product if (product := Product.query.get(product_id)) else None


def update_product(id, updated_data) -> Dict[str, str]:
    product = get_one_product(id)
    if product is None:
        return {"error": f"Produto com ID {id} não encontrado"}

    try:
        for key, value in updated_data.items():
            setattr(product, key, value)

        db.session.commit()
        return {"message": f"Produto com ID {id} atualizado com sucesso!"}

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}


def delete_product(id) -> Dict[str, str]:
    product = get_one_product(id)
    if product is None:
        return {"error": f"Produto com ID {id} não encontrado"}

    try:
        db.session.delete(product)
        db.session.commit()
        return {"message": f"Produto com ID {id} deletado com sucesso."}

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}
