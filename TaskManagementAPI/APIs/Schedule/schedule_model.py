from TaskManagementAPI import db
from datetime import datetime

class Org(db.Model):
    __tablename__ = 'schedule'
    schedule_id = db.Column(db.Integer, primary_key=True)
    schedule_uid = db.Column(db.String, nullable=False)
    org_id = db.Column(db.Integer, nullable=False)
    task_id = db.Column(db.Integer, nullable=False)
    schedule_status = db.Column(db.String, nullable=False)
    schedule_datetime_utc = db.Column(db.Datetime, nullable=True)
    schedule_timezone = db.Column(db.String, nullable=False)
    schedule_completed_by = db.Column(db.String, nullable=False)
    schedule_by = db.Column(db.Integer, nullable=False)
    schedule_to = db.Column(db.Integer, nullable=False)
    is_deleted = db.Column(db.Boolean, nullable=False, default=True)
    created_by = db.Column(db.String, nullable=False)
    updated_by = db.Column(db.String, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.Datetime, nullable=True)

    def __str__(self):
        return self.schedule_uid
    
    def add(self): 
        pass

    def commit(self):
        pass