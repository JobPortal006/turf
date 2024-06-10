from django.http import JsonResponse

def getForgotPasswordFields(request):
  responseData = {
    "heading": {
      "text": "Forgot Password",
      "style": {
        "color": "#000000",
        "fontSize": "24px",
        "fontWeight": "bold"
      }
    },
    "description": {
      "text": "Enter your registered email id",
      "style": {
        "color": "#7B7E81",
        "fontSize": "16px"
      }
    },
    "fields": [
      {
        "name": "email",
        "label": "Email id*",
        "hidden": False,
        "required": True,
        "dataType": "String",
        "fieldType": "text",
        "validations": ["isRequired", "isEmail"],
        "error": False,
        "style": {
          "color": "#000000",
          "backgroundColor": "#F5F5F5",
          "border": "1px solid #E0E0E0",
          "padding": "10px",
          "borderRadius": "5px"
        }
      }
    ],
    "buttons": [
      {
        "name": "continue",
        "text": "Continue",
        "fieldType": "submit",
        "style": {
          "backgroundColor": "#0A1E3C",
          "color": "#FFFFFF",
          "padding": "10px 20px",
          "borderRadius": "5px",
          "border": "none",
          "cursor": "pointer"
        }
      }
    ]
  }
  return JsonResponse(responseData)
