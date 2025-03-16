from dynaconf import settings

from mercadopago import SDK

ACCESS_TOKEN = settings["MERCADO_VENDOR_TOKEN"]


sdk = SDK(
    access_token=ACCESS_TOKEN,
)


def get_mercado_pago_sdk():
    return sdk
