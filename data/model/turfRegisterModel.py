from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..table.table import Roles, User, TurfDetails, UserTurfMapping
from ..sqlalchemyConfig import DATABASE_URL

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def create_user_and_turf(data):
    session = Session()
    try:
        roleName = "Turf Admin"
        role = session.query(Roles).filter(Roles.role == roleName).first()

        new_user = User(
            roleId=role.roleId,
            userName=f"{data['firstName']} {data['lastName']}",
            email=data['email'],
            profilePhoto=data['profilePhoto'],
            mobileNumber=data['mobileNumber']
        )
        session.add(new_user)
        session.commit()

        new_turf = TurfDetails(
            courtName=data['courtName'],
            turfAddress=data['location'],
            description=data['description']
        )
        session.add(new_turf)
        session.commit()

        new_mapping = UserTurfMapping(
            userId=new_user.userId,
            turfId=new_turf.turfId
        )
        session.add(new_mapping)
        session.commit()

        return True, "Success"
    except Exception as e:
        session.rollback()
        return False, str(e)
    finally:
        session.close()
