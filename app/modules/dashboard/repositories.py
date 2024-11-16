from app.modules.auth.models import User  
from app.modules.dataset.repositories import DataSetRepository, DSDownloadRecordRepository, DSViewRecordRepository
from app.modules.dataset.models import DataSet, DatasetRating, DSViewRecord  
from app.modules.featuremodel.repositories import FeatureModelRepository  
from app import db  
from sqlalchemy import func  

class DashboardRepository:
    
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
        return dataset_views

    def get_total_downloads(self) -> int:
        """
        Obtiene el número total de descargas de datasets y modelos de características.
        """
        dataset_downloads = self.ds_download_record_repository.total_dataset_downloads()
        return dataset_downloads

    def get_average_dataset_rating(self) -> float:
        """
        Calcula la calificación promedio de todos los datasets.
        """
        avg_rating = db.session.query(func.avg(DatasetRating.rating)).scalar()
        return round(avg_rating, 1) if avg_rating is not None else 0.0

        ###################################################### user id ##########################

    def get_total_datasets_by_user_id(self, user_id) -> int:
        """
        Obtiene el número total de datasets asociados a un usuario específico.
        """
        total_datasets_count = db.session.query(DataSet).filter(DataSet.user_id == user_id).count()
        return total_datasets_count 

    def get_average_dataset_rating_by_user_id(self, user_id) -> float:
        """
        Calcula la calificación promedio de todos los datasets asociados a un usuario específico.
        """
        avg_rating = (
            db.session.query(func.avg(DatasetRating.rating))
            .join(DataSet, DatasetRating.dataset_id == DataSet.id) 
            .filter(DataSet.user_id == user_id)  
            .scalar()
        )
        return round(avg_rating, 1) if avg_rating is not None else 0.0

    def get_total_views_by_user_id(self, user_id) -> int:
        """
        Obtiene el número total de visualizaciones de datasets asociados a un usuario específico.
        """
        number_views = (
            db.session.query(func.count(DSViewRecord.id))
            .join(DataSet, DSViewRecord.dataset_id == DataSet.id)  
            .filter(DataSet.user_id == user_id)  
            .scalar() 
        )
        return number_views


    def get_total_downloads_by_user_id(self, user_id) -> int:
        """
        Obtiene el número total de descargas de datasets asociados a un usuario específico.
        """
        return self.ds_download_record_repository.total_dataset_downloads_by_user_id(user_id)


    def get_total_feature_models_by_user_id(self, user_id) -> int:
        """
        Obtiene el número total de modelos de características.
        """
        return self.feature_model_repository.count_feature_models_by_user_id(user_id)