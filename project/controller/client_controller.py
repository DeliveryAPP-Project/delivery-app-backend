import json

from flask import abort, request
from flask_restx import Resource

from project.doc_model.doc_models import api, client_model
from project.ext.serializer import ClientSchema
from project.service.client_service import (
    delete_client,
    get_all_clients,
    get_one_client,
    post_client,
    update_client,
)
from project.utils.redis_utils import (
    delete_redis_value,
    get_redis_value,
    set_redis_value,
)

client_schema_list = ClientSchema(many=True)
client_schema = ClientSchema(many=False)


class ClientResource(Resource):
    def get(self):
        key_redis = "clients"
        clients = get_redis_value(key_redis)
        if clients:
            return clients
        clients = get_all_clients()
        clients = client_schema_list.dump(clients)
        set_redis_value(key_redis, json.dumps(clients))
        return clients, 200

    @api.expect(client_model)
    def post(self):
        try:
            client_data = request.json
            post_client(client_data)  # type: ignore
            delete_redis_value("clients")
            return {"message": "Cliente cadastrado com sucesso!"}, 201

        except Exception as e:
            return {"error": str(e)}, 400


class ClientResourceID(Resource):
    def get(self, id: int):
        if client := get_one_client(id):
            return client_schema.dump(client), 200
        else:
            return {"error": f"Cliente com ID {id} não encontrado."}, 404

    @api.expect(client_model)
    def patch(self, id: int):
        try:
            client_data = request.json
            result = update_client(id, client_data)  # type: ignore

            if "error" in result:
                abort(404, message=result["error"])
            delete_redis_value("clients")
            return {"message": result["message"]}, 200

        except Exception as e:
            return {"error": str(e)}, 500

    def delete(self, id: int):
        try:
            result = delete_client(id)

            if "error" in result:
                return {"error": result["error"]}, 404
            delete_redis_value("clients")
            return {"message": result["message"]}, 200

        except Exception as e:
            return {"error": str(e)}, 500
