from flask import request

from ..ext.database import db
from ..models.client_model import Client


def get_all_clients():
    return Client.query.all()


def post_client(data_client):
    data_client = request.get_json()
    client = Client(**data_client)
    db.session.add(client)
    db.session.commit()


def get_one_client(id):
    return client if (client := Client.query.get(id)) else None


def update_client(id, updated_data):
    client = get_one_client(id)

    if client is None:
        return {"error": f"Cliente com ID {id} não encontrado"}

    try:
        for key, value in updated_data.items():
            setattr(client, key, value)

        db.session.commit()
        return {"message": f"Cliente com ID {id} atualizado com sucesso!"}

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}


def delete_client(id):
    client = get_one_client(id)

    if client is None:
        return {"error": f"Cliente com ID {id} não encontrado"}

    try:
        db.session.delete(client)
        db.session.commit()
        return {"message": f"CLiente com ID {id} deletado com sucesso."}

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}
