from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity
)

from app.services.user_service import create_user, verify_password
from app.models import User


auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

"""
AUTH ROUTES
-----------
User related APIs (register, login, refresh)

मराठीत:
----------
Authentication संबंधित
routes इथे असतात
"""


# -------------------- REGISTER --------------------
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is missing"}), 400

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({"error": "User already exists"}), 409

    user = create_user(email=email, password=password)

    return jsonify({
        "message": "User registered successfully",
        "user": {
            "id": user.id,
            "email": user.email
        }
    }), 201


# -------------------- LOGIN --------------------
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is missing"}), 400

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    user = User.query.filter_by(email=email).first()
    if not user or not verify_password(user, password):
        return jsonify({"error": "Invalid credentials"}), 401

    # 🔐 Generate tokens
    access_token = create_access_token(identity=str(user.id))
    refresh_token = create_refresh_token(identity=str(user.id))

    response = make_response(jsonify({
        "message": "Login successful",
        "access_token": access_token,
        "user": {
            "id": user.id,
            "email": user.email
        }
    }))

    # 🔒 HTTP-only refresh token cookie
    response.set_cookie(
        "refresh_token",
        refresh_token,
        httponly=True,
        secure=False,          # True in production (HTTPS)
        samesite="Strict",
        max_age=7 * 24 * 60 * 60
    )

    return response, 200


# -------------------- REFRESH --------------------
@auth_bp.route("/refresh", methods=["POST"])
@jwt_required(refresh=True, locations=["cookies"])
def refresh():
    """
    REFRESH ACCESS TOKEN

    मराठीत:
    ----------
    refresh token cookie मधून येतो
    नवीन access token देतो
    """

    user_id = get_jwt_identity()

    new_access_token = create_access_token(identity=user_id)

    return jsonify({
        "access_token": new_access_token
    }), 200
