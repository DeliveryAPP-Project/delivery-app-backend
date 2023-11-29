# from ..models.user_model import User
from ..models.mock_data import mock_users


def get_all_users():
    # return User.query.all()
    return mock_users
