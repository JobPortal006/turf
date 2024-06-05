# myapp/models_sqlalchemy.py

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from .sqlalchemy_config import engine

Base = declarative_base()

class MyModel(Base):
    __tablename__ = 'my_model'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    created_at = Column(DateTime)

Base.metadata.create_all(engine)
  