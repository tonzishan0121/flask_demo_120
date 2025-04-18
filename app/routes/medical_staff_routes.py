from flask import request, jsonify
from app import app
from app.services import get_standby_staff_count, get_standby_staff_percentage


def medical_staff_routes():
    @app.route('/medical_staff_statistics', methods=['GET'])
    def medical_staff_statistics():
        standby_count = get_standby_staff_count()
        percentage = get_standby_staff_percentage()
        return jsonify({
            'standby_staff_count': standby_count,
            'standby_percentage': percentage
        }), 200