from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from .views import ReviewViewSet, ReplyViewSet, ReplynReviewViewSet

router = DefaultRouter()
router.register(r'review', viewset=ReviewViewSet, basename='rev')
router.register(r'reply', viewset=ReplyViewSet, basename='rev')
router.register(r'reply_review', viewset=ReplynReviewViewSet, basename='rev')

urlpatterns = [

path('', include(router.urls))
]

