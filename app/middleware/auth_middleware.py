import jwt

from functools import wraps
from flask import request, jsonify

SECRET_KEY = "simpleapps-secret-key"


def token_required(f):

    @wraps(f)
    def decorated(*args, **kwargs):

        token = None

        if "Authorization" in request.headers:

            bearer = request.headers["Authorization"]
            token = bearer.replace("Bearer ", "")

        if not token:
            return jsonify({
                "success": False,
                "message": "Token is missing"
            }), 401

        try:

            data = jwt.decode(
                token,
                SECRET_KEY,
                algorithms=["HS256"]
            )

            current_user_id = data["user_id"]

        except Exception:
            return jsonify({
                "success": False,
                "message": "Invalid token"
            }), 401

        return f(current_user_id, *args, **kwargs)

    return decorated