from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from data.model.userRegisterModel import userRegister

@csrf_exempt
def userRegisters(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            mobileNumber = data.get('mobileNumber')
            roleName = "User"
            response = userRegister(mobileNumber,roleName)
            
            response_data = {"Response": response}
            
            return JsonResponse(response_data, safe=False)
    except Exception as e:
        return JsonResponse({"error": f"Register Exception: {str(e)}"}, safe=False)