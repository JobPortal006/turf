from django.http import JsonResponse

def getLoginFields(request):
  responseData = {
    "heading": {
      "text": "Turf Management System",
      "style": {
          "color": "#0A1E3C" 
        }
    },
    "image": {
      "src": "/image.jpg",  
      "alt": "Turf Management System"
    },
    "fields": [
      {
        "name": "email",
        "label": "Email",
        "hidden": False,
        "required": True,
        "dataType": "String",
        "fieldType": "text",
        "validations": ["isRequired", "isEmail"],
        "error": False,
        "style": {
          "color": "#7B7E81"
        }
      },
      {
        "name": "password",
        "label": "Password",
        "hidden": False,
        "required": True,
        "dataType": "String",
        "fieldType": "text",
        "validations": ["isRequired"],
        "error": False,
        "style": {
          "color": "#7B7E81"
        }
      }
    ],
    "buttons": [
      {
        "name": "forgetPassword",
        "text": "Forget Password",
        "fieldType": "button",
        "style": {
          "color": "#0A1E3C"
        }
      },
      {
        "name": "login",
        "text": "Login",
        "fieldType": "submit",
        "style": {
          "backgroundColor": "#0A1E3C",  
          "color": "#FFFFFF" 
        }
      }
    ]
  }
  return JsonResponse(responseData)
