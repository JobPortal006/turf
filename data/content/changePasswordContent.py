from django.http import JsonResponse

def getChangePasswordFields(request):
  # Constructing JSON response for change password fields
  responseData = {
    "heading": {
      "text": "Change Password", # Text for heading
      "style": {
        "color": "#000000",
        "fontSize": "24px",
        "fontWeight": "bold"
      }
    },
    "description": {
      "text": "Reset your password", # Description about resetting password
      "style": {
        "color": "#7B7E81",
        "fontSize": "16px"
      }
    },
    "fields": [
      {
        "name": "new_password",
        "label": "Enter new password*", # Label for new password field
        "hidden": False,
        "required": True,
        "dataType": "String",
        "fieldType": "password", # Field type is password
        "validations": ["isRequired", {"minLength": 8}], # Validations for new password
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
        "label": "Confirm new password*", # Label for confirm password field
        "hidden": False,
        "required": True,
        "dataType": "String",
        "fieldType": "password", # Field type is password
        "validations": ["isRequired", {"minLength": 8}, {"match": "new_password"}], # Validations for confirm password
        "error": False,
        "style": {
          "color": "#000000",
          "backgroundColor": "#F5F5F5"
        }
      }
    ],
    "buttons": [
      {
        "name": "reset_password",
        "text": "Reset Password", # Text for reset password button
        "fieldType": "submit", # Button type is submit
        "style": {
          "backgroundColor": "#0A1E3C",
          "color": "#FFFFFF"
        }
      }
    ]
  }
  return JsonResponse(responseData) # Return JSON response with change password fields
