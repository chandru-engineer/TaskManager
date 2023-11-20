from TaskManagementAPI import db
from datetime import datetime


class Task(db.Model):

    __tablename__ = 'task'
    task_id = db.Column(db.Integer, primary_key=True)
    task_uid = db.Column(db.String, nullable=False)
    org_id = db.Column(db.Integer, nullable=False)
    assign_id = db.Column(db.Integer, nullable=False)
    schedule_id = db.Column(db.Integer, nullable=False)
    task_name = db.Column(db.String, nullable=False)
    task_description = db.Column(db.String, nullable=False)
    task_priority = db.Column(db.String, nullable=False)
    task_status = db.Column(db.String, nullable=False)
    task_deadline = db.Column(db.Datetime, nullable=True)
    task_timezone = db.Column(db.String, nullable=False)
    is_deleted = db.Column(db.Boolean, nullable=False, default=True)
    created_by = db.Column(db.String, nullable=False)
    updated_by = db.Column(db.String, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.Datetime, nullable=True)

    def __str__(self):
        return self.task_name
    
    def add(self): 
        pass

    def commit(self):
        pass