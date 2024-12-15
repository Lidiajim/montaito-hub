from flask import request, jsonify, render_template
from app.modules.ai import ai_bp
from app.modules.ai.services import AiService
from app.modules.dataset.services import DataSetService
from app.modules.featuremodel.services import FeatureModelService

ai_service = AiService()
dataset_service = DataSetService()
feature_model_service = FeatureModelService()

project_id = "amazing-source-213816"
language_code = "es"


def format_feature_response(feature_model_dict):
    return f"Feature Model: {feature_model_dict}"


def sqlalchemy_to_dict(obj):
    """
    Convierte un objeto SQLAlchemy a un diccionario, excluyendo atributos no serializables.
    """
    return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}


def format_dataset_response(dataset):
    authors = "\n".join([f"  - {author['name']} ({author['affiliation']})" for author in dataset['authors']])
    files = "\n".join([f"  - {file['name']} ({file['size_in_human_format']})" for file in dataset['files']])
    return (
        f"El dataset solicitado es:\n"
        f"  Título: {dataset['title']}\n"
        f"  ID: {dataset['id']}\n"
        f"  Creado en: {dataset['created_at']}\n"
        f"  Descripción: {dataset['description']}\n"
        f"  Autores:\n{authors}\n"
        f"  Tipo de publicación: {dataset['publication_type']}\n"
        f"  DOI de la publicación: {dataset['publication_doi']}\n"
        f"  DOI del dataset: {dataset['dataset_doi']}\n"
        f"  Tags: {', '.join(dataset['tags'])}\n"
        f"  URL: {dataset['url']}\n"
        f"  Descargar: {dataset['download']}\n"
        f"  Zenodo: {dataset['zenodo']}\n"
        f"  Archivos:\n{files}\n"
        f"  Número de archivos: {dataset['files_count']}\n"
        f"  Tamaño total: {dataset['total_size_in_human_format']}\n"
    )


@ai_bp.route('/chat', methods=['POST'])
def chat():
    try:
        # Obtén el JSON del cuerpo de la solicitud
        data = request.json
        if not data:
            return jsonify({"error": "No JSON payload received"}), 400

        # Navega por la estructura de forma segura
        message_data = data.get('message', {})
        query_result = message_data.get('queryResult', {})
        fulfillment_messages = query_result.get('fulfillmentMessages', [])

        # Verifica que fulfillmentMessages tenga al menos un elemento
        if not fulfillment_messages or not isinstance(fulfillment_messages[0], dict):
            return jsonify({"error": "'fulfillmentMessages' is empty or not a valid list"}), 400

        payload = fulfillment_messages[0].get('payload', {})
        if not payload:
            return jsonify({"error": "'payload' not found in 'fulfillmentMessages[0]'"}), 400

        # Extrae 'message' y 'response_text' del payload
        message = payload.get('message')
        response_text = payload.get('response_text')

        if not message or not response_text:
            return jsonify({"error": "'message' or 'response_text' not found in 'payload'"}), 400

        # Imprime los valores extraídos
        print(response_text)
        print(message)

        # Procesamiento basado en el valor de response_text
        valor_inicial = response_text

        if response_text == 'dataset-numero':
            response_text = dataset_service.count_synchronized_datasets()

        elif response_text == 'feature-number':
            response_text = feature_model_service.count_feature_models()

        elif response_text == 'dataset-downloads':
            total_dataset_downloads = dataset_service.total_dataset_downloads()
            response_text = total_dataset_downloads if total_dataset_downloads > 0 else 0

        elif response_text == 'feature-downloads':
            total_feature_model_downloads = feature_model_service.total_feature_model_downloads()
            response_text = total_feature_model_downloads if total_feature_model_downloads > 0 else 0

        elif response_text == 'dataset-views':
            total_dataset_views = dataset_service.total_dataset_views()
            response_text = total_dataset_views

        elif response_text == 'feature-views':
            total_feature_model_views = feature_model_service.total_feature_model_views()
            response_text = total_feature_model_views

        elif response_text == 'dataset-latest':
            latest_datasets = dataset_service.latest_synchronized()
            dataset_names = [str(dataset.id) for dataset in latest_datasets]  # Convertir a cadenas
            response_text = dataset_names

        elif response_text == 'dataset-get':
            dataset_id = message
            dataset = dataset_service.get_by_id(dataset_id)
            if dataset is None:
                response_text = "no se encontró el dataset"
            else:
                dataset = dataset.to_dict()
                response_text = format_dataset_response(dataset)

        elif response_text == 'feature-get':
            feature_model_id = message
            feature_model = feature_model_service.get_by_id(feature_model_id)
            if feature_model is None:
                response_text = "no se encontró el feature"
            else:
                feature_model_dict = sqlalchemy_to_dict(feature_model)
                response_text = format_feature_response(feature_model_dict)

        # Si response_text no cambió, lo marcamos como None
        if valor_inicial == response_text:
            response_text = None

        return jsonify({"message": message, "response": response_text})

    except Exception as e:
        # Captura cualquier otro error inesperado
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


@ai_bp.route('/ai')
def ai():
    return render_template("ai/ai.html")
