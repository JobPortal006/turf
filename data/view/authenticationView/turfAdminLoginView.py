from django.views.decorators.csrf import csrf_exempt
import json
from data.model.authenticationModel.turfAdminLoginModel import turfAdminLoginQuery
from data import message,jwtToken
from data.table import tablecontent

@csrf_exempt
def turfAdminLogin(request):
  if request.method == 'POST':
    data = json.loads(request.body)
    email = data.get('email')
    password = data.get('password')
    try:
      # Get table info for 'role' and 'user'
      role_table = tablecontent.get_table_info('roles')
      user_table = tablecontent.get_table_info('user')
      userId, role = turfAdminLoginQuery(email,password,role_table,user_table)
      print("Turf Admin Login details ------>",userId, role)
      # Generate JWT token
      jwtTokenEn = jwtToken.jwtTokenEncode(userId, role)
      if userId is not None:
        return message.response('Success','login',jwtTokenEn)  
      else:
        return message.response('Error','turfAdminLoginError',jwtTokenEn)
    except Exception as e:
      print(f"Turf Admin Login View Exception : {str(e)}")
      return message.tryExceptError(str(e))
  return message.responseMessage('Error','postMethod')
