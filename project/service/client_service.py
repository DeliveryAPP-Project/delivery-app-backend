# from ..models.client_model import Client
from ..models.mock_data import mock_clients


def get_all_clients():
    # return Client.query.all()
    return mock_clients
