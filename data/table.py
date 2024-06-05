from sqlalchemy import create_engine, Column, Integer, String, Enum, Date, DECIMAL, Text, ForeignKey, BLOB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Role(Base):
    __tablename__ = 'Role'
    roleid = Column(Integer, primary_key=True, autoincrement=True)
    role = Column(String(50), nullable=False)

class User(Base):
    __tablename__ = 'User'
    userid = Column(Integer, primary_key=True, autoincrement=True)
    roleid = Column(Integer, ForeignKey('Role.roleid'), nullable=False)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    profilephoto = Column(BLOB)
    mobilenumber = Column(String(15), nullable=False)
    
    role = relationship("Role")

class TurfType(Base):
    __tablename__ = 'TurfType'
    turftypeid = Column(Integer, primary_key=True, autoincrement=True)
    turftype = Column(String(50), nullable=False)

class TurfDetails(Base):
    __tablename__ = 'TurfDetails'
    turfid = Column(Integer, primary_key=True, autoincrement=True)
    turftypeid = Column(Integer, ForeignKey('TurfType.turftypeid'), nullable=False)
    turfaddress = Column(String(150), nullable=False)
    turftimings = Column(String(50), nullable=False)
    description = Column(Text)
    partitions = Column(Integer)
    
    turftype = relationship("TurfType")

class GameType(Base):
    __tablename__ = 'GameType'
    gametypeid = Column(Integer, primary_key=True, autoincrement=True)
    gametype = Column(String(50), nullable=False)

class GameDetails(Base):
    __tablename__ = 'GameDetails'
    gameid = Column(Integer, primary_key=True, autoincrement=True)
    turfid = Column(Integer, ForeignKey('TurfDetails.turfid'), nullable=False)
    gametypeid = Column(Integer, ForeignKey('GameType.gametypeid'), nullable=False)
    numberofcourts = Column(Integer, nullable=False)
    noofpersonsinvolved = Column(Integer, nullable=False)
    isforKids = Column(Enum('Yes', 'No'), nullable=False)
    priceperhour = Column(DECIMAL(10, 2), nullable=False)
    
    turfd = relationship("TurfDetails")
    gametype = relationship("GameType")

class UserTurfMapping(Base):
    __tablename__ = 'UserTurfMapping'
    mappingid = Column(Integer, primary_key=True, autoincrement=True)
    userid = Column(Integer, ForeignKey('User.userid'), nullable=False)
    turfid = Column(Integer, ForeignKey('TurfDetails.turfid'), nullable=False)
    
    user = relationship("User")
    turf = relationship("TurfDetails")

class Subscription(Base):
    __tablename__ = 'Subscription'
    subscriptionid = Column(Integer, primary_key=True, autoincrement=True)
    turfid = Column(Integer, ForeignKey('TurfDetails.turfid'), nullable=False)
    subscriptiontype = Column(String(50), nullable=False)
    startdate = Column(Date, nullable=False)
    enddate = Column(Date, nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    status = Column(Enum('Active', 'Expired', 'Cancelled'), nullable=False)
    
    turf = relationship("TurfDetails")

class Bookings(Base):
    __tablename__ = 'Bookings'
    bookingid = Column(Integer, primary_key=True, autoincrement=True)
    userid = Column(Integer, ForeignKey('User.userid'), nullable=False)
    turfid = Column(Integer, ForeignKey('TurfDetails.turfid'), nullable=False)
    bookingtimings = Column(String(50), nullable=False)
    bookingdate = Column(Date, nullable=False)
    bookingprice = Column(DECIMAL(10, 2), nullable=False)
    timeslot = Column(String(50), nullable=False)
    courtnumber = Column(Integer, nullable=False)
    gameid = Column(Integer, ForeignKey('GameDetails.gameid'), nullable=False)
    bookingstatus = Column(Enum('Active', 'Cancelled'), nullable=False)
    
    user = relationship("User")
    turf = relationship("TurfDetails")
    game = relationship("GameDetails")

class MaintenanceSchedules(Base):
    __tablename__ = 'MaintenanceSchedules'
    scheduleid = Column(Integer, primary_key=True, autoincrement=True)
    turfid = Column(Integer, ForeignKey('TurfDetails.turfid'), nullable=False)
    userid = Column(Integer, ForeignKey('User.userid'), nullable=False)
    taskdescription = Column(String(255), nullable=False)
    scheduleddate = Column(Date, nullable=False)
    completiondate = Column(Date)
    notes = Column(String(255), nullable=False)
    
    user = relationship("User")
    turf = relationship("TurfDetails")

class Equipment(Base):
    __tablename__ = 'Equipment'
    equipmentid = Column(Integer, primary_key=True, autoincrement=True)
    equipmentname = Column(String(50), nullable=False)
    equipmenttype = Column(String(50), nullable=False)
    purchasedate = Column(Date, nullable=False)
    maintenancedate = Column(Date, nullable=False)
    condition = Column(String(50), nullable=False)
    turfid = Column(Integer, ForeignKey('TurfDetails.turfid'), nullable=False)
    
    turf = relationship("TurfDetails")

# Create an engine
engine = create_engine('mysql://root:mysqllocal@localhost:3306/turfmanagement')

# Create all tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Commit the changes   
session.commit()

# Close the session
session.close()
