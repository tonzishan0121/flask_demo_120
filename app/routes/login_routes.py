from flask import request, jsonify
from app import app
from app.services import authenticate_user,update_last_login
from flask_jwt_extended import create_access_token,jwt_required
def login_routes():
    @app.route('/login', methods=['POST'])
    def login():
        data = request.json
        email = data.get('email')
        password = data.get('password')
        user = authenticate_user(email, password)
        if user:
            access_token = create_access_token(identity=user.email)
            update_last_login(str(email))
            
            return jsonify(access_token=access_token), 200
        else:
            return jsonify(message='Invalid credentials'), 401
        
    @app.route('/update_time', methods=['POST'])
    @jwt_required()
    def update_time():
        data = request.json
        email = data.get('email')
        update_last_login(email)
        access_token = create_access_token(identity=email)
        return jsonify(access_token=access_token), 200