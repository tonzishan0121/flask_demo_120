from flask import request, jsonify
from app.services.task_service import *
from app import app
    #新建任务记录
def task_routes():
    @app.route('/tasks', methods=['POST'])
    def create_task_route():
        data = request.json
        task = create_task(
            id=data.get('id'),
            status=data.get('status'),
            statusText=data.get('statusText'),
            location=data.get('location'),
            description=data.get('description'),
            time=data.get('time'),
            response_time=data.get('response_time')
        )
        return jsonify(task.__dict__), 201

    # 获取所有任务记录
    @app.route('/tasks', methods=['GET'])
    def get_all_tasks_route():
        tasks = get_all_tasks()
        return jsonify(tasks), 200

    # 根据任务ID获取任务记录
    @app.route('/tasks/<task_id>', methods=['GET'])
    def get_task_by_id_route(task_id):
        task = get_task_by_id(task_id)
        if task:
            return jsonify(task.__dict__), 200
        return jsonify(message='Task not found'), 404
    
    #未启用
    @app.route('/tasks/<task_id>', methods=['PUT'])
    def update_task_route(task_id):
        data = request.json
        task = update_task(task_id, **data)
        if task:
            return jsonify(task.__dict__), 200
        return jsonify(message='Task not found'), 404

    #未启用
    @app.route('/tasks/<task_id>', methods=['DELETE'])
    def delete_task_route(task_id):
        success = delete_task(task_id)
        if success:
            return jsonify(message='Task deleted successfully'), 200
        return jsonify(message='Task not found'), 404

  # 获取今日任务数量和变化百分比  
    @app.route('/task_statistics', methods=['GET'])
    def task_statistics():
        today_count = get_today_task_count()
        change_percentage = get_task_count_change_percentage()
        return jsonify({
            'today_task_count': today_count,
            'change_percentage': change_percentage
        }), 200
    
    @app.route('/tasks/today/status', methods=['GET'])
    def get_today_task_status():
        return jsonify(get_today_task_count_by_status()), 200