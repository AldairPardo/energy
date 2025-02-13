from app.models import Services
from app.database import db

class ServiceRepository:
    @staticmethod
    def get_client(client_id: int):
        # Obtener cliente
        client = db.query(Services).filter_by(id_service=client_id).first()
        return client