from flask import Blueprint, request, jsonify
from app.services.user_service import create_user
from app.models import User

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

"""
AUTH ROUTES
-----------
User related APIs (register, login)

मराठीत:
----------
Authentication संबंधित
routes इथे असतात
"""

@auth_bp.route("/register", methods=["POST"])
def register():
    """
    USER REGISTRATION API

    URL: POST /auth/register

    मराठीत:
    ----------
    नवीन user create करण्यासाठी
    हा API वापरतो
    """

    data = request.get_json()

    # 1️⃣ Basic validation
    if not data:
        return jsonify({"error": "Request body is missing"}), 400

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({
            "error": "Email and password are required"
        }), 400

    # 2️⃣ Check if user already exists
    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        return jsonify({
            "error": "User already exists"
        }), 409

    # 3️⃣ Create user (password hashing happens in service)
    user = create_user(email=email, password=password)

    # 4️⃣ Safe response (NEVER return password)
    return jsonify({
        "message": "User registered successfully",
        "user": {
            "id": user.id,
            "email": user.email
        }
    }), 201
