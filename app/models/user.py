from datetime import datetime
from . import _db as db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    email = db.Column(db.String(100), primary_key=True)
    nickname = db.Column(db.String(50), nullable=False)
    password_hash = db.Column(db.String(64), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    last_login = db.Column(db.DateTime, nullable=False, default=datetime.now)

    def set_password(self, password):
        password_hash = generate_password_hash(password)
        return password_hash

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def add_user(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    #刷新用户登陆时间
    @staticmethod
    def update_last_login(email):
        user=User.query.filter_by(email=email).first()
        user.last_login = datetime.now()
        db.session.commit()

    
    def __repr__(self):
        return f"<User {self.email}>"