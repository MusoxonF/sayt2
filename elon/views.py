from django.shortcuts import render

from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework import generics

from .models import Car, Image
from .serializers import *


class CarApiList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarApi(APIView):
    parser_classes = [MultiPartParser]

    def get(self, request):
        a = Car.objects.all()
        dict_data = CarGetSer(a, many=True)

        return Response(dict_data.data)

    def post(self, request):
        rasm_list = request.data.getlist('rasm', [])
        serializers = CarSerializer(data = request.data)
        if serializers.is_valid():
            car = serializers.save()
            for x in rasm_list:
                r = Image.objects.create(image = x)
                car.photo.add(r)
            return Response(serializers.data)
        return Response(serializers.errors)