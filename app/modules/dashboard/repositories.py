from app.modules.auth.models import User  # Asegúrate de importar tu modelo de usuario
from app.modules.dataset.repositories import (
    DataSetRepository, 
    DSDownloadRecordRepository, 
    DSViewRecordRepository
)
from app.modules.featuremodel.repositories import FeatureModelRepository
from app.modules.dataset.models import DatasetRating
from app import db
from sqlalchemy import func

class DashboardRepository:
    """
    Repositorio para realizar consultas relacionadas con las estadísticas del dashboard.
    """

    def __init__(self):
        self.dataset_repository = DataSetRepository()
        self.feature_model_repository = FeatureModelRepository()
        self.ds_download_record_repository = DSDownloadRecordRepository()
        self.ds_view_record_repository = DSViewRecordRepository()

    def get_total_datasets(self) -> int:
        """
        Obtiene el número total de datasets sincronizados.
        """
        return self.dataset_repository.count_synchronized_datasets()

    def get_total_feature_models(self) -> int:
        """
        Obtiene el número total de modelos de características.
        """
        return self.feature_model_repository.count_feature_models()

    def get_total_users(self) -> int:
        """
        Obtiene el número total de usuarios registrados.
        """
        return db.session.query(func.count(User.id)).scalar()

    def get_total_views(self) -> int:
        """
        Obtiene el número total de visualizaciones de datasets y modelos de características.
        """
        dataset_views = self.ds_view_record_repository.total_dataset_views()
        # Agrega lógica adicional para modelos de características si aplica
        return dataset_views

    def get_total_downloads(self) -> int:
        """
        Obtiene el número total de descargas de datasets y modelos de características.
        """
        dataset_downloads = self.ds_download_record_repository.total_dataset_downloads()
        # Agrega lógica adicional para modelos de características si aplica
        return dataset_downloads

    def get_average_dataset_rating(self) -> float:
        """
        Calcula la calificación promedio de todos los datasets.
        """
        avg_rating = db.session.query(func.avg(DatasetRating.rating)).scalar()
        return avg_rating if avg_rating is not None else 0.0
