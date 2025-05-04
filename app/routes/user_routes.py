from flask import request, jsonify
from app.services import get_all_users,post_test,update_last_login
from app import app

def user_routes():
    @app.route('/users', methods=['POST'])
    def post_users():
        pwd=request.json.get('pwd')
        users = post_test(pwd)
        return jsonify(users),201

    @app.route('/check_session', methods=['POST'])
    def check_session():
        email = request.json.get('email')
        if not email:
            return jsonify({"error": "缺少email参数"}), 400
        
        result = update_last_login(email)
        
        if result["status"] == "expired":
            return jsonify({"error": "会话已过期，请重新登录"}), 401
        elif result["status"] == "success":
            return jsonify({"message": "会话有效"}), 200
        else:
            return jsonify(result), 400