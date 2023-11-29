from flask_restx import Resource

from project.models.mock_data import mock_orders

# from project.service.order_service import get_all_orders


class OrderResource(Resource):

    def get(self):
        # orders = get_all_orders()
        orders = mock_orders
        return orders, 200
