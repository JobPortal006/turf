from django.http import JsonResponse
from data import message
from data.table import tableContent
from ..table.table import User
from ..sqlalchemyConfig import DATABASE_URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create the SQLAlchemy engine and session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def userRegisterInsertDynamic(firstName, lastName, mobileNumber, email, profilePhoto, userSportsInterest):
    try:
        session = Session()  # Start a new session
        userId = 1  # Assuming you have the userId
        
        # Get user table information
        userTable = tableContent.get_table_info('user')  # Correct function call
        userColumns = userTable['columns']
        
        # print("User Table Information:", userTable)

        # Check if user with userId exists
        existing_user = session.query(User).filter_by(userId=userId).first()

        if existing_user:
            # User exists, update the existing user
            setattr(existing_user, userColumns['firstName'], firstName)
            setattr(existing_user, userColumns['lastName'], lastName)  # Added lastName
            setattr(existing_user, userColumns['email'], email)
            setattr(existing_user, userColumns['profilePhoto'], profilePhoto)
            session.commit()  # Commit the transaction
            return {"status": "success", "message": "User inserted successfully"}
        else:
            # User does not exist, so we create a new one
            
              # Commit the transaction
            return {"status": "success", "message": "User Exited"}

    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, safe=False)

    finally:
        session.close()  # Close the session
