from sqlalchemy import Column, Integer, Float, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from .database import Base

# Tabla records
class Records(Base):
    __tablename__ = "records"
    
    id_record = Column(Integer, primary_key=True, index=True)
    id_service = Column(Integer, ForeignKey("services.id_service"))
    record_timestamp = Column(TIMESTAMP, ForeignKey("xm_data_hourly_per_agent.record_timestamp"))

    service = relationship("Services", back_populates="records")
    xm_data_hourly_per_agent = relationship("XmDataHourlyPerAgent", back_populates="record")

# Tabla services
class Services(Base):
    __tablename__ = "services"

    id_service = Column(Integer, primary_key=True, index=True)
    id_market = Column(Integer)
    cdi = Column(Integer)
    voltage_level = Column(Integer)

    records = relationship("Records", back_populates="service")

# Tabla tariffs
class Tariffs(Base):
    __tablename__ = "tariffs"

    id_market = Column(Integer, primary_key=True)
    cdi = Column(Integer, primary_key=True)
    voltage_level = Column(Integer, primary_key=True)

    G = Column(Float)
    T = Column(Float)
    D = Column(Float)
    R = Column(Float)
    C = Column(Float)
    P = Column(Float)
    CU = Column(Float)

# Tabla consumption
class Consumption(Base):
    __tablename__ = "consumption"

    id_record = Column(Integer, ForeignKey("records.id_record"), primary_key=True)
    value = Column(Float)

# Tabla injection
class Injection(Base):
    __tablename__ = "injection"

    id_record = Column(Integer, ForeignKey("records.id_record"), primary_key=True)
    value = Column(Float)

# Tabla xm_data_hourly_per_agent
class XmDataHourlyPerAgent(Base):
    __tablename__ = "xm_data_hourly_per_agent"

    record_timestamp = Column(TIMESTAMP, primary_key=True)
    value = Column(Float)
    
    record = relationship("Records", back_populates="xm_data_hourly_per_agent")
