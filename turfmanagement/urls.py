from django.contrib import admin
from django.urls import path, include
from data.url import userModuleUrls,authenticationContentUrls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(userModuleUrls)),
    path('authenticationContent/', include(authenticationContentUrls)),
]
   