from marshmallow import fields, validate
from TaskManagementAPI import ma 
from TaskManagementAPI.APIs.Org.org_model import Org


class CreateOrgSchema(ma.Schema):
    org_id = fields.Number(required=True)
    org_uid = fields.String(required=True, validate=validate.Length(min=1))
    org_name = fields.String(required=True, validate=validate.Length(min=1))
    org_email = fields.Email(required=True)
    created_by = fields.String(required=False)
    updated_by = fields.String(required=False)
    created_at = fields.DateTime(required=False)
    updated_at = fields.DateTime(required=False)


class UpdateOrgSchema():
    org_name = fields.String(required=True, validate=validate.Length(min=1))
    updated_by = fields.String(required=False)
    updated_at = fields.DateTime(required=False)


class DeleteOrgSchema():
    pass


class GetOrgSchema(ma.ModelSchema):
    class Meta:
        model = Org
        exclude = ('created_by', 'updated_by', 'is_deleted', 'created_at', 'updated_at')