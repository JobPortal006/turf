from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from data.model.userRegisterModel import userRegisterInsertQuery ,userRegisterSelectQuery,userRegisterUpdateQuery,userRegisterDeleteQuery
from data import message 

# Insert ----------------------> 
@csrf_exempt
def userRegistersInsert(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            userName = data.get('userName')
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


# Select -----------------> 
@csrf_exempt
def userRegisterSelect(request):
    try:
        if request.method == 'GET':
            data = json.loads(request.body)
            
            token = data.get('token')
            check = message.check(token)
            if check == True:
                response = userRegisterSelectQuery(token)
                
                if response == False:
                    return message.response('Error','noResult')
                
                return message.handleSuccess(response)
            else:
                return message.response('Error','emptyValue')
        else:
            return message.response('Error','getMethod')

        
    except Exception as e:
        return message.tryExceptError(str(e))
    
#  Upadate ------------>        

@csrf_exempt
def userRegisterUpdate(request):
    try:
        if request.method == 'PUT':
            data = json.loads(request.body)
            userName = data.get('userName')
            mobileNumber = data.get('mobileNumber')
            token = data.get("token")
            
            check = message.check(userName,mobileNumber,token)
            if check == True:
            
                result = userRegisterUpdateQuery(userName,mobileNumber,token)
                
                if result == False:
                    return message.response('Error','updateError')
                updateResponse = {"response":"Update Successfully","token":result}
                
                return message.handleSuccess(updateResponse)
            else:
                return message.response('Error','emptyValue')
            
        else:
            return message.response('Error','putMethod')
        
    except Exception as e:
        return JsonResponse({"error": f"Register Exception: {str(e)}"}, safe=False)
    

# Delete ------------------>  

@csrf_exempt
def userRegisterDelete(request):
    try:
        if request.method == 'DELETE':
            data = json.loads(request.body)
            token = data.get('token')
            
            check = message.check(token)
            if check == True:
                response = userRegisterDeleteQuery(token)
                if response == True:
                    return message.response('Success','userDelete')
                else:
                    return message.response('Error','noResult')
            else:
                return message.response('Error','emptyValue')
                
        else:
             return message.response('Error','deleteMethod')
        
    except Exception as e:
        return JsonResponse({"error": f"Register Exception: {str(e)}"}, status=500)

