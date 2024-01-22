from django.shortcuts import render

from rest_framework import generics, viewsets
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

from .serializers import *
from elon.models import *


class UserApiList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = User.objects.all()
    serializer_class = UserSerializers

class UserViewset(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializers