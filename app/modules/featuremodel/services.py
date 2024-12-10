from app.modules.featuremodel.repositories import FMMetaDataRepository, FeatureModelRepository
from app.modules.featuremodel.models import FeatureModelRating
from app import db
from sqlalchemy import func
from app.modules.hubfile.services import HubfileService
from core.services.BaseService import BaseService


class FeatureModelService(BaseService):
    def __init__(self):
        super().__init__(FeatureModelRepository())
        self.hubfile_service = HubfileService()

    def total_feature_model_views(self) -> int:
        return self.hubfile_service.total_hubfile_views()

    def total_feature_model_downloads(self) -> int:
        return self.hubfile_service.total_hubfile_downloads()

    def count_feature_models(self):
        return self.repository.count_feature_models()

    def rate_dataset(self, feature_model_id: int, user_id: int, rating: int) -> FeatureModelRating:
        if rating < 1 or rating > 5:
            raise ValueError("La calificación debe estar entre 1 y 5")

        existing_rating = (
            db.session.query(FeatureModelRating)
            .filter_by(feature_model_id=feature_model_id, user_id=user_id)
            .first())
        
        if existing_rating:
            existing_rating.rating = rating
        else:
            new_rating = FeatureModelRating(feature_model_id=feature_model_id, user_id=user_id, rating=rating)
            db.session.add(new_rating)
        
        db.session.commit()
        return existing_rating if existing_rating else new_rating
    
    def get_average_rating(self, feature_model_id: int) -> float:
        avg_rating = (
            db.session.query(func.avg(FeatureModelRating.rating))
            .filter_by(feature_model_id=feature_model_id)
            .scalar())
        return avg_rating if avg_rating is not None else 0.0  

    class FMMetaDataService(BaseService):
        def __init__(self):
            super().__init__(FMMetaDataRepository())