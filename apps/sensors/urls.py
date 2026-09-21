from rest_framework.routers import DefaultRouter
from apps.sensors.views import SensorViewSet

router = DefaultRouter()

router.register(
    "sensors",
    SensorViewSet,
    basename="sensor",
)

urlpatterns = router.urls