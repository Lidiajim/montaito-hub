
from sqlalchemy import func
from app.modules.featuremodel.models import FMMetaData, FeatureModel
from core.repositories.BaseRepository import BaseRepository
from app.modules.dataset.models import DataSet

class FeatureModelRepository(BaseRepository):
    def __init__(self):
        super().__init__(FeatureModel)

    def count_feature_models(self) -> int:
        max_id = self.model.query.with_entities(func.max(self.model.id)).scalar()
        return max_id if max_id is not None else 0
    
    def count_feature_models_by_user_id(self, user_id) -> int:
        """
        Cuenta el número total de Feature Models asociados a un usuario específico.
        """
        count = (
            self.model.query
            .join(DataSet, self.model.data_set_id == DataSet.id)  # Relaciona FeatureModel con DataSet
            .filter(DataSet.user_id == user_id)  # Filtra por user_id en DataSet
            .count()
        )
        return count

class FMMetaDataRepository(BaseRepository):
    def __init__(self):
        super().__init__(FMMetaData)
