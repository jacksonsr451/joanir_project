from src.framework.ext.flask_sqlalchemy import db


class Users(db.Model):
    id = db.Column(db.String(), primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
