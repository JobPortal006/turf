import jwt
import datetime

secret_key = 'turf123'

# Encode ----- Token
def jwtTokenEncode(userId, role):
    try:
        exp_time = datetime.datetime.utcnow() + datetime.timedelta(days=1)
        # Convert the datetime object to a UNIX timestamp
        exp_timestamp = int(exp_time.timestamp())
        # Construct the payload
        payload = {
            'userId': userId,
            'role': role,
            'exp': exp_timestamp
        }
        token = jwt.encode(payload, secret_key, algorithm='HS256')
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
