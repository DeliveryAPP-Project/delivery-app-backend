from typing import Any, Optional, TypedDict


class Adress(TypedDict):
    zip_code: str
    street_name: str
    street_number: str


class Payer(TypedDict):
    id: str
    email: str
    first_name: str
    adress: Adress


class PaymentPayload(TypedDict):
    payer: Payer
    installments: int
    transaction_amount: float
    payment_method_id: str
    date_of_expiration: str
    notification_url: str


class PaymentResponse(TypedDict):
    accounts_info: Optional[Any]
    acquirer_reconciliation: list
    additional_info: dict
    authorization_code: Optional[Any]
    binary_mode: bool
    brand_id: Optional[Any]
    build_version: str
    call_for_authorize_id: Optional[Any]
    callback_url: Optional[Any]
    captured: bool
    card: dict
    charges_details: list
    collector_id: int
    corporation_id: Optional[Any]
    counter_currency: Optional[Any]
    coupon_amount: int
    currency_id: str
    date_approved: Optional[Any]
    date_created: str
    date_last_updated: str
    date_of_expiration: str
    deduction_schema: Optional[Any]
    description: Optional[Any]
    differential_pricing_id: Optional[Any]
    external_reference: Optional[Any]
    fee_details: list
    financing_group: Optional[Any]
    id: int
    installments: int
    integrator_id: Optional[Any]
    issuer_id: str
    live_mode: bool
    marketplace_owner: Optional[Any]
    merchant_account_id: Optional[Any]
    merchant_number: Optional[Any]
    metadata: dict
    money_release_date: Optional[Any]
    money_release_schema: Optional[Any]
    money_release_status: str
    notification_url: Optional[Any]
    operation_type: str
    order: dict
    payer: dict
    payment_method: dict
    payment_method_id: str
    payment_type_id: str
    platform_id: Optional[Any]
    point_of_interaction: dict
    pos_id: Optional[Any]
    processing_mode: str
    refunds: list
    release_info: Optional[Any]
    shipping_amount: int
    sponsor_id: Optional[Any]
    statement_descriptor: Optional[Any]
    status: str
    status_detail: str
    store_id: Optional[Any]
    tags: Optional[Any]
    taxes_amount: int
    transaction_amount: float
    transaction_amount_refunded: int
    transaction_details: dict


class CreatePaymentSdkResult(TypedDict):
    status: int
    response: PaymentResponse


class Paging(TypedDict):
    total: int
    offset: int
    limit: int


class SearchResponse(TypedDict):
    results: list[PaymentResponse]
    paging: Paging


class SearshPaymentSdkResult(TypedDict):
    status: int
    response: SearchResponse


class GetPaymentSdkResult(TypedDict):
    status: int
    response: PaymentResponse


class UpdatePaymentSdkResult:
    status: int
    response: PaymentResponse
