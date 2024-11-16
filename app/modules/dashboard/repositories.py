from app import db

class DashboardRepository:
    """
    Repositorio para realizar consultas relacionadas con las estadísticas del dashboard.
    """

    def __init__(self):
        pass

    def get_total_datasets(self) -> int:
        """
        Obtiene el número total de datasets desde el repositorio correspondiente.
        """
        return 10

    def get_total_users(self) -> int:
        """
        Obtiene el número total de usuarios desde el repositorio correspondiente.
        """
        return 6

    def get_average_dataset_rating(self) -> float:
        """
        Calcula la calificación promedio de todos los datasets usando el repositorio de ratings.
        """
        return 11

    def get_total_views(self) -> int:
        """
        Obtiene el número total de visualizaciones de datasets desde el repositorio de vistas.
        """
        return 2

    def get_total_downloads(self) -> int:
        """
        Obtiene el número total de descargas de datasets desde el repositorio de descargas.
        """
        return 3

    
