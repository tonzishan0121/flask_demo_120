from datetime import datetime
from . import _db as db

class Ambulance(db.Model):
    __tablename__ = 'ambulances'
    ambulance_id = db.Column(db.String(20), primary_key=True)
    license_plate = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    statusText = db.Column(db.String(50), nullable=False)
    driver_name = db.Column(db.String(50), nullable=False)
    driver_phone = db.Column(db.String(20), nullable=False)
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
    def get_by_id(cls, ambulance_id):
        return cls.query.filter_by(ambulance_id=ambulance_id).first()

    def __repr__(self):
        return f"<Ambulance {self.ambulance_id}>"