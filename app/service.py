from .repositories.service_repository import ServiceRepository
from .repositories.tariff_repository import TariffRepository
from .repositories.record_repository import RecordRepository
from .helper import validate_month_year

class Service:
    
    @staticmethod
    def calculate_invoice(client_id: int, month: int, year: int, concept: str = "all"):
        # Validar mes y año
        validate_month_year(month, year)
        
        # Obtener data
        df = RecordRepository.get_data(client_id, year, month)
        
        consumption_kwh = df["consumption"].sum()
        injection_kwh = df["injection"].sum()
        
        # Obtener cliente
        client = ServiceRepository.get_client(client_id)
        
        # Obtener tarifa
        tariffs = TariffRepository.get_tariff_by_client(client)
        
        # Calcular totales
        ea = consumption_kwh * tariffs.CU
        ec = injection_kwh * tariffs.C
        ee1 = min(consumption_kwh, injection_kwh) * -tariffs.CU
        ee2 = 0
        ee2 = Service.calculate_ee2(df, consumption_kwh) if (concept == "all" or concept == "ee2") and injection_kwh > consumption_kwh else 0
        
        # Switch concepto 
        if concept == "ea":
            return {"EA": ea}
        elif concept == "ec":
            return {"EC": ec}
        elif concept == "ee1":
            return {"EE1": ee1}
        elif concept == "ee2":
            return {"EE2": ee2}
        else:
            return {
            "EA": ea,
            "EC": ec,
            "EE1": ee1,
            "EE2": ee2
            }
    
    @staticmethod
    def calculate_ee2(df, consumption_kwh):
        # Nueva columna 'EE2'
        df["EE2"] = 0.0
        for index, row in df.iterrows():
            df.at[index, "EE2"] = Service.calculate_ee2_value(row, df, consumption_kwh)
        
        # Calcular EE2
        df["EE2_cost"] = df["EE2"] * df["tariff"]  # Multiplicar por la tarifa
        ee2 = df["EE2_cost"].sum()
        
        return ee2
    
    @staticmethod
    def calculate_ee2_value(row, df, consumption_kwh):
        injection_sum = df.loc[:row.name, "injection"].sum()
        previous_value = df["EE2"].iloc[:row.name].sum() if row.name > 0 else 0
        result = max(0, injection_sum - consumption_kwh - previous_value)
        
        return result
    
    @staticmethod
    def get_system_load():
        return RecordRepository.get_system_load()
    
    @staticmethod
    def get_client_statistics(client_id: int, month: int, year: int):
        # Validar mes y año
        validate_month_year(month, year)
        
        # Obtener data
        df = RecordRepository.get_data(client_id, year, month)
        
        consumption_kwh = df["consumption"].sum()
        injection_kwh = df["injection"].sum()
        
        statistics = df[["timestamp", "consumption", "injection", "tariff"]].to_dict(orient="records")
        
        return {
            "client_id": client_id,
            "total_consumption": consumption_kwh,
            "total_injection": injection_kwh,
            "balance": consumption_kwh - injection_kwh,
            "statistics": statistics
        }