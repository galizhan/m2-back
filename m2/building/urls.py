from django.urls import path, include
from rest_framework import routers

from . import views

app_name = 'buildings'

router = routers.DefaultRouter(trailing_slash=True)
router.register('', views.BuildingViewSet, 'building')

urlpatterns = [
    path('', include(router.urls)),
]
