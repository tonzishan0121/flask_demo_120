from flask import request, jsonify
from app.services.task_service import create_task, get_all_tasks, get_task_by_id, update_task, delete_task
from app import app

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

    @app.route('/tasks', methods=['GET'])
    def get_all_tasks_route():
        tasks = get_all_tasks()
        return jsonify(tasks), 200

    @app.route('/tasks/<task_id>', methods=['GET'])
    def get_task_by_id_route(task_id):
        task = get_task_by_id(task_id)
        if task:
            return jsonify(task.__dict__), 200
        return jsonify(message='Task not found'), 404

    @app.route('/tasks/<task_id>', methods=['PUT'])
    def update_task_route(task_id):
        data = request.json
        task = update_task(task_id, **data)
        if task:
            return jsonify(task.__dict__), 200
        return jsonify(message='Task not found'), 404

    @app.route('/tasks/<task_id>', methods=['DELETE'])
    def delete_task_route(task_id):
        success = delete_task(task_id)
        if success:
            return jsonify(message='Task deleted successfully'), 200
        return jsonify(message='Task not found'), 404