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

def turfAdminLoginQuery(email, password):
    session = Session()
    try:
        # Get table info for 'role' and 'user'
        role_table = get_table_info('roles')
        user_table = get_table_info('user')

        role_columns = role_table['columns']
        user_columns = user_table['columns']
        
        # Check if the role 'Turf Admin' exists
        role = session.query(Roles).filter_by(**{role_columns['role']: 'Turf Admin'}).first()

        roleId = getattr(role, role_columns['roleId'])
        role_name = getattr(role, role_columns['role'])
        print("Role ID:", roleId)
        
        # Check if the email and password match an existing user with the 'Turf Admin' role
        user = session.query(User).filter_by(
            **{user_columns['email']: email, user_columns['password']: password, user_columns['roleId']: roleId}
        ).first()
        
        if user:
            userId = getattr(user, user_columns['userId'])
            return userId, role_name, email
        else:
            return None, None, None
            
    except Exception as e:
        print(f"Error: {e}")
        session.rollback()
        return message.tryExceptError(str(e))
    finally:
        session.close()
