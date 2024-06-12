from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from ..model.userLoginModel import userLoginModel
from data import message,jwtToken

@csrf_exempt
def userLogin(request):
  if request.method == 'POST':
    data = json.loads(request.body)
    mobileNumber = data.get('mobileNumber')
    try:
      userId, role, mobileNumber = userLoginModel(mobileNumber)
      print("User Login details ------>",userId, role, mobileNumber)
      # Generate JWT token
      jwtTokenEn = jwtToken.jwtTokenEncode(userId, role, mobileNumber)
      if userId is not None:
        return message.response('Success','login',jwtTokenEn)  
      else:
        return message.response('Error','loginError',jwtTokenEn)
    except Exception as e:
      print(f"User Login Exception : {str(e)}")
      return message.tryExceptError(str(e))
  return message.response('Error','postMethod',jwtTokenEn)
