from sqlalchemy.orm import sessionmaker
from data.table.table import engine, Roles, User
from data import message

Session = sessionmaker(bind=engine)

def turfAdminLoginQuery(email, password,role_table,user_table):
    session = Session()
    try:
        role_columns = role_table['columns']
        user_columns = user_table['columns']
        
        # Check if the role 'Turf Admin' exists
        role = session.query(Roles).filter_by(**{role_columns['role']: 'Turf Admin'}).first()

        roleId = getattr(role, role_columns['roleId'])
        role_name = getattr(role, role_columns['role'])
        print("turfAdminLoginQuery Role ID:", roleId)
        
        # Check if the email is match an existing user with the 'Turf Admin' role
        user = session.query(User).filter_by(
            **{user_columns['email']: email, user_columns['roleId']: roleId}
        ).first()
        
        if user:
            userId = getattr(user, user_columns['userId'])
            return userId, role_name
        else:
            return None, None
            
    except Exception as e:
        print(f"turfAdminLoginQuery Error: {e}")
        session.rollback()
        return message.tryExceptError(str(e))
    finally:
        session.close()
