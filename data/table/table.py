from sqlalchemy import create_engine, Column, Integer, String, Enum, Date, DECIMAL, Text, ForeignKey, BLOB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from ..sqlalchemyConfig import DATABASE_URL

Base = declarative_base()

class Login(Base):
    __tablename__ = 'login'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)

class Roles(Base):
    __tablename__ = 'roles'
    roleId = Column(Integer, primary_key=True, autoincrement=True)
    role = Column(String(50), nullable=False)

class User(Base):
    __tablename__ = 'user'
    userId = Column(Integer, primary_key=True, autoincrement=True)
    roleId = Column(Integer, ForeignKey('role.roleId'), nullable=False)
    userName = Column(String(50), nullable=True)
    password = Column(String(50), nullable=True)
    email = Column(String(100),nullable=True)
    profilePhoto = Column(String(50),nullable=True)
    mobileNumber = Column(String(15) , nullable=True)
    
    role = relationship("Role")

class Location(Base):
    __tablename__ = 'location'
    locationId = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, ForeignKey('user.userId'), nullable=False)
    doorNo = Column(Integer, nullable=False)
    street = Column(String(50), nullable=False)
    city = Column(String(20),nullable=False)
    state = Column(String(50),nullable=False)
    pincode = Column(String(15) , nullable=False)

    user = relationship("User")

class UserSportsInterests(Base):
    __tablename__ = 'userSportsInterests'
    userSportsInterestsId = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, ForeignKey('user.userId'), nullable=False)
    gameTypeId = Column(Integer, ForeignKey('gameType.gameTypeId'), nullable=False)
      
    user = relationship("User")
    gameType = relationship("GameType")

class TurfType(Base):
    __tablename__ = 'turfType'
    turfTypeId = Column(Integer, primary_key=True, autoincrement=True)
    turfType = Column(String(50), nullable=False)

class TurfDetails(Base):
    __tablename__ = 'turfDetails'
    turfId = Column(Integer, primary_key=True, autoincrement=True)
    courtName = Column(String(50), nullable=False)
    turfTypeId = Column(Integer, ForeignKey('turfType.turfTypeId'), nullable=False)
    turfAddress = Column(String(150), nullable=False)
    turfTimings = Column(String(50), nullable=False)
    description = Column(Text)
    partitions = Column(Enum('Yes', 'No'))
    
    turfType = relationship("TurfType")

class GameType(Base):
    __tablename__ = 'gameType'
    gameTypeId = Column(Integer, primary_key=True, autoincrement=True)
    gameType = Column(String(50), nullable=False)

class GameDetails(Base):
    __tablename__ = 'gameDetails'
    gameId = Column(Integer, primary_key=True, autoincrement=True)
    turfId = Column(Integer, ForeignKey('turfDetails.turfId'), nullable=False)
    gameTypeId = Column(Integer, ForeignKey('gameType.gameTypeId'), nullable=False)
    numberOfCourts = Column(Integer, nullable=False)
    noOfPersonsInvolved = Column(Integer, nullable=False)
    isForKids = Column(Enum('Yes', 'No'), nullable=False)
    pricePerHour = Column(DECIMAL(10, 2), nullable=False)
    
    turfDetails = relationship("TurfDetails")
    gameType = relationship("GameType")
 
class UserTurfMapping(Base):
    __tablename__ = 'userTurfMapping'
    mappingId = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, ForeignKey('user.userId'), nullable=False)
    turfId = Column(Integer, ForeignKey('turfDetails.turfId'), nullable=False)
    
    user = relationship("User")
    turfDetails = relationship("TurfDetails")

class Subscription(Base):
    __tablename__ = 'subscription'
    subscriptionId = Column(Integer, primary_key=True, autoincrement=True)
    turfId = Column(Integer, ForeignKey('turfDetails.turfId'), nullable=False)
    subscriptionType = Column(String(50), nullable=False)
    startDate = Column(Date, nullable=False)
    endDate = Column(Date, nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    status = Column(Enum('Active', 'Expired', 'Cancelled'), nullable=False)
    
    turfDetails = relationship("TurfDetails")

class Bookings(Base):
    __tablename__ = 'bookings'
    bookingId = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer, ForeignKey('user.userId'), nullable=False)
    turfId = Column(Integer, ForeignKey('turfDetails.turfId'), nullable=False)
    bookingTimings = Column(String(50), nullable=False)
    bookingDate = Column(Date, nullable=False)
    bookingPrice = Column(DECIMAL(10, 2), nullable=False)
    timeSlot = Column(String(50), nullable=False)
    courtNumber = Column(Integer, nullable=False)
    gameId = Column(Integer, ForeignKey('gameDetails.gameId'), nullable=False)
    bookingStatus = Column(Enum('Active', 'Cancelled'), nullable=False)
    
    user = relationship("User")
    turfDetails = relationship("TurfDetails")
    gameDetails = relationship("GameDetails")

class MaintenanceSchedules(Base):
    __tablename__ = 'maintenanceSchedules'
    scheduleId = Column(Integer, primary_key=True, autoincrement=True)
    turfId = Column(Integer, ForeignKey('turfDetails.turfId'), nullable=False)
    userId = Column(Integer, ForeignKey('user.userId'), nullable=False)
    taskDescription = Column(String(255), nullable=False)
    scheduledDate = Column(Date, nullable=False)
    completionDate = Column(Date)
    notes = Column(String(255), nullable=False)
    
    user = relationship("User")
    turfDetails = relationship("TurfDetails")

class Equipment(Base):
    __tablename__ = 'equipment'
    equipmentId = Column(Integer, primary_key=True, autoincrement=True)
    equipmentName = Column(String(50), nullable=False)
    equipmentType = Column(String(50), nullable=False)
    purchaseDate = Column(Date, nullable=False)
    maintenanceDate = Column(Date, nullable=False)
    condition = Column(String(50), nullable=False)
    turfId = Column(Integer, ForeignKey('turfDetails.turfId'), nullable=False)
    
    turfDetails = relationship("TurfDetails")

# Create an engine
engine = create_engine(DATABASE_URL)

# Create all tables
Base.metadata.create_all(engine)  

# Create a session
Session = sessionmaker(bind=engine)
session = Session()
    
# Commit the changes   
session.commit()

# Close the session
session.close()
