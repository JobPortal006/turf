from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from data.model.userRegisterModel import userRegisterInsertQuery ,userRegisterSelectQuery,userRegisterUpdateQuery,userRegisterDeleteQuery
from data import message 


# Insert ----------------------> 
@csrf_exempt
def userDynamicInsert(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            userName = data.get('userName')
            mobileNumber = data.get('profilePhoto')
            mobileNumber = data.get('mobileNumber')
            
            check = message.check(userName,mobileNumber)
            if check == True:
                response = userRegisterInsertQuery(mobileNumber,userName)
                
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