from django.urls import path, include
from rest_framework import routers

from . import views

app_name = 'level'

router = routers.DefaultRouter(trailing_slash=True)
router.register('level', views.LevelViewSet, 'levels')
router.register('level-buildings', views.LevelBuildingViewSet, 'level-buildings')

urlpatterns = [
    path('', include(router.urls)),
]
