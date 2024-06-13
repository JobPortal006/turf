from django.urls import path
from data.view import userRegisterView
from ..view.userRegisterView import userRegistersInsert,userRegisterSelect

from ..view import userDynamic

from ..view.authenticationView.userLoginView import userLogin
urlpatterns = [
    # Endpoint for user registration
   path('userLogin/',userLogin),

    path('userRegisters/', userRegisterView.userRegistersInsert, name='userRegistersInsert'),

    path('userRegisterSelect/',userRegisterView.userRegisterSelect),
    # path('userRegisterUpdate/',userRegisterView.userRegisterUpdate),
    # path('userRegisterDelete/',userRegisterView.userRegisterDelete),
    
    
    
    # Registeration 
    path('userDynamic/',userDynamic.userDynamicInsert),
    
    
    
]
