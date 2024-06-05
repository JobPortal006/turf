from sqlalchemy import create_engine, Column, Integer, String, Enum, Date, DECIMAL, Text, TIMESTAMP, DateTime, ForeignKey, text 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base 
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Signup(Base):
    __tablename__ = 'signup'

    id = Column(Integer, primary_key=True, autoincrement=True)
    signup_by = Column(Enum('User', 'Recruiter', name='signup_by_enum'), nullable=False)
    email = Column(String(100), nullable=False)
    mobile_number = Column(String(15), nullable=False)
    password = Column(String(255), nullable=False)
    signup_time = Column(TIMESTAMP, server_default=func.now())
    loggedin_time = Column(TIMESTAMP)


# engine = create_engine('mysql://theuser:thepassword@13.51.66.252:3306/jobportal')
engine = create_engine('mysql://root:mysqllocal@localhost:3306/turfmanagement')
Base.metadata.create_all(engine) 

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Commit the changes   
session.commit()

# Close the session
session.close()
       