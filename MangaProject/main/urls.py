from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from .views import PublisherListAPIView, PublisherDetailAPIView, SemilarMangaListAPIView, SemilarRanobeListAPIView, MangaViewSet, RanobeViewSet, SemilarMangaDetailAPIView, SemilarRanobeDetailAPIView

router = DefaultRouter()
router.register(r'manga', viewset=MangaViewSet, basename='manga')
router.register(r'ranobe', viewset=RanobeViewSet, basename='ranobe')

urlpatterns = [

path('publisher/', PublisherListAPIView.as_view()),
path('publisher/<int:pk>/', PublisherDetailAPIView.as_view()),

path('semilar/manga/', SemilarMangaListAPIView.as_view()),
path('semilar/manga/<int:pk>/', SemilarMangaDetailAPIView.as_view()),

path('semilar/ranobe/', SemilarRanobeListAPIView.as_view()),
path('semilar/ranobe/<int:pk>/', SemilarRanobeDetailAPIView.as_view()),

path('', include(router.urls))
]

