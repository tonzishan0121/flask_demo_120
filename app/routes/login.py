from flask import request, jsonify
from app import app
from app.services import authenticate_user
from flask_jwt_extended import create_access_token

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    user = authenticate_user(email, password)
    if user:
        access_token = create_access_token(identity=user.email)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify(message='Invalid credentials'), 401