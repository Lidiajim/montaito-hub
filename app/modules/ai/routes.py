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
    user_message = request.json.get('text')
           
    response_text = ai_service.detect_intent_texts(project_id, "unique-session-id", user_message, language_code)
    
    if response_text == 'dataset-numero':
        datasets_counter = dataset_service.count_synchronized_datasets()
        response_text = "Los datasets disponibles son\n" + str(datasets_counter)
        
    if response_text == 'feature-number':
        feature_models_counter = feature_model_service.count_feature_models()
        response_text = "Los features disponibles son\n" + str(feature_models_counter)
        
    if response_text == 'dataset-downloads':
        total_dataset_downloads = dataset_service.total_dataset_downloads()
        response_text = "El total de descargas de datasets es\n" + str(total_dataset_downloads)
        
    if response_text == 'feature-downloads':
        total_feature_model_downloads = feature_model_service.total_feature_model_downloads()
        response_text = "El total de descargas de features es\n" + str(total_feature_model_downloads)
        
    if response_text == 'dataset-views':
        total_dataset_views = dataset_service.total_dataset_views()
        response_text = "El total de visualizaciones de datasets es\n" + str(total_dataset_views)
        
    if response_text == 'feature-views':
        total_feature_model_views = feature_model_service.total_feature_model_views()
        response_text = "El total de visualizaciones de features es\n" + str(total_feature_model_views)
        
    if response_text == 'dataset-latest':
        latest_datasets = dataset_service.latest_synchronized()
        dataset_names = [str(dataset.id) for dataset in latest_datasets]  # Convertir a cadenas
        response_text = "Los datasets más recientes son:\n" + "\n".join(dataset_names)
        
    if response_text.startswith('dataset-get'):
        dataset_id = response_text.split(',')[-1]
        dataset = dataset_service.get_by_id(dataset_id)
        if dataset is None:
            response_text = "no se encontró el dataset"
        else:
            dataset = dataset.to_dict()
            response_text = format_dataset_response(dataset)
    
    if response_text.startswith('feature-get'):
        feature_model_id = response_text.split(',')[-1]
        feature_model = feature_model_service.get_by_id(feature_model_id)
        if feature_model is None:
            response_text = "no se encontró el feature"
        else:
            response_text = feature_model
        
    return jsonify({"response": response_text})


@ai_bp.route('/ai')
def ai():
    return render_template("ai/ai.html")
