from app.modules.fakenodo.models import Fakenodo
from core.repositories.BaseRepository import BaseRepository


class FakenodoRepository(BaseRepository):
    def __init__(self, model=None):
        """
        Permite inyección de un modelo específico, útil para pruebas.
        """
        super().__init__(model or Fakenodo)

