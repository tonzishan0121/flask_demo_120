from flask_sqlalchemy import SQLAlchemy
from ..app.services import get_all_users
from flask import jsonify
from ..app import init_app
from ..app.models.user import User
app=init_app()
db = SQLAlchemy(app)
User=User(db.Model)
users=User.get_all_users()

print(jsonify(users))