from sqlalchemy.orm import sessionmaker
from data.table.table import engine, User, Roles
from data import message
import bcrypt

Session = sessionmaker(bind=engine)

def forgetPasswordQuery(email,user_table,role_table):
    session = Session()
    try:
        user_columns = user_table['columns']
        role_columns = role_table['columns']

        # Check if the email already exists
        user = session.query(User).filter_by(**{user_columns['email']: email}).first()
        if user:
            # Email exists, return True
            roleId = getattr(user, user_columns['roleId'])
            userId = getattr(user, user_columns['userId'])
            role = session.query(Roles).filter_by(**{role_columns['roleId']: roleId}).first()
            if role:
                role_name = getattr(role, role_columns['role'])
            return userId,role_name
        else:
            # Email doesn't exist, return False
            return None,None
    except Exception as e:
        print(f"forgetPasswordQuery Error: {e}")
        session.rollback()
        return message.tryExceptError(str(e))
    finally:
        session.close()

def changePassword(password, userId,user_table):
  session = Session()
  try:
      user_columns = user_table['columns']
      # Query the user by email
      user = session.query(User).filter_by(**{user_columns['userId']: userId}).first()
      if user:
          # Update the password
          hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
          user.password = hashed_password.decode('utf-8')
          session.commit()
          return True
      else:
          # User not found
          return False
  except Exception as e:
      print(f"forgetPasswordQuery Error: {e}")
      session.rollback()
      return message.tryExceptError(str(e))
  finally:
      session.close()