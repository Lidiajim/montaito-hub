from app.modules.fakenodo.models import Fakenodo
from core.repositories.BaseRepository import BaseRepository
from sqlalchemy.exc import SQLAlchemyError


class FakenodoRepository(BaseRepository):
    """
    Repositorio específico para el modelo Fakenodo.
    Proporciona métodos adicionales para consultas personalizadas.
    """
    def __init__(self, model=None):
        """
        Permite inyección de un modelo específico, útil para pruebas.
        """
        super().__init__(model or Fakenodo)

    def get_by_status(self, status):
        """
        Obtiene todos los Fakenodos con un estado específico.
        :param status: Estado a filtrar (ejemplo: 'active')
        :return: Lista de Fakenodos con el estado dado.
        """
        try:
            return self.model.query.filter_by(status=status).all()
        except SQLAlchemyError as e:
            print(f"Error al obtener Fakenodos por estado: {e}")
            return []

    def count_by_status(self, status):
        """
        Cuenta la cantidad de Fakenodos por estado.
        :param status: Estado a filtrar.
        :return: Número total de Fakenodos con el estado dado.
        """
        try:
            return self.model.query.filter_by(status=status).count()
        except SQLAlchemyError as e:
            print(f"Error al contar Fakenodos por estado: {e}")
            return 0

    def search_by_name(self, name):
        """
        Busca Fakenodos cuyo nombre coincida parcialmente.
        :param name: Nombre o parte del nombre.
        :return: Lista de Fakenodos encontrados.
        """
        try:
            return self.model.query.filter(self.model.name.ilike(f"%{name}%")).all()
        except SQLAlchemyError as e:
            print(f"Error al buscar Fakenodos por nombre: {e}")
            return []

    def safe_delete(self, id):
        """
        Elimina un Fakenodo de forma segura si existe.
        :param id: ID del Fakenodo.
        :return: True si se eliminó correctamente, False si no existe.
        """
        try:
            obj = self.get_by_id(id)
            if obj:
                self.delete(obj)
                return True
            return False
        except SQLAlchemyError as e:
            print(f"Error al eliminar el Fakenodo: {e}")
            return False
