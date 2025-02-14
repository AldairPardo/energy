from fastapi import FastAPI
from app.service import Service


# Inicializar la app FastAPI
app = FastAPI(title="Energy Billing API")

@app.post("/calculate-invoice", summary = "Calcula la factura para un cliente y un mes específico")
def calculate_invoice(client_id: int, month: int = None, year: int = None):
    return Service.calculate_invoice(client_id, month, year)

@app.get("/client-statistics/{client_id}", summary = "Obtener estadísticas de consumo e inyección de un cliente")
def client_statistics(client_id: int, month: int = None, year: int = None):
    return Service.get_client_statistics(client_id, month, year)

@app.get("/system-load", summary = "Obtener la carga del sistema por hora")
def system_load():
    return Service.get_system_load()

@app.get("/calculate-concept/{concept}", summary="Calcula un concepto específico para un cliente y un mes específico")
def calculate_concept(concept: str, client_id: int, month: int = None, year: int = None):
    return Service.calculate_invoice(client_id, month, year, concept)