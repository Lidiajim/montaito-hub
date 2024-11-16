from app.modules.dashboard.repositories import DashboardRepository
from core.services.BaseService import BaseService


class DashboardService(BaseService):
    def __init__(self):
        super().__init__(DashboardRepository())

    def get_dashboard_public_data(self):

        
            return {
                "total_datasets": self.repository.get_total_datasets(),
                "total_users": self.repository.get_total_users(),
                "average_rating": self.repository.get_average_dataset_rating(),
                "total_views": self.repository.get_total_views(),
                "total_downloads": self.repository.get_total_downloads(),
                "total_features": self.repository.get_total_feature_models()

                            }


    def get_dashboard_user_data(self, user_id):

        return {
            "total_datasets": self.repository.get_total_datasets_by_user_id(user_id),
            "average_rating": self.repository.get_average_dataset_rating_by_user_id(user_id),
            "total_views": self.repository.get_total_views_by_user_id(user_id),
            "total_downloads": self.repository.get_total_downloads_by_user_id(user_id),
            "total_features": self.repository.get_total_feature_models_by_user_id(user_id)



        }