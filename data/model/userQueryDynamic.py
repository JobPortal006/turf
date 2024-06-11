from django.http import JsonResponse
from data import message , jwtToken

from django.db import connection
from data import message 

con = connection.cursor()

def userRegisterInsertDynamic(roleTable,userTable,roleType,userName,mobileNumber,profilePhoto):
    try:
        con = connection.cursor()
        
        # get roleId in role table 
        roleId = roleTable["role"]["fields"]["roleId"]
        roleTableName = roleTable["role"]["tableName"]
        role = roleTable["role"]["fields"]["role"]
        
        
        
        con.execute(f"select {roleId} from  {roleTableName} where {role} = %s",[roleType])
        
        # query = f"SELECT {roleId} FROM {roleTableName} WHERE {role} = %s"
        # parameters = [roleType]
        # con.execute(query, parameters)
        
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
