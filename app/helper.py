from datetime import datetime
from fastapi import HTTPException

def validate_month_year(month: int = None, year: int = None):
    current_year = datetime.now().year
    current_month = datetime.now().month

    # No pueden enviar un mes sin un año
    if month and not year:
        raise HTTPException(status_code=400, detail="Year must be provided if month is specified.")

    # Validar que el año sea válido
    if year and year < 2000:
        raise HTTPException(status_code=400, detail="El año debe ser mayor o igual a 2000.")

    # Validar que el mes sea válido
    if month and (month < 1 or month > 12):
        raise HTTPException(status_code=400, detail="Month must be between 1 and 12.")

    # No permitir fechas en el futuro
    if year and (year > current_year or (year == current_year and month and month > current_month)):
        raise HTTPException(status_code=400, detail="Date cannot be in the future.")
