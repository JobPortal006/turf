from django.http import JsonResponse
from data import message , jwtToken

from django.db import connection
from data import message 

con = connection.cursor()

def userRegisterInsertQuery(mobileNumber,userName):
    try:
        con = connection.cursor()
        con.execute("select roleId from role where role = %s", ["user"])
        result = con.fetchone()
        roleId = result[0]
        print("Role ID:", roleId)
       
        con.execute("select * from user where mobileNumber = %s", [mobileNumber])
        userResult = con.fetchone()
        if userResult:
            return False
            
        else:
            sql = "INSERT INTO user(roleId, userName,  mobileNumber) VALUES (%s , %s, %s)"
            values = (roleId,userName,mobileNumber)
            con.execute(sql, values) 
            userId = con.lastrowid

            jwtTokenEn = jwtToken.jwtTokenEncode(userId,roleId,mobileNumber)
             
            con.close()
        return jwtTokenEn
    except Exception as e:
        print(f"Error: {e}")
        con.close()
        return message.handleSuccess( "Error occurred during insertion")

# Select Query ----------------------
def userRegisterSelectQuery(token):
    try:
        con = connection.cursor()
        
        jwtTokenDecode = jwtToken.decodeToken(token)
       
        
        userId = jwtTokenDecode['userId']
        con.execute("select userId,roleId,mobileNumber from user where userId = %s", [userId])
        result = con.fetchone()
        if result:
            response = {
                "userId": result[0],
                "roleId": result[1],
                "mobileNumber": result[2]
            }
        else:
            return False
        con.close()
        return response
        
    except Exception as e:
        con.close()
        return message.tryExceptError(str(e))
    
        
def userRegisterUpdateQuery(userName,mobileNumber,token):
    try:
        con = connection.cursor()
        print("1------------")
        jwtTokenDecode = jwtToken.decodeToken(token)
        print("2------------")
        
        userId = jwtTokenDecode['userId']
        
        sql = "UPDATE user SET userName = %s, mobileNumber = %s WHERE userId = %s"
        values = (userName, mobileNumber, userId)
        updateResult = con.execute(sql, values)
        
        if updateResult:
            con.execute("select userId,roleId,mobileNumber from user where userId = %s", [userId])
            selectResult = con.fetchone()
            
            userId, roleId, mobileNumber = selectResult
            jwtTokenEncode = jwtToken.jwtTokenEncode(userId,roleId,mobileNumber)
            return jwtTokenEncode
            
            
        else:
            return False
            
        
        
    except Exception as e:
        con.close()
        return message.tryExceptError(str(e))
        
             
# Delete Query ----------------------
def userRegisterDeleteQuery(token):
    try:
        con = connection.cursor()
        jwtTokenDecode = jwtToken.decodeToken(token)
        print("--------------------,.,.<>")
        userId = jwtTokenDecode['userId']
        result = con.execute("DELETE FROM user WHERE userId = %s", [userId])
        if result:
            con.close()
            return True
        else:
            con.close()
            return False
    except Exception as e:
        con.close()
        return message.tryExceptError(str(e))  