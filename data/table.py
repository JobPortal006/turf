# db_setup.py

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

# Define SQLAlchemy engine and base
DATABASE_URL = 'mysql://root:root123@localhost:3306/deena'
engine = create_engine(DATABASE_URL)
Base = declarative_base(bind=engine)

# Define your SQLAlchemy model
class MyModel(Base):
    __tablename__ = 'my_model'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    created_at = Column(DateTime)

class Developer(Base):
    __tablename__ = 'Developer'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    created_at = Column(DateTime)
    
class Insight(Base):
    __tablename__ = 'Insight'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    created_at = Column(DateTime)    
# Create tables in the database
Base.metadata.create_all(engine)

# Example usage (optional)
from datetime import datetime

# Create a session
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

# Add a record
new_record = MyModel(name='Example Name', created_at=datetime.now())
session.add(new_record)
session.commit()

deena_record = Developer(name='Harideena',created_at=datetime.now())
session.add(deena_record)
session.commit()

print("Tables created successfully and record added.")
