from app import db
from datetime import datetime


class Fakenodo(db.Model):
    __tablename__ = "fakenodos"  # Nombre explícito de la tabla

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False, unique=True)  # Nombre del nodo
    status = db.Column(db.String(20), nullable=False, default="active")  # Estado: active/inactive
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        """
        Representación en cadena del objeto.
        """
        return f"<Fakenodo id={self.id}, name='{self.name}', status='{self.status}'>"

    def to_dict(self):
        """
        Serializa el objeto a un diccionario.
        """
        return {
            "id": self.id,
            "name": self.name,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data):
        """
        Crea una instancia de Fakenodo a partir de un diccionario.
        """
        return cls(
            name=data.get("name"),
            status=data.get("status", "active"),  # Por defecto, el status es 'active'
        )
