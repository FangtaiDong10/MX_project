from .model import User
import functools

from flask_jwt_extended import jwt_required
from flask_jwt_extended import current_user


def permission_required(permission=None):
    def wrapper(func):
        @jwt_required()
        @functools.wraps(func)
        def decorator(*arg, **kwargs):
            if current_user._cls == "User.Admin":
                if permission is None or permission in current_user.permissions:
                    return func(*arg, **kwargs)
                else:
                    return {"message": f"Permission '{permission}' is required"}
            return {
                "message": "Permission denied",
            }, 403

        return decorator

    return wrapper


def register_user_lookup(jwt):
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]

        return User.objects(username=identity).first_or_404(message="User not found")

    jwt.user_lookup_loader(user_lookup_callback)
