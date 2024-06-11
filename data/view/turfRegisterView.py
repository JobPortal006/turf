from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from data.model.turfRegisterModel import turfRegister

@csrf_exempt
def turfRegister(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            profilePhoto = data.get('profilePhoto')
            firstName = data.get('firstName')
            lastName = data.get('lastName')
            email = data.get('email')
            courtName = data.get('courtName')
            location = data.get('location')
            description = data.get('description')
            mobileNumber = data.get('mobileNumber')
            registrationDocument = data.get('registrationDocument')
            roleName = "Turf Admin"
            response = turfRegister(mobileNumber,roleName)
            
            response_data = {"Response": response}
            
            return JsonResponse(response_data, safe=False)
    except Exception as e:
        return JsonResponse({"error": f"Register Exception: {str(e)}"}, safe=False)