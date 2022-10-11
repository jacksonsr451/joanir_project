from flask import Flask
from flask_admin import Admin


admin = Admin()


def init_app(app: Flask, **config):
    admin.name = app.config.get('TITLE')
    admin.template_mode = "bootstrap3"
    admin.init_app(app=app, **config)
    return app
