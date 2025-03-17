import json
from http import HTTPStatus

from flask import abort, request
from flask_restx import Resource

from project.doc_model.doc_models import api, payment_model
from project.errors.NotFoundErr import NotFoundError
from project.ext.serializer import PaymentSchema
from project.service.payment_service import (
    create_payment,
    get_all_payments,
    get_payment,
    update_payment,
)
from project.utils.redis_utils import (
    delete_redis_value,
    get_redis_value,
    set_redis_value,
)

payment_schema_list = PaymentSchema(many=True)
payment_schema = PaymentSchema(many=False)


class PaymentResource(Resource):
    def get(self):
        key_redis = "payments"
        payments = get_redis_value(key_redis)

        if payments:
            return payments, 200

        payments = get_all_payments()
        payments = payment_schema_list.dump(payments)

        set_redis_value(key_redis, json.dumps(payments))

        return payments, 200

    @api.expect(payment_model)
    def post(self):
        try:
            payment_data = request.json

            if not payment_data:
                return abort(
                    HTTPStatus.BAD_REQUEST, description="Payment data is required"
                )

            create_payment(payment_data)
            delete_redis_value("payments")
            return {"message": "Pagamento cadastrado com sucesso!"}, 201

        except NotFoundError as e:
            abort(HTTPStatus.NOT_FOUND, description=str(e.message))

        except ValueError as e:
            abort(HTTPStatus.BAD_REQUEST, description=str(e))

        except Exception as e:
            abort(HTTPStatus.INTERNAL_SERVER_ERROR, description=str(e))


class PaymentResourceID(Resource):
    def get(self, id: int):
        payment = get_payment(id)

        if not payment:
            return abort(
                HTTPStatus.NOT_FOUND,
                description=f"Pagamento com ID {id} não encontrado.",
            )

        return payment_schema.dump(payment), 200

    @api.expect(payment_model)
    def patch(self, id: int):
        try:
            payment_data = request.json
            if not payment_data:
                raise ValueError("Payment data is required")

            payment = update_payment(id, payment_data)

            delete_redis_value("payments")

            return {
                "message": f"Pagamento com ID {payment.id} atualizado com sucesso"
            }, 200

        except NotFoundError as e:
            abort(HTTPStatus.NOT_FOUND, description=str(e.message))

        except Exception as e:
            abort(HTTPStatus.INTERNAL_SERVER_ERROR, description=str(e))
