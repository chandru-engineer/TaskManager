from TaskManagementAPI.constants.status_code import INTERNAL_SERVER_ERROR, OK
from TaskManagementAPI.constants.messages import SERVER_ERROR, OTP_SENT
from TaskManagementAPI.errors.error_handler import CustomError
from TaskManagementAPI.APIs.Org.org_model import Org
from TaskManagementAPI.APIs.Users.user_model import User
from TaskManagementAPI.APIs.Auth.auth_schema import RegisterSchame
from TaskManagementAPI.APIs.Users.user_schema import GetOrgSchema
from TaskManagementAPI import db
from marshmallow import ValidationError
from TaskManagementAPI.configs.celery_config import celery


def register_controller(data: dict):
    try:
        data = RegisterSchame().load(data)
        data['org_id'] = add_org(data)
        otp = add_user(data)
        if isinstance(otp, int):
            task = celery.send_task('send_otp', 
                                    args=[{'user_email': data['user_email'], "otp": otp}])
            return {'Successfull': OTP_SENT}, OK
        else:
            raise CustomError(str(error), log=True)
    except ValidationError as error:
        raise CustomError(str(error), status_code=400)
    except Exception as error:
        raise CustomError(str(error), log=True)


def add_org(data: dict):
    try:
        org_data = {
            "org_name": data['org_name'],
            "org_email": data['user_email'],
            "created_by": data['user_email'],
            "org_uid": generate_uid(6)
        }
        org_obj = Org(**org_data)
        db.session.add(org_obj)
        db.session.commit()
        return org_obj.org_id
    except Exception as error:
        raise CustomError(str(error))


def add_user(data: dict):
    try:
        user_data = {
            'org_id': data['org_id'],
            "user_name": data['user_name'],
            "user_email": data['user_email'],
            "is_admin": True,
            "password": generate_hash(data['password']),
            'created_by': data['user_email'],
            "user_uid": generate_uid(6),
            "otp": generate_otp()
        }
        user_obj = User(**user_data)
        db.session.add(user_obj)
        db.session.commit()
        return user_obj.otp
    except Exception as error:
        raise CustomError(str(error), log=True)



import random
import string
import hashlib

def generate_uid(length: int):
    characters = string.ascii_letters 
    return ''.join(random.choice(characters) for _ in range(length))

def generate_hash(input_string: str):
    # Create a new SHA-256 hash object
    sha256_hash = hashlib.sha256()
    # Update the hash object with the bytes representation of the input string
    sha256_hash.update(input_string.encode('utf-8'))
    # Get the hexadecimal representation of the hash
    return sha256_hash.hexdigest()

def generate_otp():
    # Generate a random 6-digit number
    otp = random.randint(100000, 999999)
    return otp
