import jwt ,json
from django.http import JsonResponse

import datetime

global secret_key
secret_key = '1234'

# Encode ----- Token
def jwtTokenEncode(userId, roleId, mobileNumber):
    try:
        # Construct the payload
        payload = {
            'userId': userId,
            'roleId': roleId,
            'mobileNumber': mobileNumber,
            # 'iat': datetime.datetime.utcnow(),  # Issued at time
            # 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Expiration time (1 hour from now)
        }

        token = jwt.encode(payload, secret_key, algorithm='HS256')
        print("JWT:", token)

        # Return the token
        return token

    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return {"error": f"Unexpected error: {str(e)}"}



# Decode ----- Token
def decodeToken(token):
    try:
        decoded_payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        # json_payload = json.dumps(decoded_payload)
        print("Decoded Payload:", decoded_payload)
        return decoded_payload
    except jwt.ExpiredSignatureError:
        return {"error": "Token has expired"}  # Return a dictionary
    except jwt.InvalidTokenError:
        return {"error": "Invalid token"}  # Return a dictionary
