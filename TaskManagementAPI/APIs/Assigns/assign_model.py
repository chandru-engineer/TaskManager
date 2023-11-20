# Table assign {
#   assign_id integer [primary key]
#   org_id integer
#   assign_to integer
#   task_id integer [ref: - task.task_id]
#   assign_by integer
#   is_deleted boolean
#   assign_uid varchar
#   created_by varchar
#   updated_by varchar
#   created_at datetime
#   updated_at datetime
# }

from TaskManagementAPI import db
from datetime import datetime


class Assign(db.Model):

    __tablename__ = 'assign'
    
    assign_id = db.Column(db.Integer, primary_key=True)
    assign_uid = db.Column(db.String, nullable=False)
    task_id = db.Column(db.Integer, nullable=False)
    assign_to = db.Column(db.Integer, nullable=False)
    assign_by = db.Column(db.Integer, nullable=False)
    is_deleted = db.Column(db.Boolean, nullable=False, default=True)
    created_by = db.Column(db.String, nullable=False)
    updated_by = db.Column(db.String, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.Datetime, nullable=True)

    def __str__(self):
        return self.assign_uid
    
    def add(self): 
        pass

    def commit(self):
        pass