from flask import Flask
from flask_jwt_extended import JWTManager
from .config import Config
def init_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS
    app.config['JWT_SECRET_KEY'] = Config.JWT_SECRET_KEY
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = Config.JWT_ACCESS_TOKEN_EXPIRES
    jwt = JWTManager(app)
    return app

app=init_app()

from .routes import login_routes,task_routes,user_routes,task_record_routes,ambulance_routes,medical_staff_routes

login_routes()
task_routes()
user_routes()
task_record_routes()
ambulance_routes()
medical_staff_routes()

__all__ = ['app']