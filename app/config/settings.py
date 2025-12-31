# app/config/settings.py

from datetime import timedelta

"""
WHY CONFIG FILE?
----------------
Industry rule:
Configuration ≠ Code

मराठीत:
---------
Password, DB URL, Environment
हे code मध्ये hardcode करायचं नाही
"""

class Config:
    """
    DATABASE URL FORMAT:
    postgresql://username:password@host:port/dbname
    """

    SQLALCHEMY_DATABASE_URI = (
        "postgresql://postgres:Pund%402020@localhost:5432/pythonflaskdb"
    )

    """
    WHY FALSE?
    ----------
    SQLAlchemy changes track करतं
    पण Flask app ला गरज नसते

    मराठीत:
    ----------
    Performance improve करण्यासाठी false
    """
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    """
    JWT SECRET KEY
    --------------
    Used to SIGN JWT tokens

    मराठीत:
    ----------
    ह्या key शिवाय
    token verify होणार नाही
    """
    JWT_SECRET_KEY = "dev-secret-change-later"



    JWT_TOKEN_LOCATION = ["headers", "cookies"]
    JWT_REFRESH_COOKIE_NAME = "refresh_token"
    JWT_COOKIE_SECURE = False      # True in production (HTTPS)
    JWT_COOKIE_SAMESITE = "Strict"
    JWT_COOKIE_CSRF_PROTECT = False

    """
    JWT TOKEN EXPIRY
    ----------------
    Access token किती वेळ valid असेल

    मराठीत:
    ----------
    Token जास्त वेळ valid ठेवणं
    security risk आहे
    """
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
