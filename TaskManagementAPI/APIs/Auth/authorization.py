import jwt
from functools import wraps
from flask import jsonify, request
from TaskManagementAPI.configs.env_loader import SECRET_KEY
from TaskManagementAPI.constants.messages import (
    ACCESS_TOKEN_REQUIRED, SERVER_ERROR, UNAUTHORIZED
)


# This method will validate the Authorization.
def authorize(roles):
    def authorize_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            access_token = request.headers.get('access_token')
            if not access_token:
                return jsonify({'Unsuccessful': ACCESS_TOKEN_REQUIRED}), 401
            try:
                data = jwt.decode(access_token, SECRET_KEY, verify=True, algorithms=['HS256'])
                user_role = data['Role']
            except Exception as e:
                return jsonify({'Unsuccessful': SERVER_ERROR}), 401
            if user_role == []:
                return wrapper
            if user_role not in roles:
                return jsonify({'Unsuccessful': UNAUTHORIZED}), 401
            return func(*args, **kwargs)
        return wrapper
    return authorize_decorator