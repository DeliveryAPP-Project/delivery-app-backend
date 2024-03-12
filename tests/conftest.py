import os

import pytest

from project import create_app_wsgi


@pytest.fixture
def app_testing():
    os.environ['FLASK_ENV'] = 'testing'
    return create_app_wsgi()
