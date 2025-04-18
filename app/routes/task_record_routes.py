from flask import request, jsonify
from app import app
from app.services.task_record_service import *

@app.route('/task_record', methods=['GET'])#获取平均响应时长和增长百分比
def task_record_routes():
    @app.route('/response_time_statistics', methods=['GET'])
    def response_time_statistics():
        today_avg = get_today_avg_response_time()
        change_percentage = get_response_time_change_percentage()
        return jsonify({
            'today_avg_response_time': today_avg,
            'change_percentage': change_percentage
        }), 200