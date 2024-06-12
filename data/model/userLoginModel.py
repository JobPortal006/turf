from sqlalchemy.orm import sessionmaker
from data.table.table import engine, Roles, User
from data import message
from ..table.tablecontent import TABLES

Session = sessionmaker(bind=engine)

def get_table_info(table_name):
    for table in TABLES:
        if table['tableName'] == table_name:
            return table
    return None

def userLoginModel(mobileNumber):
    session = Session()
    try:
        # Get table info for 'role' and 'user'
        role_table = get_table_info('role')
        user_table = get_table_info('user')

        if not role_table or not user_table:
            raise ValueError("Table information not found in TABLES")

        role_columns = role_table['columns']
        user_columns = user_table['columns']
        # Check if the role 'User' exists
        role = session.query(Roles).filter_by(**{role_columns['role']: 'User'}).first()
        
        if not role:
            raise ValueError("Role 'User' not found")

        roleId = getattr(role, role_columns['roleId'])
        role_name = getattr(role, role_columns['role'])
        print("Role ID:", roleId)
        
        # Check if the mobile number already exists
        user = session.query(User).filter_by(**{user_columns['mobileNumber']: mobileNumber}).first()
        if user:
            userId = getattr(user, user_columns['userId'])
            return userId, role_name, mobileNumber
        else:
            # Create and add the new user
            new_user = User(**{user_columns['roleId']: roleId, user_columns['mobileNumber']: mobileNumber})
            session.add(new_user)
            session.commit()
            userId = getattr(new_user, user_columns['userId'])
            
            # Return success message
            return userId, role_name, mobileNumber
    except Exception as e:
        print(f"Error: {e}")
        session.rollback()
        return message.tryExceptError(str(e))
    finally:
        session.close()
