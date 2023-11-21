from TaskManagementAPI import ma 
import re
from marshmallow import fields, validate, ValidationError, validates
from TaskManagementAPI.constants.messages import INVALID_STRING, WEAK_PASSWORD


class RegisterSchame(ma.Schema):
    user_name = fields.String(required=True, validate=validate.Length(min=1, max=55))
    user_email = fields.String(required=True, validate=validate.Length(min=1, max=55))
    org_name = fields.String(required=True, validate=validate.Length(min=1,max=55))
    password = fields.String(required=True, validate=validate.Length(min=8))

    # Add a custom validation for org_name using the @validates decorator
    @validates("org_name")
    def validate_org_name(self, value):
        if not self.is_valid_org_name(value):
            raise ValidationError(INVALID_STRING)
        return value
    
    @validates("user_name")
    def validate_org_name(self, value):
        if not self.is_valid_org_name(value):
            raise ValidationError(INVALID_STRING)
        return value
    
    @validates("password")
    def validate_org_name(self, value):
        if not self.is_valid_org_name(value):
            raise ValidationError(WEAK_PASSWORD)
        return value

    def is_valid_org_name(self, value):
        # Use a regular expression to check for invalid characters
        return bool(re.match(r'^[a-zA-Z0-9_\- ]+$', value))
    
    def is_valid_password(self, value):
        # Check for at least one uppercase letter, one lowercase letter, one digit, one special character, and no spaces
        pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()-_=+[\]{}|;:\'",.<>/?`~])[A-Za-z\d!@#$%^&*()-_=+[\]{}|;:\'",.<>/?`~]{8,}$')
        return bool(pattern.match(value))
    


class LoginSchema(ma.Schema):
    user_email = fields.String(required=True, validate=validate.Length(min=1, max=55))
    password = fields.String(required=True, validate=validate.Length(min=8))




class UpdatePasswordSchema(ma.Schema):
    user_email = fields.String(required=True, validate=validate.Length(min=1, max=55))
    password = fields.String(required=True, validate=validate.Length(min=8))
    confirm_password = fields.String(required=False)
    otp = fields.Integer(required=True)

    # Add a custom validation for org_name using the @validates decorator
    @validates("password")
    def validate_org_name(self, value):
        if not self.is_valid_org_name(value):
            raise ValidationError(WEAK_PASSWORD)
        return value

    def is_valid_password(self, value):
        # Check for at least one uppercase letter, one lowercase letter, one digit, one special character, and no spaces
        pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()-_=+[\]{}|;:\'",.<>/?`~])[A-Za-z\d!@#$%^&*()-_=+[\]{}|;:\'",.<>/?`~]{8,}$')
        return bool(pattern.match(value))
    