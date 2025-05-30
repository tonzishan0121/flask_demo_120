import os
import datetime

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS=os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', False)
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'jwt_secret_key')
    JWT_ACCESS_TOKEN_EXPIRES =datetime.timedelta(seconds=eval(os.getenv('JWT_ACCESS_TOKEN_EXPIRES', 3600)))