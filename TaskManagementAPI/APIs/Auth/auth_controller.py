import jwt
import random
import string
import secrets
import hashlib
from datetime import datetime
from TaskManagementAPI import db
from marshmallow import ValidationError
from TaskManagementAPI.configs.configs import SECRET_KEY
from TaskManagementAPI.configs.celery_config import celery
from jwt.exceptions import ExpiredSignatureError, InvalidSignatureError
from TaskManagementAPI.constants.status_code import (
    OK, BAD_REQUEST) 
from TaskManagementAPI.constants.messages import (
    SERVER_ERROR, OTP_SENT, USER_NOT_FOUND, INVALID_OTP, PASSWORD_UPDATED, 
    INVALID_PASSWORD, INVALID_REFRESH_TOKEN, LOGIN_REQUIRED, REFRESG_TOKEN_REQUIRED,
    NOT_VALID_JSON) 
from TaskManagementAPI.errors.error_handler import CustomError
from TaskManagementAPI.APIs.Org.org_model import Org
from TaskManagementAPI.APIs.Users.user_model import User
from TaskManagementAPI.APIs.Auth.auth_schema import (
    RegisterSchame, LoginSchema, UpdatePasswordSchema, 
    AddUserSchema)
from TaskManagementAPI.APIs.Users.user_schema import GetOrgSchema



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
        return {'Unsuccessful': NOT_VALID_JSON, "error": str(error)}, BAD_REQUEST
    except Exception as error:
        raise CustomError(str(error), log=True)
    

def login_controller(data: dict):
    try:
        data = LoginSchema().load(data)
        user_obj = User.query.filter_by(name=data['user_email']).first()
        if user_obj:
            if user_obj.password == generate_hash(data['password']):
                payload_access = {
                    'user_id': user_obj.user_id,
                    'user_uid': user_obj.user_uid,
                    "user_name": user_obj.user_name,
                    "user_email": user_obj.user_email, 
                    'user_role': "Admin" if user_obj.is_admin else "User",
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
                }
                payload_refresh = {
                    "username": user_obj.user_email,
                    "exp": user_obj.datetime.utcnow() + datetime.timedelta(days=30)
                }
                access_token = jwt.encode(payload_access, SECRET_KEY, algorithm='HS256')
                refresh_token = jwt.encode(payload_refresh, SECRET_KEY, algorithm='HS256')
                return {'access_token': access_token, 'refresh_token': refresh_token}, OK
    except Exception as error:
        raise CustomError(str(error), log=True)


def refresh_controller(refresh_token: str):
    if not refresh_token:
        return {'error': REFRESG_TOKEN_REQUIRED}, 401
    try:
        data = jwt.decode(refresh_token, SECRET_KEY, algorithms=['HS256'])
        user_obj = User.query.filter_by(user_email=data['user_email']).first()
        if user_obj:
            payload_access = {
                    'user_id': user_obj.user_id,
                    'user_uid': user_obj.user_uid,
                    "user_name": user_obj.user_name,
                    "user_email": user_obj.user_email, 
                    'user_role': "Admin" if user_obj.is_admin else "User",
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
            }
            access_token = jwt.encode(payload_access, SECRET_KEY, algorithm='HS256')
            return {'access_token': access_token}, OK
    except ExpiredSignatureError:
        raise CustomError(str(LOGIN_REQUIRED), status_code=401, log=True)
    except InvalidSignatureError:
        raise CustomError(str(INVALID_REFRESH_TOKEN), status_code=401, log=True)
    except Exception as error:
        raise CustomError(str(error), log=True)


def forgot_password_controller(user_email: str):
    try:
        user_obj = User.query.filter_by(user_email=user_email, is_deleted=False)
        if user_obj.first() is None:
            return {'Unsuccessful': USER_NOT_FOUND}, 404
        otp = generate_otp()
        user_obj.opt = otp
        user_obj.is_otp_used = False
        db.session.commit()
        task = celery.send_task('send_otp', 
                                    args=[{'user_email': user_obj.user_email, "otp": otp}])
        return {'Successfull': OTP_SENT}, OK
    except Exception as error:
        raise CustomError(str(error))



def update_password_controller(data: dict):
    try:
        data = UpdatePasswordSchema().load(data)
        user_obj = User.query.filter_by(user_email=data['user_email'], is_deleted=False)
        if user_obj.first() is None:
            return {'Unsuccessful': USER_NOT_FOUND}, 404
        if user_obj.otp == data['otp'] and user_obj.otp == False:
            user_obj.password = generate_hash(data['password'])
            user_obj.is_otp_used = True
            db.session.commit()
            return {'Successfull': PASSWORD_UPDATED}, 200
        else:
            return {'Successfull': INVALID_OTP}, 400
    except Exception as error:
        raise CustomError(str(error))


def update_password_with_auth_controller(data: dict):
    try:
        data = UpdatePasswordSchema().load(data)
        user_obj = User.query.filter_by(user_email=data['user_email'], is_deleted=False)
        if user_obj.first() is None:
            return {'Unsuccessful': USER_NOT_FOUND}, 404
        if data['password'] == data['confirm_password']:
            user_obj.password = generate_hash(data['password'])
            db.session.commit()
            return {'Successfull': PASSWORD_UPDATED}, 200
        else:
            return {'Successfull': INVALID_PASSWORD}, 400
    except Exception as error:
        raise CustomError(str(error))



def add_user_controller(data: dict):
    try:
        data = AddUserSchema().load(data)
        user_obj = User.query.filter_by(user_email=data['user_email'], is_deleted=False)

    except Exception as error:
        raise CustomError(str(error))




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


def generate_uid(length: int):
    characters = string.ascii_letters
    uid = ''.join(secrets.choice(characters) for _ in range(length))
    return uid


def generate_hash(input_string: str):
    # Create a new SHA-256 hash object
    sha256_hash = hashlib.sha256()
    # Update the hash object with the bytes representation of the input string
    sha256_hash.update(input_string.encode('utf-8'))
    # Get the hexadecimal representation of the hash
    return sha256_hash.hexdigest()



def generate_otp():
    # Generate a secure random 6-digit number
    otp = secrets.randbelow(900000) + 100000
    return otp
