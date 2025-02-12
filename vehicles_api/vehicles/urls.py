from django.urls import path
from .views import VehicleDetailAPIView, VehicleListAPIView
urlpatterns = [
    path('Vehicles/', VehicleListAPIView.as_view(), name='Vehicle-list-create'),
    path('Vehicles/<int:pk>/', VehicleDetailAPIView.as_view(), name='Vehicle-detail'),
]