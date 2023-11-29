from flask_restx import Resource

from project.models.mock_data import mock_clients

# from project.service.client_service import get_all_clients


class ClientResource(Resource):

    def get(self):
        # clients = get_all_clients()
        clients = mock_clients
        return clients, 200
