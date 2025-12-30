# app/config/settings.py

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
