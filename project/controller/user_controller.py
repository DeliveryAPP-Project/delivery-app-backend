# from project.models.mock_data import mock_users
from flask import abort, request
from flask_restx import Resource

from project.service.user_service import (delete_user, get_all_users,
                                          get_one_user, post_user, update_user)


class UserResource(Resource):
    def get(self):
        users = get_all_users()
        return {"users": users}, 200

    def post(self):
        try:
            user_data = request.json
            post_user(user_data)
            return {"message": "Usuário cadastrado com sucesso!"}, 201
        except Exception as e:
            return {"error": str(e)}, 400


class UserResourceID(Resource):
    def get(self, id):
        if user := get_one_user(id):
            return {"user": user.to_dict()}, 200  # type: ignore
        else:
            return {"error": f"Usuário com ID {id} não encontrado."}, 404

    def patch(self, id):
        try:
            user_data = request.json
            result = update_user(id, user_data)

            if "error" in result:
                abort(404, message=result["error"])

            return {"message": result["message"]}, 200

        except Exception as e:
            return {"error": str(e)}, 500

    def delete(self, id):
        try:
            result = delete_user(id)

            if "error" in result:
                return {"error": result["error"]}, 404

            return {"message": result["message"]}, 200

        except Exception as e:
            return {"error": str(e)}, 500
