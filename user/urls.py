from django.urls import path
from .views import *


urlpatterns = [
    path('api/', UserApiList.as_view(), name = 'UserApi'),
    path('detail/<int:pk>/', UserDetail.as_view(), name = 'Userdetail'),
]