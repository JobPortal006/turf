from sqlalchemy.orm import sessionmaker
from data.table.table import engine, Roles, User
from data import message

Session = sessionmaker(bind=engine)

def userLoginQuery(mobileNumber,role_table,user_table):
    session = Session()
    try:
        role_columns = role_table['columns']
        user_columns = user_table['columns']
        
        # Check if the role 'User' exists
        role = session.query(Roles).filter_by(**{role_columns['role']: 'User'}).first()

        roleId = getattr(role, role_columns['roleId'])
        role_name = getattr(role, role_columns['role'])
        print("userLoginModel Role ID:", roleId)
        
        # Check if the mobile number already exists
        user = session.query(User).filter_by(**{user_columns['mobileNumber']: mobileNumber}).first()
        if user:
            userId = getattr(user, user_columns['userId'])
            return userId, role_name
        else:
            # Create and add the new user
            new_user = User(**{user_columns['roleId']: roleId, user_columns['mobileNumber']: mobileNumber})
            session.add(new_user)
            session.commit()
            userId = getattr(new_user, user_columns['userId'])
            
            # Return success message
            return userId, role_name
    except Exception as e:
        print(f"userLoginModel Error: {e}")
        session.rollback()
        return message.tryExceptError(str(e))
    finally:
        session.close()
