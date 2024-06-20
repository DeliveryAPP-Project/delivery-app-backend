from flask import request
from ..ext.database import db
from ..models.user_model import User
from typing import Dict, Optional


def get_all_users()-> list[User]:
    return User.query.all()


def post_user(user_data)-> None:
    user_data = request.get_json()
    user = User(**user_data)
    db.session.add(user)
    db.session.commit()


def get_one_user(user_id)-> Optional[User]:
    return user if (user := User.query.get(user_id)) else None


def update_user(user_id, updated_data) -> Dict[str, str]:
    user = get_one_user(user_id)

    if user is None:
        return {"error": f"Usuário com ID {user_id} não encontrado"}

    try:
        for key, value in updated_data.items():
            setattr(user, key, value)

        db.session.commit()
        return {"message": f"Usuário com ID {user_id} atualizado com sucesso!"}

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}


def delete_user(id) -> Dict[str, str]:
    user = get_one_user(id)

    if user is None:
        return {"error": f"Usuário com ID {id} não encontrado"}

    try:
        db.session.delete(user)
        db.session.commit()
        return {"message": f"Usuário com ID {id} deletado com sucesso."}

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}
