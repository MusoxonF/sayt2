from django.shortcuts import render

from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Car, Image
from .serializers import *


class CarApiList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarApi(APIView):
    parser_classes = [MultiPartParser]
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        a = Car.objects.all()
        dict_data = CarSerializer(a, many=True)

        return Response(dict_data.data)

    def post(self, request):
        rasm_list = request.data.get('rasm', [])
        serializers = CarSerializer(data = request.data)
        if serializers.is_valid():
            car = serializers.save()
            for x in rasm_list:
                r = Image.objects.create(image = x)
                car.photo.add(r)
            return Response(serializers.data)
        return Response(serializers.errors)



class CarApiDetail(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request, id):
        try:   
            a = Car.objects.get(id = id)
            ser = CarGetSer(a)
            return Response(ser.data)
        except:
            return Response({'xato': "bu id xato"})

    # def put(self, request, id):
    #     a = Car.objects.get(id = id)
    #     serializer = CarGetSer(data = request.data, instance = a)
    #     if serializer.is_valid(raise_exception = True):
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors)

    def patch(self, request, id):
        a = Car.objects.get(id = id)
        serializer = CarGetSer(data = request.data, instance = a, partial = True)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id):
        a = Car.objects.get(id=id)
        a.delete()
        message = {'delete':'successfull'}
        return Response(message)


    