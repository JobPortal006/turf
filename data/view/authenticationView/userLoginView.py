from django.views.decorators.csrf import csrf_exempt
import json
from ...model.authenticationModel.userLoginModel import userLoginQuery
from data import message,jwtToken
from data.table import tableContent

@csrf_exempt
def userLogin(request):
  if request.method == 'POST':
    data = json.loads(request.body)
    mobileNumber = data.get('mobileNumber')
    try:
      # Get table info for 'role' and 'user'
      role_table = tableContent.get_table_info('roles')
      user_table = tableContent.get_table_info('user')
      userId, role = userLoginQuery(mobileNumber,role_table,user_table)
      print("User Login details ------>",userId, role)
      # Generate JWT token
      jwtTokenEn = jwtToken.jwtTokenEncode(userId, role)
      if userId is not None:
        return message.response('Success','login',jwtTokenEn)  
      else:
        return message.response('Error','loginError',jwtTokenEn)
    except Exception as e:
      print(f"User Login Exception : {str(e)}")
      return message.tryExceptError(str(e))
  return message.responseMessage('Error','postMethod')
