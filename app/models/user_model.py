from app.extensions.db import db

class User(db.Model):
    """
    USER TABLE DEFINITION

    मराठीत:
    ----------
    User म्हणजे database मधील table
    इथे फक्त columns define करायचे
    """

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(255), unique=True, nullable=False)

    password_hash = db.Column(db.String(255), nullable=False)

    is_active = db.Column(db.Boolean, default=True)
