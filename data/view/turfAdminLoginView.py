from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from ..model.userLoginModel import userLoginModel
from data import message,jwtToken

@csrf_exempt
def turfAdminLogin(request):
  if request.method == 'POST':
    data = json.loads(request.body)
    mobileNumber = data.get('mobileNumber')
    print(mobileNumber)
    try:
      userId, role, mobileNumber = userLoginModel(mobileNumber)
      # Generate JWT token
      jwtTokenEn = jwtToken.jwtTokenEncode(userId, role, mobileNumber)
      print("User Login jwtTokenEn ------>",jwtTokenEn)
      if userId is not None:
        return message.response('Success','login',jwtTokenEn)  
      else:
        return message.response('Error','loginError',jwtTokenEn)
    except Exception as e:
      print(str(e))
  return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)
