from TaskManagementAPI import ma
from TaskManagementAPI.APIs.Users.user_model import User
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class GetOrgSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        exclude = ("password", "user_id", "otp", "is_otp_used", "is_active", "is_deleted")