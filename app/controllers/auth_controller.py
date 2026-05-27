from flask import jsonify, request

from app.services.auth_service import AuthService

from app.middleware.auth_middleware import (
    token_required
)


class AuthController:

    @staticmethod
    def register():

        data = request.get_json()

        user_id = AuthService.register(data)

        return jsonify({
            "success": True,
            "message": "Register success",
            "user_id": user_id
        }), 201

    @staticmethod
    def login():

        data = request.get_json()

        result = AuthService.login(data)

        if not result:
            return jsonify({
                "success": False,
                "message": "Invalid email or password"
            }), 401

        return jsonify({
            "success": True,
            "data": result
        }), 200

    @staticmethod
    @token_required
    def profile(current_user_id):

        profile = AuthService.get_profile(
            current_user_id
        )

        return jsonify({
            "success": True,
            "data": profile
        }), 200