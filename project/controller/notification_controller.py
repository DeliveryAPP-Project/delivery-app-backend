from flask import request
from flask_restx import Resource

from project.doc_model.doc_models import api, notification_model
from project.ext.payment_gateways.mercadopago.schema import NotificationPayload
from project.ext.serializer import PaymentSchema
from project.service.payment_service import (
    get_payment_by_mercadopago_id,
    update_payment,
)

from ..ext.payment_gateways.mercadopago.payment import get_payment as get_mp_payment

payment_schema = PaymentSchema(many=False)


# {
#     "action": "payment.updated",
#     "api_version": "v1",
#     "data": {"id": "1334092911"},
#     "date_created": "2021-11-01T02:02:02Z",
#     "id": "1334092911",
#     "live_mode": false,
#     "type": "payment",
#     "user_id": 221150409,
# }


class NotificationResource(Resource):
    @api.expect(notification_model)
    def post(self):
        try:
            if not request.json:
                return {"error": "Invalid request json"}, 400

            notification_data: NotificationPayload = request.json

            if not isinstance(notification_data, dict):
                return {"error": "Invalid input data type"}, 400

            if notification_data["action"] == "payment.updated":
                mercadopago_id = notification_data["id"]

                existing_payment = get_payment_by_mercadopago_id(id=int(mercadopago_id))

                if not existing_payment:
                    return {
                        "error": "Nenhum pagamento encontrado para essa notificação!"
                    }, 404

                mp_payment = get_mp_payment(id=int(mercadopago_id))
                actual_status = mp_payment["response"]["status"]

                updated_payment = update_payment(
                    id=existing_payment.id,
                    updated_data={"status": actual_status},
                )

                if not updated_payment:
                    return {"error": "Pagamento não atualizado"}, 400

                return {"messaage": "Pagaamento atualizado com sucesso"}, 200

        except Exception as e:
            return {"error": str(e)}, 400
