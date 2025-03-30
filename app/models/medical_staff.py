from datetime import datetime
from . import _db as db

class MedicalStaff(db.Model):
    __tablename__ = 'medical_staff'
    staff_id = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    statusText = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    ambulance_id = db.Column(db.String(20), db.ForeignKey('ambulances.ambulance_id'), nullable=True)
    last_update_time = db.Column(db.DateTime, nullable=False, default=datetime.now)

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
    def get_by_id(cls, staff_id):
        return cls.query.filter_by(staff_id=staff_id).first()
    def __repr__(self):
        return f"<MedicalStaff {self.staff_id}>"