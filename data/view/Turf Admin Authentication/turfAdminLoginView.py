from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from ..model.turfAdminLoginModel import turfAdminLoginQuery
from data import message,jwtToken

@csrf_exempt
def turfAdminLogin(request):
  if request.method == 'POST':
    data = json.loads(request.body)
    email = data.get('email')
    password = data.get('password')
    try:
      userId, role, mobileNumber = turfAdminLoginQuery(email,password)
      print("Turf Admin Login details ------>",userId, role, mobileNumber)
      # Generate JWT token
      jwtTokenEn = jwtToken.jwtTokenEncode(userId, role, mobileNumber)
      if userId is not None:
        return message.response('Success','login',jwtTokenEn)  
      else:
        return message.response('Error','turfAdminLoginError',jwtTokenEn)
    except Exception as e:
      print(f"Turf Admin Login View Exception : {str(e)}")
      return message.tryExceptError(str(e))
  return message.response('Error','postMethod',jwtTokenEn)
