from datetime import datetime
from . import _db as db

class TaskRecord(db.Model):
    __tablename__ = 'task_records'
    record_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task_id = db.Column(db.String(20), db.ForeignKey('tasks.id'), nullable=False)
    ambulance_id = db.Column(db.String(20), db.ForeignKey('ambulances.ambulance_id'), nullable=False)
    equipment_id = db.Column(db.String(20), db.ForeignKey('medical_equipment.equipment_id'), nullable=False)
    doctor_id = db.Column(db.String(20), db.ForeignKey('medical_staff.staff_id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    end_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    duration = db.Column(db.Integer, nullable=False)
    task_status = db.Column(db.String(20), nullable=False)
    task_statusText = db.Column(db.String(50), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, record_id):
        return cls.query.filter_by(record_id=record_id).first()
    def __repr__(self):
        return f"<TaskRecord {self.record_id}>"