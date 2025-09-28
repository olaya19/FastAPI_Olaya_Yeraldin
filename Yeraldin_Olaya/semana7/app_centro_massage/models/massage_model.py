# models/massage_model.py
from sqlalchemy import Column, Integer, String
from database import Base

class Massage(Base):
    __tablename__ = "massages"

    id = Column(Integer, primary_key=True, index=True)
    session = Column(String, index=True)
    therapist = Column(String)
    schedule = Column(String)
