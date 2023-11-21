import jwt
from functools import wraps
from flask import request, jsonify
from jwt import ExpiredSignatureError, InvalidSignatureError
from TaskManagementAPI.configs.env_loader import SECRET_KEY
from TaskManagementAPI.constants.messages import (
    ACCESS_TOKEN_REQUIRED, ACCESS_TOKEN_EXPRIED,INVALID_ACCESS_TOKEN,
    SERVER_ERROR
)


# This method will validate the Authentication.
def required_auth(req_data):
    @wraps(req_data)
    def decorated(*args, **kwargs):
        access_token = request.headers.get('access_token')
        if not access_token:
            return jsonify({'Unsuccessful': ACCESS_TOKEN_REQUIRED}), 401
        try:
            data = jwt.decode(access_token, SECRET_KEY, verify=True, algorithms=['HS256'])
        except ExpiredSignatureError:
            return jsonify({'Unsuccessful': ACCESS_TOKEN_EXPRIED}), 401
        except InvalidSignatureError:
            return jsonify({'Unsuccessful': INVALID_ACCESS_TOKEN}), 401
        except:
            return jsonify({'Unsuccessful': SERVER_ERROR}), 500
        return req_data(data, *args, **kwargs)
    return decorated
