from django.urls import path
from .views import advs_detail, advs_list
urlpatterns = [
    path('', advs_list),
    path('<int:pk>/', advs_detail),

]

