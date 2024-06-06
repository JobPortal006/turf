from django.http import JsonResponse

from django.db import connection
cursor = connection.cursor()

def userRegisterQuery(mobilenumber):
    try:
        id = 1
        # sql = "INSERT INTO user(roleid, username, password, email, mobilenumber) VALUES (%s, %s, %s, %s, %s)"
        sql = "INSERT INTO user(roleid, mobilenumber) VALUES (%s, %s)"
        
        values = (id,  mobilenumber)
        print("---------------------------")
        cursor.execute(sql, values)  # Assuming cursor is your MySQL cursor object
        print("[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]")
        return "Successfully inserted"
    except Exception as e:
        print(f"Error: {e}")
        return "Error occurred during insertion"
