from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from data.model.userQueryDynamic import userRegisterInsertDynamic
from data import message 
from turf.data import tablesFields


# Insert ----------------------> 
@csrf_exempt
def userDynamicInsert(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            roleType = "user"
            userName = data.get('userName')
            profilePhoto = data.get('profilePhoto')
            mobileNumber = data.get('mobileNumber')
            
            check = message.check(roleType,userName,mobileNumber,profilePhoto)
            if check == True:
                
                roleTable = tablesFields.userRegisterRoleTable
                userTable = tablesFields.userRegisterUserTable
                response = userRegisterInsertDynamic(roleTable,userTable,roleType,userName,mobileNumber,profilePhoto)
                
                if response == False:
                    return message.response('Error','mobileError')
                    
                userRegisterResponse = {"response":"Login Successfully","token":response}
                
                return message.handleSuccess(userRegisterResponse)
            else:
                return message.response('Error','emptyValue')
        else:
            return message.response('Error','postMethod')
    except Exception as e:
        return message.tryExceptError(str(e))