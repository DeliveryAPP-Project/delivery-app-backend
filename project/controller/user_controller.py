from flask_restx import Resource

# from project.service.user_service import get_all_users
from project.models.mock_data import mock_users


class UserResource(Resource):

    def get(self):
        # users = get_all_users()
        users = mock_users
        return users, 200
