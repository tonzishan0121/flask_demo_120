from flask import request, jsonify
from app import app
from app.services import get_idle_ambulance_count, get_idle_ambulance_percentage

def ambulance_routes():
    @app.route('/ambulance_statistics', methods=['GET'])
    def ambulance_statistics():
        idle_count = get_idle_ambulance_count()
        percentage = get_idle_ambulance_percentage()
        return jsonify({
            'idle_ambulance_count': idle_count,
            'idle_percentage': percentage
        }), 200