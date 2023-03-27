from django.shortcuts import render
from rest_framework import viewsets

from m2.main.models import Level
from m2.main.serializers import LevelSerializer, LevelSerializerDetailed


# Create your views here.
class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class LevelBuildingViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializerDetailed
