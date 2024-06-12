from django.contrib import admin
from django.urls import path, include
from data.url import userModuleUrls,authenticationContentUrls,turfAdminauthenticationUrls

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login/',login_data),
    path('', include(userModuleUrls)),
    path('authenticationContent/', include(authenticationContentUrls)),
    path('', include(turfAdminauthenticationUrls)),
]