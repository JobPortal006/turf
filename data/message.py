from django.http import JsonResponse
import os

#dynamic success response
def handleSuccess(success,data):
    return JsonResponse({"status":True,"statusCode":200,"message":success,"token":data})

#dynamic error response
def errorResponse(error):
    return  JsonResponse({"status":False,"statusCode":404,"message":error})

#server error response
def serverErrorResponse():
    return  JsonResponse({"status":False,"statusCode":500,"message":"Internal Server Error"})

def response(val, key,data):
    key_value_mapping = {
        'Success': {
            'login': 'Login Successfully',
            'userDelete': 'Delete Successfully',
            'forgetPassword': 'Email sent Successfully',
            'passwordUpdate':'Password Updated Successfully'
        },
        'Error': {
            'mobileError': 'Mobile Number already exists. Please use a different mobile number.',
            'loginError':'Login failed',
            'turfAdminLoginError':'Invalid email or password',
            'forgetPasswordError': 'Email is not registered',
            'passwordUpdateError':'Password is not Updated',
            'noResult': 'No Result Found',
            'putMethod': 'Use the PUT method',
            'getMethod': 'Use the GET method',
            'deleteMethod': 'Use the DELETE method',
            'emptyValue':'Value is None',
        }
    }
    if val == 'Success' and data is not None:
        return handleSuccess(key_value_mapping[val][key],data)
    else:
        return errorResponse(key_value_mapping[val][key])

def tryExceptError(message):
    # List of error messages that trigger server reload
    reload_messages = [
        "(2006, 'Server has gone away')",
        "(2013, 'Lost connection to server during query')",
        "Invalid salt",
        "(2013, 'Lost connection to MySQL server during query')",
        "(2006, '')",
        "(2014, 'Commands out of sync; you can't run this command now')"
    ]
    # Check if the message triggers server reload
    if message in reload_messages:
        serverReload()
    # Always return a JSON response
    return JsonResponse({"status": False, "statusCode": 500, "message": message})

def serverReload():
    manage_py_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'manage.py')
    os.utime(manage_py_path, None)
