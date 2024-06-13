from django.http import JsonResponse

def getProfileDetails(request):
  responseData = {
    "heading": {
      "text": "Profile Details",
      "style": {
        "color": "#000000"
      }
    },
    "fields": [
      {
        "name": "first_name",
        "label": "First Name",
        "hidden": False,
        "required": True,
        "dataType": "String",
        "fieldType": "text",
        "validations": ["isRequired"],
        "error": False,
        "style": {
          "color": "#000000"
        }
      },
      {
        "name": "last_name",
        "label": "Last Name",
        "hidden": False,
        "required": True,
        "dataType": "String",
        "fieldType": "text",
        "validations": ["isRequired"],
        "error": False,
        "style": {
          "color": "#000000"
        }
      },
      {
        "name": "mobile_number",
        "label": "Mobile Number",
        "hidden": False,
        "required": True,
        "dataType": "String",
        "fieldType": "text",
        "validations": ["isRequired", "isPhoneNumber"],
        "error": False,
        "style": {
          "color": "#000000"
        }
      },
      {
        "name": "email_id",
        "label": "Email id",
        "hidden": False,
        "required": True,
        "dataType": "String",
        "fieldType": "text",
        "validations": ["isRequired", "isEmail"],
        "error": False,
        "style": {
          "color": "#000000"
        }
      }
    ],
    "buttons": [
      {
        "name": "continue",
        "text": "CONTINUE",
        "fieldType": "submit",
        "style": {
          "backgroundColor": "#0A1E3C",
          "color": "#FFFFFF"
        }
      },
      {
        "name": "skip",
        "text": "SKIP",
        "fieldType": "button",
        "style": {
          "color": "#000000"
        }
      }
    ]
  }
  return JsonResponse(responseData)
