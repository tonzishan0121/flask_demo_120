from flask import jsonify

@app.errorhandler(404)
def not_found_error(e):
    return jsonify(error=str(e)), 404

@app.errorhandler(500)
def internal_error(e):
    return jsonify(error=str(e)), 500