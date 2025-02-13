from app.models import Records, Consumption, Injection, XmDataHourlyPerAgent
from sqlalchemy.sql import func
from sqlalchemy import extract
from app.database import db
import pandas as pd


class RecordRepository:

    def get_data(client_id, year=None, month=None):
        # Unir Injection con Records y XMDataHourlyPerAgent
        query = db.query(
            Records.record_timestamp,
            Consumption.value.label("consumption"),
            Injection.value.label("injection"),
            XmDataHourlyPerAgent.value.label("tariff")
        ).join(Consumption, Consumption.id_record == Records.id_record)\
         .join(Injection, Injection.id_record == Records.id_record)\
         .join(XmDataHourlyPerAgent, XmDataHourlyPerAgent.record_timestamp == Records.record_timestamp)\
         .filter(Records.id_service == client_id)
        
        if year and month:
            query = query.filter(
                extract('year', Records.record_timestamp) == year,
                extract('month', Records.record_timestamp) == month
            )
        
        query_data = query.all()

        df = pd.DataFrame(query_data, columns=["timestamp", "consumption", "injection", "tariff"])
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df.fillna(0, inplace=True)
        
        return df
    
    @staticmethod
    def get_system_load():
        load = db.query(
            Records.record_timestamp,
            func.sum(Consumption.value).label("total_consumption"),
            func.sum(Injection.value).label("total_injection"),
            (func.sum(Consumption.value) - func.sum(Injection.value)).label("net_load")
        ).join(Consumption, Consumption.id_record == Records.id_record)\
         .join(Injection, Injection.id_record == Records.id_record)\
         .group_by(Records.record_timestamp)\
         .all()
        
        return [row._asdict() for row in load]