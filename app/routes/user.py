from flask import request, jsonify
from app.services import get_all_users,post_test,test_user
from app import app

def user_routes():
    @app.route('/users', methods=['GET'])
    def get_users():
        users = get_all_users()
        return jsonify(users),200
    
    @app.route('/users', methods=['POST'])
    def post_users():
        pwd=request.json.get('pwd')
        users = post_test(pwd)
        return jsonify(users),201

    @app.route('/tests/users', methods=['POST'])
    def test_users():
        pwd=request.json.get('pwd')
        pwd_hash = test_user(pwd)
        return {"pwd_hash":pwd_hash},202
