import boto3
from django.conf import settings

def get_cognito_client():
    return boto3.client('cognito-idp', region_name=settings.AWS_COGNITO_REGION)

def authenticate_user(username, password):
    client = get_cognito_client()
    try:
        response = client.initiate_auth(
            ClientId=settings.AWS_COGNITO_APP_CLIENT_ID,
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': username,
                'PASSWORD': password
            }
        )
        return response['AuthenticationResult']
    except client.exceptions.NotAuthorizedException:
        return None

def get_user_attributes(access_token):
    client = get_cognito_client()
    try:
        response = client.get_user(AccessToken=access_token)
        return response['UserAttributes']
    except client.exceptions.NotAuthorizedException:
        return None
