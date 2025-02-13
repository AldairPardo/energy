from app.models import Tariffs
from app.database import db

class TariffRepository:
    @staticmethod
    def get_tariff_by_client(client):
        query = db.query(Tariffs).filter_by(
            id_market=client.id_market,
            voltage_level=client.voltage_level
        )
        if client.voltage_level not in [2, 3]:
            query = query.filter_by(cdi=client.cdi)
        
        tariffs = query.first()
        return tariffs