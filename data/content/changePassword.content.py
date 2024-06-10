from django.http import JsonResponse

def getChangePasswordFields(request):
  responseData = {
    "heading": {
      "text": "Change Password",
      "style": {
        "color": "#000000",
        "fontSize": "24px",
        "fontWeight": "bold"
      }
    },
    "description": {
      "text": "Reset your password",
      "style": {
        "color": "#7B7E81",
        "fontSize": "16px"
      }
    },
    "fields": [
      {
        "name": "new_password",
        "label": "Enter new password*",
        "hidden": False,
        "required": True,
        "dataType": "String",
        "fieldType": "password",
        "validations": ["isRequired", {"minLength": 8}],
        "error": False,
        "style": {
          "color": "#000000",
          "backgroundColor": "#F5F5F5",
          "border": "1px solid #E0E0E0",
          "padding": "10px",
          "borderRadius": "5px"
        }
      },
      {
        "name": "confirm_password",
        "label": "Confirm new password*",
        "hidden": False,
        "required": True,
        "dataType": "String",
        "fieldType": "password",
        "validations": ["isRequired", {"minLength": 8}, {"match": "new_password"}],
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
        "name": "reset_password",
        "text": "Reset Password",
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
