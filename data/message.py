from django.http import JsonResponse
import os


#dynamic success response
def handleSuccess(success):
    return JsonResponse({"status": True, "statusCode": 200, "message": success},safe=False)

def handleSuccess1(success,data):
    return JsonResponse({"status":True,"statusCode":200,"message":success,"data":data})

#dynamic error response
def errorResponse(error):
    return  JsonResponse({"status":False,"statusCode":404,"message":error})

#dynamic error response
def tokenResponse(error):
    return  JsonResponse({"status":False,"statusCode":400,"message":error})

#server error response
def serverErrorResponse():
    return  JsonResponse({"status":False,"statusCode":500,"message":"Internal Server Error"})

def response(val, key):
    print("--------------------")
    key_value_mapping = {
        'Success': {
            'Signup': 'Signup Successfully',
            'Login': 'Login Successfully',
            'userDelete': 'Delete Successfully',
            
        },
        'Error': {
            'mobileError': 'Mobile Number already exists. Please use a different mobile number.',
            'noResult': 'No Result Found',
            'postMethod': 'Use the POST method',
            'putMethod': 'Use the PUT method',
            'getMethod': 'Use the GET method',
            'deleteMethod': 'Use the DELETE method',
            'emptyValue':'Value is None',
            
            
            
            
        }
    }
    
    if val == 'Success':
        return handleSuccess(key_value_mapping[val][key])
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



def check(*args):
    for i in args:
        if i == '' or i is None:
            return False
    return True