import bcrypt
import jwt
import datetime

from app.repositories.auth_repository import (
    AuthRepository
)

SECRET_KEY = "simpleapps-secret-key"


class AuthService:

    @staticmethod
    def register(data):

        hashed_password = bcrypt.hashpw(
            data["password"].encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

        user_id = AuthRepository.create_user(
            data["full_name"],
            data["email"],
            hashed_password
        )

        return user_id

    @staticmethod
    def login(data):

        user = AuthRepository.find_user_by_email(
            data["email"]
        )

        if not user:
            return None

        password_valid = bcrypt.checkpw(
            data["password"].encode("utf-8"),
            user[3].encode("utf-8")
        )

        if not password_valid:
            return None

        token = jwt.encode(
            {
                "user_id": user[0],
                "exp": datetime.datetime.utcnow()
                + datetime.timedelta(hours=12)
            },
            SECRET_KEY,
            algorithm="HS256"
        )

        return {
            "token": token,
            "user": {
                "id": user[0],
                "full_name": user[1],
                "email": user[2]
            }
        }

    @staticmethod
    def get_profile(user_id):

        user = AuthRepository.find_user_by_id(
            user_id
        )

        if not user:
            return None

        return {
            "id": user[0],
            "full_name": user[1],
            "email": user[2],
            "created_at": str(user[3])
        }