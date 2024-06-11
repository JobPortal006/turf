from django.urls import path
from data.view import userRegisterView
from data.content import loginContent, forgetPasswordContent, otpVerificationContent, changePasswordContent

urlpatterns = [
    # Endpoint for user registration
    path('userRegisters/', userRegisterView.userRegisters, name='userRegisters'),

    # Endpoint for login content
    path('loginContent/', loginContent.getLoginFields, name='loginContent'), 

    # Endpoint for forget password content
    path('forgetPasswordContent/', forgetPasswordContent.getForgotPasswordFields, name='forgetPasswordContent'), 

    # Endpoint for OTP verification content
    path('otpVerificationContent/', otpVerificationContent.getOTPVerificationFields, name='otpVerificationContent'), 

    # Endpoint for change password content
    path('changePasswordContent/', changePasswordContent.getChangePasswordFields, name='changePasswordContent'),

    path('userRegisterSelect/',userRegisterView.userRegisterSelect),
    path('userRegisterUpdate/',userRegisterView.userRegisterUpdate),
    path('userRegisterDelete/',userRegisterView.userRegisterDelete),
]
