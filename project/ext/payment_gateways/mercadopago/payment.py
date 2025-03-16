from project.ext.payment_gateways.mercadopago.main import get_mercado_pago_sdk
from project.ext.payment_gateways.mercadopago.schema import (
    CreatePaymentSdkResult,
    GetPaymentSdkResult,
    PaymentPayload,
    SearshPaymentSdkResult,
)

sdk = get_mercado_pago_sdk()
payment = sdk.payment()


def create_payment(payload: PaymentPayload):
    sdkResult: CreatePaymentSdkResult = payment.create(payment_object=payload)

    return sdkResult


def list_payments():
    sdkResult: SearshPaymentSdkResult = payment.search()

    return sdkResult


def get_payment(id: int):
    sdkResult: GetPaymentSdkResult = payment.get(payment_id=id)

    return sdkResult


def update_payment(id: int, update_data: dict):
    sdkResult = payment.update(payment_id=id, payment_object=update_data)

    return sdkResult
