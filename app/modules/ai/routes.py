from flask import request, jsonify, render_template
from app.modules.ai import ai_bp
from app.modules.ai.services import AiService

ai_service = AiService()

project_id = "amazing-source-213816"
language_code = "es"


@ai_bp.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('text')
    response_text = ai_service.detect_intent_texts(project_id, "unique-session-id", user_message, language_code)

    return jsonify({"response": response_text})


@ai_bp.route('/ai')
def ai():
    return render_template("ai/ai.html")
