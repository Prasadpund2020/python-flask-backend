from flask import Blueprint

# Blueprint object
health_bp = Blueprint("health", __name__)

@health_bp.route("/")
def root():
    """
    ROOT ROUTE → "/"

    WHY THIS EXISTS?
    ----------------
    To verify backend is running

    मराठीत:
    ----------
    Server चालू आहे का
    हे check करण्यासाठी
    """
    return {
        "status": "UP",
        "message": "Flask backend is running"
    }
