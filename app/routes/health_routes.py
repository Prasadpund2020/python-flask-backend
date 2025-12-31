from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

health_bp = Blueprint("health", __name__)

@health_bp.route("/health", methods=["GET"])
@jwt_required()
def health_check():
    """
    PROTECTED HEALTH CHECK

    मराठीत:
    ----------
    ह्या route ला
    token शिवाय access मिळणार नाही
    """

    user_id = get_jwt_identity()

    return jsonify({
        "status": "ok",
        "message": "JWT is valid",
        "user_id_from_token": user_id
    }), 200
