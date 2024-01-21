from django.urls import path
from .views import *


urlpatterns = [
    path('Detail/<int:id>/', CarApiDetail.as_view()),
    path('api/', CarApiList.as_view(), name = 'CarApi'),

]