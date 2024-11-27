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
        response_text = "Los datasets más recientes son\n" + str(dataset_service.latest_synchronized())
        
    if response_text == 'feature-latest':
        response_text = "Los features más recientes son\n" + str(feature_model_service.latest_feature_models())
        
    return jsonify({"response": response_text})


@ai_bp.route('/ai')
def ai():
    return render_template("ai/ai.html")
