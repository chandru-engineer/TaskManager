from flask import request
from werkzeug.exceptions import BadRequest
from TaskManagementAPI.APIs.Auth.authentication import required_auth
from TaskManagementAPI.APIs.Auth.authorization import authorize
from TaskManagementAPI.APIs.Auth import auth_blueprint
from TaskManagementAPI.errors.error_handler import CustomError
from TaskManagementAPI.constants.status_code import BAD_REQUEST
from TaskManagementAPI.constants.messages import NOT_VALID_JSON
from TaskManagementAPI.configs.flask_limiter_config import limiter
from TaskManagementAPI.APIs.Auth.auth_controller import (  
    register_controller, login_controller, refresh_controller,
    forgot_password_controller, update_password_controller, 
    update_password_with_auth_controller
    )


@auth_blueprint.route('/register', methods=['POST'])
@limiter.limit("100 per day")
def register_view():
    try:
        data = request.get_json(force=True)
        return register_controller(data)
    except BadRequest as error:
        raise CustomError(NOT_VALID_JSON, BAD_REQUEST)
    except Exception as error:
        raise CustomError(str(error), log=True)



@auth_blueprint.route('/login', methods=['POST'])
@limiter.limit("100 per day")
def login_view():
    try:
        data = request.get_json(force=True)
        return login_controller(data)
    except BadRequest as error:
        raise CustomError(NOT_VALID_JSON, BAD_REQUEST)
    except Exception as error:
        raise CustomError(str(error), log=True)



@auth_blueprint.route('/refresh', methods=['POST'])
@limiter.limit("1 per day")
def refresh_view():
    try:
        refresh_token = request.headers.get('refresh_token')
        return refresh_controller(refresh_token)
    except BadRequest as error:
        raise CustomError(NOT_VALID_JSON, BAD_REQUEST)
    except Exception as error:
        raise CustomError(str(error), log=True)


@auth_blueprint.route('/forgotPassword', methods=['POST'])
@limiter.limit("1 per day")
def forgot_password_view():
    try:
        user_email = request.args.get('user_email')
        return forgot_password_controller(user_email)
    except Exception as error:
        raise CustomError(str(error), log=True)
    


@auth_blueprint.route('/updatePassword', methods=['POST'])
@limiter.limit("1 per day")
def forgot_password_view():
    try:
        data = request.get_json(force=True)
        return update_password_controller(data)
    except BadRequest as error:
        raise CustomError(NOT_VALID_JSON, BAD_REQUEST)
    except Exception as error:
        raise CustomError(str(error), log=True)


@auth_blueprint.route('/updatePasswordWithAuth', methods=['POST'])
@limiter.limit("1 per day")
@required_auth
def forgot_password_with_auth_view():
    try:
        data = request.get_json(force=True)
        return update_password_with_auth_controller(data)
    except BadRequest as error:
        raise CustomError(NOT_VALID_JSON, BAD_REQUEST)
    except Exception as error:
        raise CustomError(str(error), log=True)