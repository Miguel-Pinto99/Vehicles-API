from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import VehicleSerializer
from .models import Vehicle
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from ..specifications.persistance import SpecsLogic

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
            vehicle = serializer.save()
            SpecsLogic(vehicle)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
