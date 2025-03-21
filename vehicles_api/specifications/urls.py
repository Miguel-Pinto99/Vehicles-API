from django.urls import path
from .views import SpecificationsListAPIView
from .views import SpecificationsDetailAPIView
urlpatterns = [
    path('Specifications/', SpecificationsListAPIView.as_view(), name='Specifications-list-create'),
    path('Specifications/<str:pk>/', SpecificationsDetailAPIView.as_view(), name='Specifications-detail'),
]
