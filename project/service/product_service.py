# from ..models.product_model import Product
from ..models.mock_data import mock_products


def get_all_products():
    # return Product.query.all()
    return mock_products
