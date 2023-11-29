from flask_restx import Resource

from project.models.mock_data import mock_restaurants

# from project.service.restaurant_service import get_all_restaurants


class RestaurantResource(Resource):

    def get(self):
        # restaurants = get_all_restaurants()
        restaurants = mock_restaurants
        return restaurants, 200
