from TaskManagementAPI import db
from datetime import datetime



class User(db.Model):
    __tablename__ = "user"
    user_id = db.Column(db.Integer, primary_key=True)
    user_uid = db.Column(db.String, nullable=False)
    org_id = db.Column(db.Integer, nullable=False)
    user_name = db.Column(db.String, nullable=False)
    user_email = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=True)
    is_active = db.Column(db.Boolean, nullable=True)
    is_deleted = db.Column(db.Boolean, nullable=True)
    last_login_time = db.Column(db.DateTime, default=None)
    created_by = db.Column(db.String, nullable=False)
    updated_by = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=None)
    


