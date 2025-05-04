from flask import send_file,Blueprint
from app.services.analyze_service import *
from flask_jwt_extended import jwt_required

analyze_routes = Blueprint('analyze_routes', __name__)
@analyze_routes.route('/analyze/task-trend')
def task_trend():
    img = get_task_trend()
    return send_file(img, mimetype='image/png')

@analyze_routes.route('/analyze/region-distribution')
def region_distribution():
    img = get_region_distribution()
    return send_file(img, mimetype='image/png')

