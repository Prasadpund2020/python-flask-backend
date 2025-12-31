from flask import Flask
from app.config.settings import Config
from app.extensions.db import db
from app.routes import health_bp   # 👈 routes, not routers
from app import models  # 👈 THIS IS THE KEY LINE
from app.routes import auth_bp
from app.extensions.jwt import jwt 



def create_app():
    app = Flask(__name__)

    # Load config
    app.config.from_object("app.config.settings.Config")

    # Init DB
    db.init_app(app)
    jwt.init_app(app)

    """
    THIS LINE IS THE KEY
    --------------------
    Without this → 404 for all routes

    मराठीत:
    ----------
    route register केल्याशिवाय
    Flask ला route माहिती नसतो
    """


    print("JWT SECRET:", app.config.get("JWT_SECRET_KEY"))
    print("JWT EXP:", app.config.get("JWT_ACCESS_TOKEN_EXPIRES"))



    app.register_blueprint(health_bp)
    app.register_blueprint(auth_bp)

    return app
