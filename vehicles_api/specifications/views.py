from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Specification
from .serializer import SpecificationSerializer

# Create your views here.
class SpecificationsListAPIView(APIView):
    def get(self, request):
        specifications = Specification.objects.all()
        serializer = SpecificationSerializer(specifications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SpecificationsDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            specification = Specification.objects.get(pk=pk)
        except Specification.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = SpecificationSerializer(specification)
        return Response(serializer.data, status=status.HTTP_200_OK)
