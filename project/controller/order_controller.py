from http.client import HTTPException

from flask import request
from flask_restx import Resource
from project.ext.serializer import OrderSchema
from project.service.order_service import (delete_one_order, get_all_orders,
                                           get_one_order, post_order,
                                           update_order)

order_schema_list = OrderSchema(many=True)
order_schema = OrderSchema(many=False)


class OrderResource(Resource):

    def get(self):
        orders = get_all_orders()
        return order_schema_list.dump(orders), 200


    def post(self):
        try:
            order_data = request.json
            post_order(order_data)
            return {"message": "Pedido criado com sucesso!"}, 201
        
        except Exception as e:
            return {"error": str(e)}, 400


class OrderResourceID(Resource):

    def get(self, id):
        if order := get_one_order(id):
            return order_schema.dump(order), 200  # type: ignore
        else:
            return {"error": f"Ordem com ID {id} não encontrado."}, 404
        

    def patch(self, id):
        try:
            order_data = request.json
            result = update_order(id, order_data)
            return {"message": result["message"]}, 200

        except HTTPException as e:
            return {"error": str(e)}, e.code  # type: ignore

        except Exception as e:
            return {"error": str(e)}, 500


    def delete(self, id):
        try:
            result = delete_one_order(id)

            if "error" in result:
                return {"error": result["error"]}, 404
            return {"message": result["message"]}, 200

        except Exception as e:
            return {"error": str(e)}, 500