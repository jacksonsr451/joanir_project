from datetime import datetime

from src.framework.ext.flask_sqlalchemy import db


class Users(db.Model):
    id = db.Column(db.String(), primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    admin = db.Column(db.Boolean(), nullable=True, default=True)
    created_at = db.Column(db.String(), nullable=True, default=datetime.now().strftime('dd%/MM%/YY%'))
    updated_at = db.Column(db.String(), nullable=True, default=datetime.now().strftime('dd%/MM%/YY%'))
