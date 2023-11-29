from flask_restx import Resource

from project.models.mock_data import mock_products

# from project.service.product_service import get_all_products


class ProductResource(Resource):

    def get(self):
        # products = get_all_products()
        products = mock_products
        return products, 200
