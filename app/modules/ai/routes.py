from flask import request, jsonify, render_template
from app.modules.ai import ai_bp
from app.modules.ai.services import AiService

ai_service = AiService()

project_id = "amazing-source-213816"
language_code = "es"


def get_datasets():
    # Aquí puedes hacer una consulta a tu base de datos o cualquier otro origen de datos
    datasets = [
        "Dataset 1: Usuarios",
        "Dataset 2: Transacciones",
        "Dataset 3: Productos",
        "Dataset 4: Reviews"
    ]
    return datasets


@ai_bp.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('text')
           
    response_text = ai_service.detect_intent_texts(project_id, "unique-session-id", user_message, language_code)
    
    if response_text == 'dataset':
        datasets = get_datasets()
        response_text = "Los datasets disponibles son:\n" + "\n".join(datasets)
        
    return jsonify({"response": response_text})


@ai_bp.route('/ai')
def ai():
    return render_template("ai/ai.html")
