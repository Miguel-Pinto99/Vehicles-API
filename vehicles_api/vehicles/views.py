from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import VehicleSerializer
from .models import Vehicle
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView

class VehicleListAPIView(APIView):
    def get(self, request):
        Vehicles = Vehicle.objects.all()
        serializer = VehicleSerializer(Vehicles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(request=VehicleSerializer,
                         responses={201: VehicleSerializer(),
                                    400: 'Bad Request'})
    def post(self, request):
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VehicleDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Vehicle.objects.get(pk=pk)
        except Vehicle.DoesNotExist:
            return None

    def get(self, request, pk):
        Vehicle = self.get_object(pk)
        if Vehicle is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = VehicleSerializer(Vehicle)
        return Response(serializer.data)

    @extend_schema(request=VehicleSerializer,
                         responses={201: VehicleSerializer(),
                                    400: 'Bad Request'})
    def put(self, request, pk):
        Vehicle = self.get_object(pk)
        if Vehicle is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = VehicleSerializer(Vehicle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        Vehicle = self.get_object(pk)
        if Vehicle is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        Vehicle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
