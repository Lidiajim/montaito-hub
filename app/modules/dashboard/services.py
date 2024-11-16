from app.modules.dashboard.repositories import DashboardRepository
from core.services.BaseService import BaseService


class DashboardService(BaseService):
    def __init__(self):
        super().__init__(DashboardRepository())

    def get_dashboard_data(self):

        
            return {
                "total_datasets": self.repository.get_total_datasets(),
                "total_users": self.repository.get_total_users(),
                "average_rating": self.repository.get_average_dataset_rating(),
                "total_views": self.repository.get_total_views(),
                "total_downloads": self.repository.get_total_downloads()
                            }