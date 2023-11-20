from flask import request
from werkzeug.exceptions import BadRequest
from TaskManagementAPI.APIs.Auth import auth_blueprint
from TaskManagementAPI.errors.error_handler import CustomError
from TaskManagementAPI.constants.status_code import BAD_REQUEST
from TaskManagementAPI.constants.messages import NOT_VALID_JSON
from TaskManagementAPI.configs.flask_limiter_config import limiter
from TaskManagementAPI.APIs.Auth.auth_controller import create_account_control, \
    update_account_control, get_account_details_control, delete_account_control



# route used to create a account
@auth_blueprint.route('/createAccount', methods=['POST'])
def create_account():
    try:
        data = request.get_json(force=True)
        return create_account_control(data)
    except BadRequest as error:
        raise CustomError(NOT_VALID_JSON, BAD_REQUEST)
    except Exception as error:
        raise CustomError(str(error))


# route used to uodate the account details
@auth_blueprint.route('/updateAccount', methods=['PUT'])
def update_account():
    try:
        decoded_token=None
        data = request.get_json(force=True)
        return update_account_control('data')
    except BadRequest as error:
        raise CustomError(NOT_VALID_JSON, BAD_REQUEST)
    except Exception as error:
        raise CustomError(str(error), log=True)
    

# routes used to get the account details
@auth_blueprint.route('/getAccountDetails', methods=['GET'])
def get_account_details():
    try:
        decoded_token=None
        return get_account_details_control('data')
    except Exception as error:
        raise CustomError(str(error), log=True)
    

# route used to delete the account details
@auth_blueprint.route('/deleteAccount', methods=['DELETE'])
def delete_account():
    try:
        decoded_token=None
        return delete_account_control(decoded_token)
    except Exception as error:
        raise CustomError(str(error), log=True)
    


@auth_blueprint.route('/limited', methods=['GET'])
@limiter.limit("1 per day")
def limited():
    try:
        # Your controller logic here
        return {'message': 'This route has rate limiting'}
    except Exception as e:
        raise CustomError(message="Rate limit exceeded", status_code=429)