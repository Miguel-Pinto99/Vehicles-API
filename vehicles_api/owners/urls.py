from django.urls import path
from .views import OwnerDetailAPIView, OwnerListAPIView
urlpatterns = [
    path('Owners/', OwnerListAPIView.as_view(), name='owner-list-create'),
    path('Owners/<int:pk>/', OwnerDetailAPIView.as_view(), name='owner-detail'),
]
