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


class NotificationResource(Resource):
    @api.expect(notification_model)
    @api.response(200, "Pagamento atualizado com sucesso")
    @api.response(400, "Requisição inválida ou erro interno")
    @api.response(404, "Pagamento não encontrado")
    @api.doc(
        description="""
        Endpoint para processar notificações do MercadoPago sobre atualizações de pagamento.

        Recebe um payload no formato específico do MercadoPago e atualiza o status do pagamento correspondente.
        """,
        params={},
        body=notification_model,
    )
    def post(self):
        """
        Processa notificações de atualização de pagamento.

        Exemplo de requisição (JSON):
        {
            "action": "payment.updated",
            "api_version": "v1",
            "data": {"id": "12345"},
            "date_created": "2023-01-01T00:00:00Z",
            "id": "12345",
            "live_mode": false,
            "type": "payment",
            "user_id": 123456
        }

        Respostas:
        - 200: Pagamento atualizado (ex: {"message": "Pagamento atualizado com sucesso"}),
        - 400: Erro na requisição (ex: JSON inválido, dados incorretos),
        - 404: Pagamento não encontrado no sistema
        """

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
