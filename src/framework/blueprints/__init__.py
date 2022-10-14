from flask import Blueprint, Flask

from src.framework.blueprints.web import home_controller

blueprint = Blueprint(
    '/', __name__, static_folder='../statics', template_folder='../templates'
)


def init_app(app, **config):
    home_controller.init_controller(blueprint)
    app.register_blueprint(blueprint)
