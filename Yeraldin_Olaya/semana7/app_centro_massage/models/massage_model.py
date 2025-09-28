# models/massage_model.py
from database import Base
from sqlalchemy import Column, Integer, String


class Massage(Base):
    __tablename__ = "massages"

    id = Column(Integer, primary_key=True, index=True)
    session = Column(String, index=True)
    therapist = Column(String)
    schedule = Column(String)
