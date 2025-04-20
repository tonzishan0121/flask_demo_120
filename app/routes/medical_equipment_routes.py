from flask import request, jsonify
from app import app
from app.services.medical_equipment_service import *


def medical_equipment_routes():
    @app.route('/available_equipment_statistics', methods=['GET'])
    def available_equipment_statistics():
        available_count = get_available_equipment_count()
        percentage = get_available_equipment_percentage()
        return jsonify({
            'available_percentage': percentage,
            'available_equipment_count': available_count
        }), 200