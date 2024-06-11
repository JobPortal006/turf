from django.urls import path
from data.content import loginContent, forgetPasswordContent, otpVerificationContent, changePasswordContent

urlpatterns = [
    # Endpoint for login content
    path('loginContent/', loginContent.getLoginFields, name='loginContent'), 

    # Endpoint for forget password content
    path('forgetPasswordContent/', forgetPasswordContent.getForgotPasswordFields, name='forgetPasswordContent'), 

    # Endpoint for OTP verification content
    path('otpVerificationContent/', otpVerificationContent.getOTPVerificationFields, name='otpVerificationContent'), 

    # Endpoint for change password content
    path('changePasswordContent/', changePasswordContent.getChangePasswordFields, name='changePasswordContent')
]
