from django.urls import path
from data.view import userRegisterView
from ..view.userRegisterView import userRegistersInsert,userRegisterSelect

urlpatterns = [
    # Endpoint for user registration
    path('userRegisters/', userRegisterView.userRegistersInsert, name='userRegistersInsert'),

    path('userRegisterSelect/',userRegisterView.userRegisterSelect),
    # path('userRegisterUpdate/',userRegisterView.userRegisterUpdate),
    # path('userRegisterDelete/',userRegisterView.userRegisterDelete),
]
