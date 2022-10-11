from src.framework.admin.auth import UserAdmin
from src.framework.ext.flask_admin import admin
from src.framework.ext.flask_sqlalchemy import db
from src.framework.models.users import Users


def init_app(app, **config):
    admin.add_view(UserAdmin(Users, db.session))
