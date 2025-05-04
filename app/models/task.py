from datetime import datetime,timedelta
from . import _db as db

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.String(20), primary_key=True)
    status = db.Column(db.String(20), nullable=False)
    statusText = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    response_time = db.Column(db.Integer, nullable=True)

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
        return cls.query.limit(50).all()

    @classmethod
    def get_by_id(cls, task_id):
        return cls.query.filter_by(id=task_id).first()
    
    @classmethod
    def get_today_count(cls):
        today_start = datetime.combine(datetime.now().date(), datetime.min.time())
        today_end = today_start + timedelta(days=1)
        return cls.query.filter(cls.time >= today_start, cls.time < today_end).count()

    @classmethod
    def get_yesterday_count(cls):
        yesterday_start = datetime.combine(datetime.now().date() - timedelta(days=1), datetime.min.time())
        yesterday_end = yesterday_start + timedelta(days=1)
        return cls.query.filter(cls.time >= yesterday_start, cls.time < yesterday_end).count()
    
    @classmethod
    def get_today_task_count_by_status(cls)->dict:
        today_start = datetime.combine(datetime.now().date(), datetime.min.time())
        today_end = today_start + timedelta(days=1)
        status = ['completed', 'processing', 'pending']
        num={}
        for i in status:
            count = cls.query.filter(cls.time >= today_start, cls.time < today_end, cls.status == i).count()
            num[i] = count
        return num
    
    def __repr__(self):
        return f"<Task {self.id}>"