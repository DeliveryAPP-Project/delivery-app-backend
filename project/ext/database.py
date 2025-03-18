from contextlib import contextmanager

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


@contextmanager
def get_database_session():
    session = db.session()
    yield session

    session.close()


def init_app(app):
    db.init_app(app)
    Migrate(app, db)
