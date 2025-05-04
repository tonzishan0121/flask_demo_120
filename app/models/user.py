from datetime import datetime,timedelta
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

    def update_last_login(self):
        now = datetime.now()
        # 检查是否超过24小时
        self.last_login = now
        db.session.commit()
        print(self.last_login)
        return True  # 更新成功

    
    def __repr__(self):
        return f"<User {self.email}>"