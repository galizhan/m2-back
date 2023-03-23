from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.serializers import BaseSerializer

from m2.building.models import Building
from m2.building.serializers import BuildingSerializer, BuildingDetailSerializer


# Create your views here.
class BuildingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    
    def get_serializer_class(self) -> type[BaseSerializer]:
        if self.action == 'retrieve':
            return BuildingDetailSerializer
        return super().get_serializer_class()
    
