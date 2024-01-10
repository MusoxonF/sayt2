from django.shortcuts import render

from rest_framework import generics

from .serializers import *
from elon.models import *


class UserApiList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers