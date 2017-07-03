"""
factory for use with flask blueprints
"""
import os
from flask import Flask
from flask_migrate import Migrate

from perfsonar_data.model import db

_DEFAULT_DSN = "sqlite:////tmp/perfsonar-data.sqlite"


def create_app(dsn=_DEFAULT_DSN):
    app = Flask("perfsonar_data")
    app.config["SQLALCHEMY_DATABASE_URI"] = dsn
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # this is actually the default, but maybe worth being explicit
    ALEMBIC_MIGRATION_DIRECTORY = os.path.join(
        os.path.dirname(__file__),
        "migrations")

    db.init_app(app)

    Migrate(app, db, directory=ALEMBIC_MIGRATION_DIRECTORY)
    # migrate = Migrate(app, db, directory=ALEMBIC_MIGRATION_DIRECTORY)

    # cf. http://flask.pocoo.org/docs/0.10/patterns/appfactories/
    from perfsonar_data.server import server
    app.register_blueprint(server)

    return app