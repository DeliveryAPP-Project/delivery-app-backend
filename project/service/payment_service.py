# type: ignore

import logging
from http import HTTPStatus
from typing import TypedDict

from dynaconf import settings

from project.errors.NotFoundErr import NotFoundError
from project.ext.database import get_database_session
from project.ext.payment_gateways.mercadopago.payment import (
    create_payment as mp_create_payment,
)
from project.ext.payment_gateways.mercadopago.schema import (
    CreatePaymentSdkResult,
    PaymentPayload,
)
from project.models.order_model import Order
from project.models.payment_model import Payment

notification_url = settings["NOTIFICATION_URL"]


class CreatePaymentDTO(TypedDict):
    order_id: str
    payment_type: str


class UpdatePaymentDTO(TypedDict):
    status: str


def get_payment(payment_id: int):
    return payment if (payment := Payment.query.get(payment_id)) else None


def get_payment_by_mercadopago_id(id: int):
    existing_payment = Payment.query.filter_by(mercadopago_id=id).first()

    return existing_payment


def get_all_payments():
    return Payment.query.all()


def create_payment(payment_data: CreatePaymentDTO):
    existing_order = Order.query.get(payment_data["order_id"])

    if not existing_order:
        raise NotFoundError(f"Pedido com o ID {payment_data['order_id']}")

    created_payment: list[Payment] = []

    if payment_data["payment_type"] == "Pix":
        payload: PaymentPayload = {
            "payer": {
                "email": existing_order.client.email,
                "first_name": existing_order.client.name,
            },
            "installments": 1,
            "payment_method_id": "pix",
            "transaction_amount": existing_order.total_value,
        }

        if notification_url:
            payload["notification_url"] = notification_url  # type: ignore

        sdkResponse: CreatePaymentSdkResult = mp_create_payment(payload)

        if sdkResponse["status"] not in [HTTPStatus.OK, HTTPStatus.CREATED]:
            raise Exception(
                f"Mercado Pago Sdk Error: Não foi possível criar o Pagamento, \nstatus: {sdkResponse['status']}\nresponse: \n{sdkResponse['response']}"
            )

        transaction_data = sdkResponse["response"]["point_of_interaction"][
            "transaction_data"
        ]

        new_payment = Payment(
            order_id=existing_order.id,
            total_value=existing_order.total_value,
            type=payment_data["payment_type"],
            qr_code=transaction_data["qr_code"],
            qr_code_base64=transaction_data["qr_code_base64"],
            ticket_url=transaction_data["ticket_url"],
            mercadopago_id=sdkResponse["response"]["id"],
            date_of_expiration=sdkResponse["response"]["date_of_expiration"],
        )
        created_payment.append(new_payment)

    if payment_data["payment_type"] == "Dinheiro":
        new_payment = Payment(
            order_id=existing_order.id,
            total_value=existing_order.total_value,
            type=payment_data["payment_type"],
        )
        created_payment.append(new_payment)

    with get_database_session() as db_session:
        try:
            payment = created_payment[0]
            db_session.add(payment)
            db_session.commit()

            result = {
                "payment_id": payment.id,
                "transaction_data": {
                    "qr_code": payment.qr_code,
                    "qr_code_base64": payment.qr_code_base64,
                    "ticket_url": payment.ticket_url,
                },
            }

            return result

        except Exception as e:
            logging.error(f"Erro ao criar pedido: {e}")
            db_session.rollback()
            raise e


def update_payment(id: int, updated_data: UpdatePaymentDTO):
    payment: Payment | None = get_payment(id)

    if payment is None:
        raise NotFoundError(f"Pagamento com ID {id} não encontrado")

    payment.status = updated_data["status"]

    with get_database_session() as db_session:
        try:
            db_session.commit()
            db_session.refresh(payment)
            return payment

        except Exception as e:
            db_session.rollback()
            raise e
