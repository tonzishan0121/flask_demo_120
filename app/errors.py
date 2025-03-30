from flask import jsonify
from app import app  
@app.errorhandler(404)
def not_found_error(e):
    return jsonify(error="Not found"), 404

@app.errorhandler(500)
def internal_error(e):
    return jsonify(error="Internal server error"), 500