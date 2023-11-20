from TaskManagementAPI import db
from datetime import datetime


class Org(db.Model):
    __tablename__ = 'org'
    org_id = db.Column(db.Integer, primary_key=True)
    org_uid = db.Column(db.String, nullable=False)
    org_name = db.Column(db.String, nullable=False)
    org_email = db.Column(db.String, nullable=False)
    is_deleted = db.Column(db.Boolean, nullable=True, default=True)
    created_by = db.Column(db.String, nullable=False)
    updated_by = db.Column(db.String, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=True)

    def __str__(self):
        return self.org_name
    
    def add(self): 
        pass

    def commit(self):
        pass