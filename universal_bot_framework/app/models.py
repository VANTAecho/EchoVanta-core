from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Bot(Base):
    __tablename__ = 'bots'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
