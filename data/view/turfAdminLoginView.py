from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# from ..model.turfAminLoginModel import turfAdminLoginModel
from data import message,jwtToken

@csrf_exempt
def turfAdminLogin(request):
  if request.method == 'POST':
    data = json.loads(request.body)
    email = data.get('email')
    password = data.get('password')
    print(email,password)
    try:
      # userId, role, mobileNumber = turfAdminLoginModel(mobileNumber)
      # Generate JWT token
      # jwtTokenEn = jwtToken.jwtTokenEncode(userId, role, mobileNumber)
      print("User Login jwtTokenEn ------>")
      # if userId is not None:
      #   return message.response('Success','login',jwtTokenEn)  
      # else:
      #   return message.response('Error','loginError',jwtTokenEn)
    except Exception as e:
      print(str(e))
  return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)
