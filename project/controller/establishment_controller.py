import json

from flask import abort, request
from flask_restx import Resource

from project.doc_model.doc_models import api, establishment_model
from project.ext.serializer import EstablishmentSchema
from project.service.establishment_service import (
    delete_establishment,
    get_all_establishments,
    get_one_establishment_with_products,
    post_establishment,
    update_establishment,
)
from project.utils.redis_utils import (
    delete_redis_value,
    get_redis_value,
    set_redis_value,
)

establishment_schema_list = EstablishmentSchema(many=True)
establishment_schema = EstablishmentSchema(many=False)


class EstablishmentResource(Resource):
    def get(self):
        key_redis = "establishment"
        establishments = get_redis_value(key_redis)
        if establishments:
            return establishments
        establishments = get_all_establishments()
        establishments = establishment_schema_list.dump(establishments)
        set_redis_value(key_redis, json.dumps(establishments))
        return establishments, 200

    def post(self):
        try:
            establishment_data = request.json
            response = post_establishment(establishment_data)
            return response
        
        except Exception as e:
            return {"error": str(e)}, 400


class EstablishmentResourceID(Resource):
    def get(self, id: int):
        if establishment := get_one_establishment_with_products(id):
            return establishment  # type: ignore
        else:
            return {"error": f"Estabelecimento com ID {id} não encontrado."}, 404

    @api.expect(establishment_model)
    def patch(self, id: int):
        try:
            establishment_data = request.json
            result = update_establishment(id, establishment_data)  # type: ignore

            if "error" in result:
                abort(404, message=result["error"])
            delete_redis_value("clients")
            return {"message": result["message"]}, 200

        except Exception as e:
            return {"error": str(e)}, 500

    def delete(self, id: int):
        try:
            result = delete_establishment(id)

            if "error" in result:
                return {"error": result["error"]}, 404
            delete_redis_value("establishments")
            return {"message": result["message"]}, 200

        except Exception as e:
            return {"error": str(e)}, 500
