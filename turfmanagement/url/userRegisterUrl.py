from django.contrib import admin
from django.urls import path
from data.view import userRegisterView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('userRegisters/', userRegisterView.userRegisters, name='userRegisters'),
    
    # path('register/', userRegisterView.userRegisters, name='register_api'),
    
]