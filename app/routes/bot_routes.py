from app.services import get_model_response
from flask import Blueprint, request, Response, stream_with_context


bot_bp = Blueprint('bot', __name__)

@bot_bp.route('/chat', methods=['POST'])
def bot():
    data = request.get_json()
    user_question = data['question']
    response = get_model_response(user_question)
    return Response(stream_with_context(response), mimetype='application/json')