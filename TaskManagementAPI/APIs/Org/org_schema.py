from marshmallow import Schema, fields, validate
from TaskManagementAPI import ma 
from TaskManagementAPI.APIs.Org.org_model import Org

class Org(db.Model):
    __tablename__ = 'org'
    org_id = db.Column(db.Integer, primary_key=True)
    org_uid = db.Column(db.String, nullable=False)
    org_name = db.Column(db.String, nullable=False)
    org_email = db.Column(db.String, nullable=False)
    is_deleted = db.Column(db.Boolean, nullable=False, default=True)
    created_by = db.Column(db.String, nullable=False)
    updated_by = db.Column(db.String, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.Datetime, nullable=True)



class CreateOrgSchema():
    pass




class CreateOrgSchema(ma.Schema):
    org_uid = fields.String(required=True, validate=validate.Length(min=1))
    org_name = fields.String(required=True, validate=validate.Length(min=1))
    org_email = fields.Email(required=True)
    created_by = fields.String(required=True)


class UpdateOrgSchema():
    pass


class DeleteOrgSchema():
    pass


class GetOrgSchema(ma.ModelSchema):
    class Meta:
        model = Org
        exclude = ('created_by', 'updated_by', 'is_deleted', 'created_at', 'updated_at')