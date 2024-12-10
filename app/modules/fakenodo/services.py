from app.modules.fakenodo.repositories import FakenodoRepository
from core.services.BaseService import BaseService


class FakenodoService(BaseService):
    """
    Servicio para gestionar operaciones relacionadas con Fakenodo.
    Extiende BaseService y utiliza FakenodoRepository.
    """
    def __init__(self, repository=None):
        """
        Inicializa el servicio con un repositorio de Fakenodo.
        Permite la inyección de dependencias para facilitar pruebas.
        """
        super().__init__(repository or FakenodoRepository())

    def get_active_fakenodos(self):
        """
        Recupera todos los Fakenodos con estado 'active'.
        """
        return self.repository.get_by_status("active")

    def count_active_fakenodos(self):
        """
        Cuenta la cantidad de Fakenodos con estado 'active'.
        """
        return self.repository.count_by_status("active")

    def search_fakenodo_by_name(self, name):
        """
        Busca Fakenodos por un nombre parcial.
        """
        return self.repository.search_by_name(name)

    def delete_fakenodo_safe(self, id):
        """
        Elimina un Fakenodo de forma segura.
        Devuelve True si se eliminó correctamente, False si no existe.
        """
        return self.repository.safe_delete(id)
