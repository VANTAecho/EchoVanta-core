from sqlalchemy import Column, String, Boolean, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid
from datetime import datetime

Base = declarative_base()


def generate_uuid():
    return str(uuid.uuid4())


class Bot(Base):
    __tablename__ = 'bots'
    id = Column(String, primary_key=True, default=generate_uuid)
    name = Column(String)
    type = Column(String)
    platform = Column(String)
    owner_id = Column(String)
    config = Column(JSON)
    enabled = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
