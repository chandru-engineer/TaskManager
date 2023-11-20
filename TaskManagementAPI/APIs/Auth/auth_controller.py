from TaskManagementAPI.constants.status_code import INTERNAL_SERVER_ERROR
from TaskManagementAPI.constants.messages import SERVER_ERROR
from TaskManagementAPI.errors.error_handler import CustomError


def create_account_control(data):
    try:
        pass
    except Exception as error:
        raise CustomError(str(error), log=True)
    

def update_account_control():
    try:
        pass
    except Exception as error:
        raise CustomError(str(error), log=True)
    

def get_account_details_control():
    try:
        pass
    except Exception as error:
        raise CustomError(str(error), log=True)
    

def delete_account_control():
    try:
        pass
    except Exception as error:
        raise CustomError(str(error), log=True)