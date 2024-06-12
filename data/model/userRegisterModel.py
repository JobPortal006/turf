from sqlalchemy.orm import sessionmaker
from data.table.table import engine, Roles, User
from data import message, jwtToken

Session = sessionmaker(bind=engine)

def userRegisterInsertQuery(mobileNumber, userName):
    session = Session()
    try:
        role = session.query(Roles).filter_by(role='user').first()
        if not role: 
            return False
        
        roleId = role.roleId
        print("Role ID:", roleId)
        
        user = session.query(User).filter_by(mobileNumber=mobileNumber).first()
        if user:
            return False
        else:
            new_user = User(roleId=roleId, userName=userName, mobileNumber=mobileNumber)
            session.add(new_user)
            session.commit()
            userId = new_user.userId

            jwtTokenEn = jwtToken.jwtTokenEncode(userId, roleId, mobileNumber)
        return jwtTokenEn
    except Exception as e:
        print(f"Error: {e}")
        session.rollback()
        return message.handleSuccess("Error occurred during insertion")
    finally:
        session.close()  

def userRegisterSelectQuery(token):
    session = Session()
    try:
        jwtTokenDecode = jwtToken.decodeToken(token)
        userId = jwtTokenDecode['userId']

        user = session.query(User).filter_by(userId=userId).first()
        if user:
            response = {
                "userId": user.userId,
                "roleId": user.roleId,
                "mobileNumber": user.mobileNumber
            }
        else:
            return False
        return response
    except Exception as e:
        return message.tryExceptError(str(e))
    finally:
        session.close()

def userRegisterUpdateQuery(userName, mobileNumber, token):
    session = Session()
    try:
        jwtTokenDecode = jwtToken.decodeToken(token)
        userId = jwtTokenDecode['userId']

        user = session.query(User).filter_by(userId=userId).first()
        if not user:
            return False

        user.userName = userName
        user.mobileNumber = mobileNumber
        session.commit()

        jwtTokenEncode = jwtToken.jwtTokenEncode(user.userId, user.roleId, user.mobileNumber)
        return jwtTokenEncode
    except Exception as e:
        session.rollback()
        return message.tryExceptError(str(e))
    finally:
        session.close()

def userRegisterDeleteQuery(token):
    session = Session()
    try:
        jwtTokenDecode = jwtToken.decodeToken(token)
        userId = jwtTokenDecode['userId']

        user = session.query(User).filter_by(userId=userId).first()
        if not user:
            return False

        session.delete(user)
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        return message.tryExceptError(str(e))
    finally:
        session.close()
