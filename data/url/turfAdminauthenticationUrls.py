from django.urls import path
from ..view.turfAdminLoginView import turfAdminLogin

urlpatterns = [
   path('turfAdminLogin/',turfAdminLogin),
]
