from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from m2.users.api.views import UserViewSet
from m2.building.urls import router as building_router

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.registry.extend(building_router.registry)


app_name = "api"
urlpatterns = router.urls
