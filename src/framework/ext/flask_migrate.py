from flask_migrate import Migrate

from src.framework.ext.flask_sqlalchemy import db

migrate = Migrate()


def init_app(app, **config):
    migrate.init_app(app=app, db=db, **config)
