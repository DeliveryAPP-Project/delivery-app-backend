import json
from flask import abort, request
from flask_restx import Resource
from project.ext.serializer import UserSchema

from project.service.user_service import (
    delete_user,
    get_all_users,
    get_one_user,
    post_user,
    update_user,
)
from project.utils.redis_utils import (
    delete_redis_value,
    get_redis_value,
    set_redis_value,
)

user_schema_list = UserSchema(many=True)
user_schema = UserSchema(many=False)


class UserResource(Resource):
    def get(self):
        key_redis = "users"
        users = get_redis_value(key_redis)
        if users:
            return users
        users = get_all_users()
        users = user_schema_list.dump(users)
        set_redis_value(key_redis, json.dumps(users))
        return users, 200

    def post(self):
        try:
            user_data = request.json
            post_user(user_data)
            delete_redis_value("users")
            return {"message": "Usuário cadastrado com sucesso!"}, 201

        except Exception as e:
            return {"error": str(e)}, 400


class UserResourceID(Resource):
    def get(self, id):
        if user := get_one_user(id):
            return user_schema.dump(user), 200  # type: ignore
        else:
            return {"error": f"Usuário com ID {id} não encontrado."}, 404

    def patch(self, id):
        try:
            user_data = request.json
            result = update_user(id, user_data)

            if "error" in result:
                abort(404, message=result["error"])
            delete_redis_value("clients")
            return {"message": result["message"]}, 200

        except Exception as e:
            return {"error": str(e)}, 500

    def delete(self, id):
        try:
            result = delete_user(id)

            if "error" in result:
                return {"error": result["error"]}, 404
            delete_redis_value("users")
            return {"message": result["message"]}, 200

        except Exception as e:
            return {"error": str(e)}, 500
