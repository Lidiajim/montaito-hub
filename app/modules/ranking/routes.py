# app/modules/ranking/routes.py
from flask import render_template
from app.modules.dataset.services import DataSetService
from app.modules.ranking import ranking_bp


# Creamos la ruta de ranking para obtener los datasets ordenados por calificación
@ranking_bp.route('/ranking', methods=['GET'])
def ranked_datasets():
    dataset_service = DataSetService()
    ranked_datasets = dataset_service.get_datasets_ordered_by_rating()
    return render_template('ranking/index.html', datasets=ranked_datasets)
