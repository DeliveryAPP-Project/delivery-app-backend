# from ..models.order_model import Order
from ..models.mock_data import mock_orders


def get_all_orders():
    # return Order.query.all()
    return mock_orders
