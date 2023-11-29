# from ..models.restaurant_model import Restaurant
from ..models.mock_data import mock_restaurants


def get_all_restaurants():
    # return Restaurant.query.all()
    return mock_restaurants
