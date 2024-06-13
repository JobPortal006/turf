from django.views.decorators.csrf import csrf_exempt
import json
from data.model.authenticationModel.addNewUserModel import addNewUserQuery
from data import message,jwtToken
from data.table import tableContent

@csrf_exempt
def addNewUser(request):
  if request.method == 'POST':
    data = json.loads(request.body)
    role=data.get('role')
    email = data.get('email')
    password = data.get('password')
    try:
      # Get table info for 'role' and 'user'
      role_table = tableContent.get_table_info('roles')
      user_table = tableContent.get_table_info('user')
      userId, role = addNewUserQuery(role,email,password,role_table,user_table)
      print("Add New User details ------>",userId, role)
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
