from flask import render_template, jsonify, request
from app.modules.auth.services import AuthenticationService
from app.modules.featuremodel import featuremodel_bp
from app.modules.featuremodel.services import FeatureModelService

feature_model_service = FeatureModelService


@featuremodel_bp.route('/featuremodel', methods=['GET'])
def index():
    return render_template('featuremodel/index.html')


@featuremodel_bp.route('/featuremodel/<int:feature_model_id>/average_rating', methods=['GET'])
def get_average_rating(feature_model_id):
    feature_model_service = FeatureModelService()
    avg_rating = feature_model_service.get_average_rating(feature_model_id)
    return jsonify({"average_rating": avg_rating}), 200


@featuremodel_bp.route('/featuremodel/<int:feature_model_id>/rate', methods=['POST'])
def rate_feature_model(feature_model_id):
    current_user = AuthenticationService().get_authenticated_user()  # Verifica si el usuario está logueado
    if not current_user:
        return jsonify({"error": "Debes estar logueado para calificar"}), 401  # Si no está logueado

    rating = request.json.get('rating')
    if not rating:
        return jsonify({"error": "La calificación es obligatoria"}), 400

    feature_model_service = FeatureModelService()
    try:
        rating_obj = feature_model_service.rate_dataset(feature_model_id, current_user.id, rating)
        return jsonify({"message": "Calificación guardada", "rating": rating_obj.rating}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400  # Si la calificación no es válida (fuera de rango)
        