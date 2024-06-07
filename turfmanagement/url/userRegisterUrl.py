from django.contrib import admin
from django.urls import path
from data.view import userRegisterView

urlpatterns = [
    path('userRegistersInsert/', userRegisterView.userRegistersInsert, name='userRegisters'),
    path('userRegisterSelect/',userRegisterView.userRegisterSelect),
    path('userRegisterUpdate/',userRegisterView.userRegisterUpdate),
    path('userRegisterDelete/',userRegisterView.userRegisterDelete),
    
    
    
    # path('register/', userRegisterView.userRegisters, name='register_api'),
    
]