from django.urls import path
from ..view.authenticationView import turfAdminLoginView,forgetPasswordView,addNewUserView

urlpatterns = [
   path('addNewUser/',addNewUserView.addNewUser,name='addNewUser'),

   path('turfAdminLogin/',turfAdminLoginView.turfAdminLogin,name='turfAdminLogin'),

   path('forgetPassword/',forgetPasswordView.forgetPassword,name='forgetPassword'),

   path('changePassword/',forgetPasswordView.changePassword,name='changePassword'),
]
