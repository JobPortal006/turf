userRegisterRoleTable = ["role","roleId","role"]
userRegisterUserTable = ["user","roleId","userName","profilePhoto","mobileNumber"]

userRegisterRoleTable = {
    "role": {
        "tableName": "role",  # Text for heading
        "fields": {
            "roleId": "roleId",
            "role": "role",
        }
    } 
}

userRegisterUserTable = { "user": {
        "tableName": "user",  
        "fields": {
            "roleId": "roleId",
            "userName": "userName",
            "profilePhoto": "profilePhoto",
            "password":"password",
            "email":"email",
            "mobil eNumber": "mobileNumber",
            
            
        }
    }
}