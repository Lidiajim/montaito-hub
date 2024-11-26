from flask import Flask, request, jsonify
import os
from google.cloud import dialogflow_v2 as dialogflow

app = Flask(__name__)

# Configuración de autenticación de Google Cloud

project_id = "amazing-source-213816"
language_code = "es"


# Función para enviar consultas a Dialogflow
def detect_intent_texts(project_id, session_id, text, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(request={"session": session, "query_input": query_input})

    return response.query_result.fulfillment_text


@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response_text = detect_intent_texts(project_id, "unique-session-id", user_message, language_code)
    
    return jsonify({"response": response_text})


if __name__ == '__main__':
    app.run(debug=True)
