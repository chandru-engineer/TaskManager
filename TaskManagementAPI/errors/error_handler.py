from TaskManagementAPI.constants.messages import SERVER_ERROR
from TaskManagementAPI.constants.status_code import INTERNAL_SERVER_ERROR



class CustomError(Exception):
    """
    CustomError class for handling custom exceptions with additional context.

    Attributes:
    - message (str): The error message.
    - status_code (int): The HTTP status code associated with the error.
    - module_name (str): The name of the module where the error occurred.
    - function_name (str): The name of the function where the error occurred.
    """

    def __init__(self, message=None, status_code=None, module_name=None, function_name=None, log=False):
        """
        Initializes a new instance of the CustomError class.

        Parameters:
        - message (str, optional): The error message. Defaults to None.
        - status_code (int, optional): The HTTP status code associated with the error. 
          Defaults to None.
        - module_name (str, optional): The name of the module where the error occurred.
          Defaults to None.
        - function_name (str, optional): The name of the function where the error occurred.
          Defaults to None.
        """
        super().__init__(message)
        self.status_code = status_code or INTERNAL_SERVER_ERROR
        self.error_message = message or SERVER_ERROR
        self.module_name = module_name
        self.function_name = function_name
        self.log = log