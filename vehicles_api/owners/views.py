
# Create your views here.
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import OwnerSerializer
from .models import Owner
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView

class OwnerListAPIView(APIView):
    def get(self, request):
        owners = Owner.objects.all()
        serializer = OwnerSerializer(owners, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(request=OwnerSerializer,
                         responses={201: OwnerSerializer(),
                                    400: 'Bad Request'})
    def post(self, request):
        serializer = OwnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OwnerDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Owner.objects.get(pk=pk)
        except Owner.DoesNotExist:
            return None

    def get(self, request, pk):
        owner = self.get_object(pk)
        if owner is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = OwnerSerializer(owner)
        return Response(serializer.data)

    @extend_schema(request=OwnerSerializer,
                         responses={201: OwnerSerializer(),
                                    400: 'Bad Request'})
    def put(self, request, pk):
        owner = self.get_object(pk)
        if owner is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = OwnerSerializer(owner, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        owner = self.get_object(pk)
        if owner is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        owner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
