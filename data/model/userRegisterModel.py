from data.table.table import Session, User, Role

def userRegister(mobileNumber, roleName):
    try:
        session = Session()

        # Check if the role exists
        role = session.query(Role).filter_by(role=roleName).first()

        if role is None:
            # If role doesn't exist, create a new role
            new_role = Role(role=roleName)
            session.add(new_role)
            session.commit()
            roleId = new_role.roleId
        else:
            roleId = role.roleId

        # Insert the new user with the retrieved or newly created roleId
        new_user = User(roleId=roleId, mobileNumber=mobileNumber)
        session.add(new_user)
        session.commit()
        
        return True
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
        return False
