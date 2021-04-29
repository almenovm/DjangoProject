from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path
from auth_.views import *

urlpatterns = [
    path('login/', obtain_jwt_token),
    # path('register/', obtain_jwt_token),
]