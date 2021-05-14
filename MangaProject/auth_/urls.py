from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path, include
from auth_.views import *
router = DefaultRouter()
router.register(r'profile', viewset=ProfileViewSet, basename='auth')

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('', include(router.urls))
]