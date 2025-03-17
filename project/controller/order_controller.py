import json
from http import HTTPStatus

from flask import abort, request
from flask_restx import Resource

from project.doc_model.doc_models import api, order_model
from project.errors.NotFoundErr import NotFoundError
from project.ext.serializer import OrderSchema
from project.service.order_service import (
    create_order,
    delete_order,
    get_all_orders,
    get_order,
    update_order,
)
from project.utils.redis_utils import (
    delete_redis_value,
    get_redis_value,
    set_redis_value,
)

order_schema_list = OrderSchema(many=True)
order_schema = OrderSchema(many=False)


class OrderResource(Resource):
    def get(self):
        key_redis = "orders"
        orders = get_redis_value(key_redis)

        if orders:
            return orders, 200

        orders = get_all_orders()
        orders = order_schema_list.dump(orders)
        set_redis_value(key_redis, json.dumps(orders))

        return orders, 200

    @api.expect(order_model)
    def post(self):
        try:
            order_data = request.json
            if not order_data:
                return abort(HTTPStatus.BAD_REQUEST, "No Payload found!")

            delete_redis_value("order")

            created_id = create_order(order_data=order_data)
            return {
                "message": f"Pedido com ID {created_id} criado com sucesso!"
            }, HTTPStatus.CREATED

        except KeyError as e:
            abort(HTTPStatus.BAD_REQUEST, f"Validation Error: Missing {e}")

        except NotFoundError as e:
            abort(HTTPStatus.NOT_FOUND, e.message)

        except BaseException as e:
            abort(HTTPStatus.BAD_REQUEST, str(e))


class OrderResourceID(Resource):
    def get(self, id: int):
        if order := get_order(id):
            return order_schema.dump(order), 200  # type: ignore
        else:
            return {"error": f"Ordem com ID {id} não encontrado."}, 404

    @api.expect(order_model)
    def patch(self, id: int):
        try:
            order_data = request.json

            if order_data is None:
                return abort(400, "error Dados do pedido não fornecidos.")

            result = update_order(id, order_data)
            delete_redis_value("clients")

            return {"message": result["message"]}, 200

        except NotFoundError as e:
            abort(HTTPStatus.NOT_FOUND, str(e))

        except Exception as e:
            abort(HTTPStatus.INTERNAL_SERVER_ERROR, str(e))

    def delete(self, id: int):
        try:
            result = delete_order(id)

            delete_redis_value("orders")

            return {"message": result["message"]}, 200

        except NotFoundError as e:
            abort(HTTPStatus.NOT_FOUND, str(e))

        except Exception as e:
            abort(HTTPStatus.INTERNAL_SERVER_ERROR, str(e))
