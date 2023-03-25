from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from m2.apartment.models import Apartment
from m2.apartment.serializers import ApartmentSerializer


# Create your views here.
class ApartmentViewSet(viewsets.ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    filter_backends = (DjangoFilterBackend,)
