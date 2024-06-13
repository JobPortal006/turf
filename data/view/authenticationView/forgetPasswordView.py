from django.views.decorators.csrf import csrf_exempt
import json
from ...model.authenticationModel import forgetPasswordModel
from data import message,jwtToken
from ...table import tableContent

globalemail = ""
# Get table info for 'user'
user_table = tableContent.get_table_info('user')
role_table = tableContent.get_table_info('roles')

@csrf_exempt
def forgetPassword(request):
  if request.method == 'POST':
    data = json.loads(request.body)
    email = data.get('email')
    try:
      userId, role = forgetPasswordModel.forgetPasswordQuery(email,user_table,role_table)
      print("Turf Admin Login details ------>",userId, role)
      # Generate JWT token
      jwtTokenEn = jwtToken.jwtTokenEncode(userId, role)
      if userId is not None:
        return message.response('Success','forgetPassword',jwtTokenEn)  
      else:
        return message.response('Error','forgetPasswordError',jwtTokenEn)
    except Exception as e:
      print(f"User Login Exception : {str(e)}")
      return message.tryExceptError(str(e))
  return message.responseMessage('Error','postMethod')

@csrf_exempt
def changePassword(request):
  try:
    if request.method == 'POST':  
      data = json.loads(request.body)
      password = data.get('password')
      token = data.get('token')
      # Decode the token
      tokenResult = jwtToken.decodeToken(token)
      userId = tokenResult['userId']
      print('changePassword userId',userId)  # Debug print to check userId
      # Update the password
      password_update = forgetPasswordModel.changePassword(password, userId, user_table)
      if password_update: 
        return message.response('Success', 'passwordUpdate',token)
      else:
        return message.response('Error', 'passwordUpdateError',token)
    else:
        return message.response('Error', 'postMethod',token)
  except Exception as e:
    return message.tryExceptError(str(e))