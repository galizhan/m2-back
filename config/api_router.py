from django.conf import settings
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from m2.users.api.views import UserViewSet
from m2.building.urls import urlpatterns as building_urls
from m2.apartment.urls import urlpatterns as apartment_urls
from m2.main.urls import urlpatterns as main_urls

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)


app_name = "api"
urlpatterns = [
    path("", include(router.urls)),
    path("building/", include(building_urls)),
    path("apartment/", include(apartment_urls)),
    path("main/", include(main_urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
