from django.http import JsonResponse

def getOTPVerificationFields(request):
  responseData = {
    "heading": {
      "text": "OTP Verification",
      "style": {
        "color": "#000000",
        "fontSize": "24px",
        "fontWeight": "bold"
      }
    },
    "description": {
      "text": "Enter the 6 digit otp code sent to your registered email id",
      "style": {
        "color": "#7B7E81",
        "fontSize": "16px"
      }
    },
    "fields": [
      {
        "name": "otp",
        "label": "Enter code*",
        "hidden": False,
        "required": True,
        "dataType": "String",
        "fieldType": "text",
        "validations": ["isRequired", "isNumeric", {"minLength": 6}, {"maxLength": 6}],
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
