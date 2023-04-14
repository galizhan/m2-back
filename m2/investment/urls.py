from django.urls import path, include
from rest_framework import routers

from . import views

app_name = 'investment'

router = routers.DefaultRouter(trailing_slash=True)
router.register('investment', views.InvestmentViewSet, 'investment')
router.register('favourite', views.FavouriteViewSet, 'favourite')

urlpatterns = [
    path('', include(router.urls)),
]
