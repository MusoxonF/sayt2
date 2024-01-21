from django.urls import path, include
from .views import *

from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'Api', UserViewset)

urlpatterns = [
    path('api/', UserApiList.as_view(), name = 'UserApi'),
    path('v1/', include(router.urls)),
    path('detail/<int:pk>/', UserDetail.as_view(), name = 'Userdetail'),
]